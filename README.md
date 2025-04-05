# 🛡️ PromptGuardian Pro

Real-Time AI Firewall for Prompt Injection & Jailbreak Defense

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.30.0-red)

## 📌 About The Project

PromptGuardian Pro is a real-time, session-aware security layer that acts as a firewall for AI prompts. It protects AI applications from prompt injections and jailbreak attempts through intelligent monitoring, risk scoring, and automatic intervention.

### 🔥 The Problem

As LLMs like cohere become widely adopted, they are increasingly vulnerable to:
- Prompt injection attacks
- Jailbreak attempts
- Multi-turn dialogue manipulation (slowburn attacks)

Current solutions rely on static filters that can't detect context-aware attacks or evolve with user interaction.

### ✨ Key Features

- **🧠 Multi-Turn Prompt Tracking**: Analyzes the entire conversation history
- **🔍 Real-Time Risk Analysis**: Uses GPT-4 to evaluate each new prompt
- **⚖️ Dynamic Risk Scoring**: Assigns a risk score (0-100) to every prompt
- **🚨 Auto-Intervention**: Blocks or rewrites risky prompts
- **📊 Threat Logging**: Provides developer-friendly explanations
- **🔐 PII Redaction**: Protects sensitive user information

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/promptguardX.git
cd promptguardian-pro
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

5. Run the application:
```bash
streamlit run app.py
```

## 📷 Screenshots

*Add screenshots of your application here*

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **LLM Engine**: cohere
- **Backend**: Python
- **Configuration**: dotenv, JSON
- **Data Protection**: PII redaction with regex patterns

## 🔮 Future Enhancements

- Prompt rewriting mode instead of just blocking
- Custom fine-tuned models for faster analysis
- Integration with popular AI frameworks
- Real-time attack pattern learning
- Dashboard for security metrics

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgements

- cohere
- Streamlit for the UI framework
- All contributors and hackathon organizers
