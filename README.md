
# 🤖 AI Customer Support Agent

## 📌 Project Overview

This project is developed as part of the **Infosys Springboard Virtual Internship Program 7.0** under the **AI Agent Coordination & Decision Engine** project.

The AI Customer Support Agent is a foundational AI agent built using **Python**, **LangChain**, and **Google Gemini**. The agent is designed to understand customer queries and generate accurate, professional, and context-aware responses.

This project demonstrates the implementation of a single AI agent as the first milestone before extending it into a complete multi-agent architecture.

---

# 🎯 Milestone 1 Objectives

- Configure LangChain and required dependencies.
- Develop a foundational AI agent.
- Implement prompt templates.
- Create a basic testing interface.

---

# 🚀 Features

- AI-powered customer support assistant
- LangChain integration
- Google Gemini integration
- Prompt-based response generation
- Interactive command-line interface
- Modular project structure
- Easy to extend into a multi-agent system

---

# 🏗️ Project Architecture

```
User Query
     │
     ▼
Customer Support Agent
     │
     ▼
LangChain Framework
     │
     ▼
Google Gemini
     │
     ▼
AI Generated Response
```

---

# 🛠️ Technologies Used

- Python
- LangChain
- Google Gemini API
- python-dotenv
- Git
- GitHub

---

# 📂 Project Structure

```
AI-Customer-Support-Agent/

│── agents/
│     └── research_agent.py

│── prompts/
│     └── system_prompt.txt

│── tests/
│     └── test_agent.py

│── main.py
│── requirements.txt
│── README.md
│── .env.example
│── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Customer-Support-Agent.git
```

Move into the project directory

```bash
cd AI-Customer-Support-Agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root and add your Gemini API key.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# ▶️ Running the Project

```bash
python main.py
```

---

# 💬 Sample Interaction

**User**

```
My order has not been delivered.
```

**AI Agent**

```
I'm sorry for the inconvenience.
Please provide your Order ID so I can check the delivery status and assist you further.
```

---

# 📋 Milestone 1 Deliverables

- ✔ LangChain Configuration
- ✔ Google Gemini Integration
- ✔ Foundational AI Customer Support Agent
- ✔ Prompt Template
- ✔ Basic Testing Interface

---

# 🔮 Future Enhancements

- Multi-Agent Coordination
- Shared Memory
- Knowledge Base Integration
- API Integration
- Web Interface
- Database Support
- Coordinator Agent
- Decision Agent
- Research Agent
- Planning Agent

---

# 👨‍💻 Author

Jesmaa E

Infosys Springboard Virtual Internship Program 7.0

---

# 📄 License

This project is developed for educational purposes as part of the Infosys Springboard Virtual Internship Program.
