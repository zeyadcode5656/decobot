# 🤖 DecoBot — Rule-Based AI Chatbot

A hybrid AI chatbot built from scratch with Python and Flask, deployed live on the internet.
Built as Project 1 of the DecodeLabs AI Engineering Program — Batch 2026.

## 🌐 Live Demo
👉 https://zeyad5656.pythonanywhere.com

## 🎯 What is DecoBot?
DecoBot is a rule-based AI chatbot that uses a hybrid architecture:
- **Rules first** — instant O(1) dictionary lookup for known intents
- **LLM second** — Groq (Llama 3.3 70B) fallback for unknown questions

## ✨ Features
- ⚡ Instant rule-based responses using Python dictionaries
- 🧠 Groq LLM fallback for complex questions
- 💾 Conversation memory system
- 🔍 Smart partial matching with word boundary detection
- 🎲 Response variety using random selection
- 🌐 Beautiful web UI with Flask
- 🌙 Dark / Light mode toggle
- ⌨️ Typing animation
- 📋 Copy message button
- 🕐 Timestamps on every message
- 📊 Message counter and session timer
- 📱 Fully mobile responsive
- 🔐 Secure API key management

## 🏗️ Architecture
User Input
↓
Sanitization (.lower().strip())
↓
Memory Check → handles personal info
↓
Rule-Based Dictionary → O(1) instant response
↓
Groq LLM Fallback → answers anything else
↓
Response sent back to browser
## 🛠️ Tech Stack
- **Python** — core logic
- **Flask** — web framework
- **Groq API** — LLM fallback (Llama 3.3 70B)
- **HTML/CSS/JS** — frontend
- **PythonAnywhere** — deployment
- **Git/GitHub** — version control

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/zeyadcode5656/decobot.git
cd decobot

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GROQ_API_KEY=your-key-here" > .env

# Run the app
python app.py
```

## 📁 Project Structure
decobot/
├── app.py              ← Flask backend + chatbot logic
├── requirements.txt    ← Python dependencies
├── Procfile           ← Deployment config
├── .env               ← API key (never shared)
├── .gitignore         ← Protects .env
└── templates/
└── index.html     ← Chat interface
## 💡 Key Concepts Learned
- Control flow and decision-making logic
- Dictionary O(1) vs if-elif O(n) algorithmic efficiency
- Input sanitization and normalization
- Hybrid AI architecture (rules + LLM)
- REST API integration
- Flask web development
- Git version control and deployment

## 👨‍💻 Author
**Zeyad Sayed** — AI Engineering Student at DecodeLabs, Batch 2026

## 🔗 Connect
- LinkedIn: linkedin.com/in/zeyadcode5656
- GitHub: github.com/zeyadcode5656