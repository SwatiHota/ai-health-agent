import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOGETHER_API_KEY = "tgp_v1_9XbcpxVHW9-j7ZfyU8ssmSaW1Rb-BIp_o0kQMq4UP80"

# Setup DB for chat history
conn = sqlite3.connect("chat_history.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS history (timestamp TEXT, role TEXT, message TEXT)")
conn.commit()

def log_chat(role, message):
    c.execute("INSERT INTO history (timestamp, role, message) VALUES (?, ?, ?)",
              (datetime.now().isoformat(), role, message))
    conn.commit()

def get_together_response(data, custom_question):
    prompt = f"""
    You are a friendly AI health assistant. The user wants help with their Fitbit data:
    - TotalSteps: {data['TotalSteps']}
    - Sleep: {data['sleep']} hours
    - Calories: {data['calories']} kcal

    Question: \"{custom_question}\"

    Give an informative, encouraging response using the data.
    """

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "top_p": 0.7
    }

    res = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=payload)
    if res.status_code == 200:
        return res.json()["choices"][0]["message"]["content"]
    else:
        return f"⚠️ Error from Together.ai: {res.status_code} - {res.text}"

# Streamlit UI
st.set_page_config(page_title="AI Health Agent (User-Prompted)", page_icon="🧠")
st.title("🧠 AI Health Agent")
st.caption("Upload your Fitbit data. Ask questions only for rows marked as anomalies.")

uploaded_file = st.file_uploader("📂 Upload Fitbit CSV", type=["csv"])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        df.columns = df.columns.str.strip()
        st.success("✅ File uploaded successfully.")
        st.write(df.head())

        required_columns = {"TotalSteps", "Calories", "TotalMinutesAsleep", "Anomaly"}
        if not required_columns.issubset(df.columns):
            st.error("❌ Missing required columns: TotalSteps, Calories, TotalMinutesAsleep, Anomaly")
        else:
            anomalies = df[df["Anomaly"] == 1]

            if anomalies.empty:
                st.warning("⚠️ No anomalies found in your data.")
            else:
                st.subheader("📅 Anomalous Dates Detected")
                
                if "ActivityDate" in anomalies.columns:
                    available_dates = anomalies["ActivityDate"].astype(str).unique().tolist()
                else:
                    available_dates = [f"Row {i}" for i in anomalies.index]

                selected_date = st.selectbox("Select an anomalous day to ask a question:", available_dates)

                st.markdown("💡 **Example prompts:**")
                st.markdown("""
                - Why did I sleep less on this day?
                - How can I improve my activity after this anomaly?
                - Is my step count okay on this day?
                - What might be the reason for this anomaly?
                """)

                user_question = st.text_input("Ask a question based on this anomaly")

                if user_question and selected_date:
                    # Get the selected row
                    if "ActivityDate" in anomalies.columns:
                        selected_row = anomalies[anomalies["ActivityDate"].astype(str) == selected_date].iloc[0]
                    else:
                        row_index = int(selected_date.split()[-1])
                        selected_row = anomalies.loc[row_index]

                    data_point = {
                        "TotalSteps": int(selected_row["TotalSteps"]),
                        "sleep": round(selected_row["TotalMinutesAsleep"] / 60, 1),
                        "calories": int(selected_row["Calories"])
                    }

                    with st.chat_message("user"):
                        st.markdown(f"**{selected_date}**: {user_question}")
                    log_chat("user", f"{selected_date}: {user_question}")

                    ai_response = get_together_response(data_point, user_question)

                    with st.chat_message("assistant"):
                        st.markdown(ai_response)
                    log_chat("assistant", ai_response)

    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")

# Chat History
with st.expander("📜 Chat History"):
    rows = c.execute("SELECT timestamp, role, message FROM history ORDER BY timestamp DESC LIMIT 10").fetchall()
    for ts, role, msg in rows:
        st.markdown(f"**{role.capitalize()}** ({ts.split('T')[0]}): {msg}")
