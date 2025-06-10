# 🧑‍🏫 Technical Tutor UI using LLaMA 3.2 + Streamlit

This project is an **interactive chatbot-style technical tutor** that uses **Meta's LLaMA 3.2 Instruct model** through the local **Ollama API** and a modern web interface powered by **Streamlit**.

It is designed to help students ask questions and receive clear, concise answers on engineering, AI, data science, and computer science topics.

---

## 🧠 Features

- 💬 Chat-based interface using LLaMA 3.2
- 🧑‍🎓 Technical explanations in plain English
- 🔄 Maintains chat history per session
- ⚙️ Fast local inference via [Ollama](https://ollama.com)
- 🌐 Simple Streamlit UI

---

## 🖥️ Tech Stack

- [LLaMA 3.2](https://ai.meta.com/llama/)
- [Ollama](https://ollama.com)
- [Streamlit](https://streamlit.io)
- `openai` Python client (Ollama is OpenAI API compatible)
- `.env` for environment variables

---

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/llama3-tutor-ui.git
cd llama3-tutor-ui
pip install streamlit openai python-dotenv
# Install Ollama (if not installed)
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama server
ollama run llama3:8b-instruct
