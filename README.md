# 🤖 LLM-Based Multi-Agent Digital Assistant

A sample project demonstrating how to build a **multi-agent AI system** for enterprise-grade digital assistance using a graph-based workflow and large language models.

---

## 📌 Overview

This project showcases the implementation of a **multi-agent AI architecture**, where multiple autonomous agents collaborate to perform complex tasks and deliver intelligent responses.

Each agent is designed with a specific responsibility, enabling the system to provide both:

- 🧠 **Logical Assistance** – Analytical, fact-based responses  
- ❤️ **Emotional Assistance** – Empathetic, human-like interactions  

---

## 🧩 Key Features

### 🔹 Multi-Agent System
- Multiple autonomous AI agents working together
- Task specialization across agents (e.g., reasoning vs emotional intelligence)
- Collaborative decision-making

### 🔹 Graph-Based Workflow (DAG)
- Directed Acyclic Graph (DAG) structure
- Ensures:
  - No cyclic dependencies
  - Efficient task execution
  - Clear flow of control between agents

### 🔹 Dual Assistance Modes
- **Logical Digital Assistant**
  - Handles reasoning, structured thinking, and factual queries
- **Emotional Digital Assistant**
  - Provides supportive, empathetic, and context-aware responses

### 🔹 Powered by Gemini LLM
- Integrated with **Google’s Gemini Large Language Model**
- Enables:
  - Natural language understanding
  - Context-aware conversations
  - Intelligent response generation

---

## 🏗️ Architecture Overview

```text
            User Input
                 │
                 ▼
        ┌─────────────────┐
        │  Input Analyzer │
        └─────────────────┘
                 │
     ┌───────────┴───────────┐
     ▼                       ▼
┌──────────────┐     ┌──────────────┐
│ Logical Agent│     │ Emotional Agent│
└──────────────┘     └──────────────┘
     │                       │
     └───────────┬───────────┘
                 ▼
        ┌─────────────────┐
        │ Response Builder│
        └─────────────────┘
                 │
                 ▼
            Final Output
```

## 🚀 Getting Started
### Prerequisites
```text
Python 3.8+
Access to Gemini API (Google AI)
Required dependencies (install via requirements.txt if provided)
```

### Installation
```text
git clone https://github.com/brij-joe/digi-assist.git
cd digi-assist
uv venv .venv
.venv\Scripts\activate
uv sync
```
## Run the Project
```text
python src\multi-agent-main.py
or
uv run src\multi-agent-main.py
```

## 📚 Use Cases
- Enterprise virtual assistants
- Customer support automation
- Mental wellness companions
- Intelligent workflow automation
- Conversational AI systems

## ⚠️ Disclaimer
This project is a sample implementation intended for learning and demonstration purposes. It provides a conceptual foundation for building enterprise-grade multi-agent systems.

## 📬 Contact
For technical guidance, enterprise implementations, or collaboration:
📧 Email: brij_joe@yahoo.com

# ⭐ Support
If you find this project useful, consider giving it a ⭐ on GitHub!

---