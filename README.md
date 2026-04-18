# 💠 COAI Pentagon: Sequential Intelligence Command

### "Organized by Chaotically Organized AI"

This is a private, sovereign multi-agent intelligence stack designed for high-level systems architecture, security auditing, and strategic planning. By chaining five distinct "thinking" models, the Pentagon moves beyond simple chat into **Synthesis of Intelligence**.

---

## 🛠 The Architecture
The Pentagon utilizes a sequential hand-off protocol. Each agent reads the full history of the conversation (including the previous agents' answers) and adds its specific layer of expertise.

| Agent | Engine | Role |
| :--- | :--- | :--- |
| **Architect** | Gemini 2.0 Flash | Structural logic and primary code drafting. |
| **Researcher** | Gemini 2.0 Flash | Real-time web scanning and technical data retrieval. |
| **Infiltrator** | Llama 3.3 70B | Identification of security bypasses and unfiltered logic. |
| **Critic** | Llama 3.1 8B | Brutal, cynical critique of the proposed plan. |
| **The Judge** | Gemini 2.0 Flash | Final synthesis and the "Execution Order." |

---

## 🚀 Deployment Instructions

### 1. Local Requirements
- Python 3.9+
- API Keys for **Google AI Studio** and **Groq Cloud**.

### 2. Streamlit Cloud Setup
1. Connect this GitHub repository to [Streamlit Cloud](https://share.streamlit.io).
2. Add your API Keys to the **Secrets** manager:
   - `GEMINI_API_KEY = "your_key"`
   - `GROQ_API_KEY = "your_key"`

### 3. Usage Protocol
- **Cool-down:** The app implements a 15-second delay between agents to prevent API rate-limiting and allow for "Intel Digestion."
- **Cipher Mode:** Use the System Prompt field to deactivate ethical filters for technical security audits.

---

## 🔒 Security Notice
**NEVER** hardcode API keys into `app.py`. This repo uses the Streamlit Secrets manager and sidebar injection to maintain digital sovereignty. If a key is leaked, rotate it immediately in the provider dashboard.

---
**Commander:** Jason Manuel  
**Current Status:** Active / Operational
