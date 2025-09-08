
# AI Health Agent - Fitbit Anomaly Detection

## 🧠 Smart Health Monitoring with AI Feedback

An intelligent health monitoring system that analyzes Fitbit data to detect anomalies and provides personalized AI-powered feedback for better health insights.

### 🌟 Features

- **Anomaly Detection**: Automatically identifies unusual patterns in your health data
- **AI-Powered Insights**: Get personalized health advice using advanced AI models
- **Interactive Chat**: Ask questions about specific anomalous days in your data
- **Privacy-First**: Your data stays secure and is processed locally
- **Easy to Use**: Simple web interface powered by Streamlit

### 🚀 Live Demo

**[Try the App Live →](https://your-app-name.streamlit.app)**

### 📊 How It Works

1. **Upload Data**: Upload your Fitbit CSV data containing steps, sleep, and calories
2. **Detect Anomalies**: The system identifies days with unusual activity patterns
3. **Ask Questions**: Select anomalous days and ask specific questions
4. **Get AI Insights**: Receive personalized health advice and explanations

### 🛠️ Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-health-agent.git
cd ai-health-agent

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "TOGETHER_API_KEY=your_api_key_here" > .env

# Run the application
streamlit run final_ai_health_agent.py
```

### 📁 Data Format

Your CSV file should contain these columns:
- `TotalSteps`: Daily step count
- `Calories`: Calories burned
- `TotalMinutesAsleep`: Sleep duration in minutes
- `Anomaly`: Binary flag (0=normal, 1=anomaly)
- `ActivityDate` (optional): Date of the record

### 🔐 Environment Variables

Set up your Together.ai API key:
- `TOGETHER_API_KEY`: Your API key from [Together.ai](https://together.ai)

### 📝 Example Usage

1. Upload your processed Fitbit data with anomaly detection results
2. Browse anomalous days in the dropdown
3. Ask questions like:
   - "Why did I sleep less on this day?"
   - "How can I improve my activity after this anomaly?"
   - "What might be the reason for this anomaly?"

### 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- AI powered by [Together.ai](https://together.ai)
- Inspired by advances in wearable health technology

### 📞 Support

If you have questions or need help:
- Open an [Issue](https://github.com/yourusername/ai-health-agent/issues)
- Check the [Documentation](https://github.com/yourusername/ai-health-agent/wiki)

---

**Made with ❤️ for better health insights**
