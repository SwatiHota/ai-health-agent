Research-Work-MSDS---LJMU-
AI Agent for Real-time Health Monitoring and Anomaly Detection
🧠 AI Health Agent with Fitbit Anomaly Detection
An interactive AI-powered health assistant that detects anomalies in Fitbit data, and provides personalized, interpretable feedback using Large Language Models (LLMs).
This project combines data preprocessing, anomaly detection, and natural language AI responses into a complete feedback loop.
⚙️ Features
✅ Upload Fitbit anomaly dataset (CSV)
✅ Detect anomalous days (Anomaly = 1)
✅ Ask natural language questions about anomalies
✅ Get LLM-powered feedback (via Together.ai API)
✅ Chat history stored in SQLite for tracking
✅ Easy-to-use Streamlit Web UI
📊 Workflow
_Data Preparation
Run FitBit_Analysis.ipynb to clean, preprocess, and label Fitbit data anomalies.
Output → fitbit_anomaly_data.csv.
AI Health Agent
Launch final_ai_health_agent.py with Streamlit.
Upload fitbit_anomaly_data.csv.
Select an anomalous day.
Ask health-related questions in natural language.
Get personalized, encouraging AI responses._
1. final_ai_health_agent.py
Type: Streamlit Web App (Python Script)
Description:
This is the main AI Health Agent application built with Streamlit.
Allows users to upload their Fitbit anomaly CSV dataset.
Filters out rows marked as anomalies.
Lets users ask natural language questions about specific anomalous days.
Uses the Together.ai LLM API (DeepSeek-R1-Distill-Llama-70B) to generate interpretable and encouraging health feedback.
Maintains a chat history using SQLite for reference.
2. FitBit_Analysis.ipynb
Type: Jupyter Notebook
Description:
This notebook contains the data preprocessing, anomaly detection, and analysis workflow.
Loads and cleans Fitbit data.
Applies anomaly detection techniques (likely Autoencoder/Statistical checks).
Generates the fitbit_anomaly_data.csv dataset with anomaly labels (Anomaly = 1).
Provides exploratory analysis (EDA) of steps, sleep, calories, and related metrics.
Serves as the backend research notebook for preparing the dataset used by the AI Health Agent.
3. fitbit_anomaly_data.csv
Type: AI Health Agent Dataset (CSV)
Description:
The processed Fitbit dataset with anomaly labels.
Columns include:
-ActivityDate – Date of activity
-TotalSteps – Daily step count
-Calories – Calories burned
-TotalMinutesAsleep – Total minutes of sleep
-Anomaly – Binary flag (1 = anomaly, 0 = normal)
Used as input for the AI Health Agent to provide personalized anomaly-based insights.
📁 Datasets Used
1. dailyActivity_merged.csv
Description:
Contains daily-level Fitbit activity data. Each row represents one user’s activity on a given date.
Key Columns:
Id – Unique user identifier
ActivityDate – Date of activity record
TotalSteps – Number of steps taken
TotalDistance – Distance covered (miles)
Calories – Calories burned
SedentaryMinutes, LightlyActiveMinutes, FairlyActiveMinutes, VeryActiveMinutes – Minutes spent in different activity levels
Use in project:
Used to analyze activity patterns and detect physical activity anomalies (e.g., unusually low steps or calories).
2. sleepDay_merged.csv
Description:
Provides daily sleep monitoring data recorded by Fitbit.
Key Columns:
Id – Unique user identifier
SleepDay – Date of sleep record
TotalSleepRecords – Number of sleep sessions (naps, overnight sleep)
TotalMinutesAsleep – Total duration of sleep (minutes)
TotalTimeInBed – Total time spent in bed (minutes)
Use in project:
Used to detect sleep anomalies (e.g., very low sleep, restless patterns) that may indicate health or lifestyle issues.
3. weightLogInfo_merged.csv
Description:
Contains weight tracking and related health metrics logged by Fitbit users.
Key Columns:
Id – Unique user identifier
Date – Date of weight log
WeightKg, WeightPounds – Weight in kilograms and pounds
BMI – Body Mass Index
IsManualReport – Whether the entry was manually entered or auto-recorded
Fat – Body fat percentage (if available)
Use in project:
Provides body composition and BMI data that can be correlated with activity and sleep anomalies to give holistic health insights.
✅ Together, these datasets allow analysis of activity + sleep + weight to detect daily anomalies and provide AI-generated personalized feedback in the Streamlit Health Agent.

