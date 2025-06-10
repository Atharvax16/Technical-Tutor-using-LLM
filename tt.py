import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load .env for base URL
load_dotenv()
URL = os.getenv("URL")

# Ollama setup
client = OpenAI(base_url=URL, api_key='ollama')  # dummy key for local Ollama
MODEL = "llama3.2"

# System prompt
SYSTEM_PROMPT = "You are a helpful technical tutor for engineering students. Explain concepts clearly and simply."

# Set Streamlit page
st.set_page_config(page_title="Technical Tutor", page_icon="🧑‍🏫")
st.title("🧑‍🏫 Technical Tutor using LLaMA 3.2")

# Session state for chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    speaker = "🧑 You" if msg["role"] == "user" else "🤖 Tutor"
    st.markdown(f"**{speaker}:** {msg['content']}")

# Input box
user_input = st.chat_input("Ask your question here...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from LLaMA 3.2
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state.messages,
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})

        # Display reply
        st.markdown(f"**🤖 Tutor:** {reply}")
