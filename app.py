import streamlit as st
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

# -----------------------------
# Load API Key
# -----------------------------
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -----------------------------
# Page Settings
# -----------------------------
st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖"
)

st.title("🤖 My AI Assistant")

# -----------------------------
# Chat Memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
user_message = st.chat_input("Type your message...")

if user_message:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.markdown(user_message)

    # Get Gemini response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message
    )

    ai_reply = response.text

    # Save AI reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_reply
    })

    with st.chat_message("assistant"):
        st.markdown(ai_reply)