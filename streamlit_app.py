import os
import streamlit as st
from groq import Groq

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="DrakFury",
    page_icon="🐉",
    layout="wide"
)

# ================= CHATGPT-LIKE THEME =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0f172a;
    color: #e5e7eb;
}

header[data-testid="stHeader"] {
    background: transparent;
}

/* Remove avatars completely */
.stChatMessageAvatar {
    display: none;
}

/* Chat container spacing */
.stChatMessage {
    padding: 0.4rem 0;
}

/* USER MESSAGE (right side like ChatGPT) */
.stChatMessage[data-testid="chat-message-user"] {
    display: flex;
    justify-content: flex-end;
}

.stChatMessage[data-testid="chat-message-user"] > div {
    background: #1e293b;
    border-radius: 12px;
    padding: 0.6rem 0.8rem;
    max-width: 75%;
}

/* ASSISTANT MESSAGE (left side) */
.stChatMessage[data-testid="chat-message-assistant"] {
    display: flex;
    justify-content: flex-start;
}

.stChatMessage[data-testid="chat-message-assistant"] > div {
    background: #020617;
    border-radius: 12px;
    padding: 0.6rem 0.8rem;
    max-width: 75%;
    border: 1px solid rgba(148,163,184,0.15);
}

/* Input box */
textarea {
    background: #020617 !important;
    color: #e5e7eb !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ================= STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "welcome_done" not in st.session_state:
    st.session_state.welcome_done = False

# ================= GROQ =================
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.1-8b-instant"

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are DrakFury. "
        "Talk like a real human. "
        "Short, calm, direct replies. "
        "No robotic explanations."
    )
}

# ================= HEADER =================
st.markdown(
    "<h2 style='text-align:center; margin-bottom:0.2rem;'>DrakFury</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; opacity:0.6; font-size:0.85rem;'>Silent · Fast · Intelligent</p>",
    unsafe_allow_html=True
)

if os.path.exists("drakfury_logo.png"):
    st.image("drakfury_logo.png", width=120)

# ================= WELCOME =================
if not st.session_state.welcome_done:
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hey. I’m DrakFury.\n\nWhat do you want to talk about?"
    })
    st.session_state.welcome_done = True

# ================= CHAT HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=None):
        st.write(msg["content"])

# ================= USER INPUT =================
user_input = st.chat_input("Message DrakFury…")

if user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar=None):
        st.write(user_input)

    # Build Groq-safe messages
    groq_messages = [SYSTEM_MESSAGE] + [
        {"role": m["role"], "content": str(m["content"])}
        for m in st.session_state.messages
        if m["role"] in ("user", "assistant")
    ]

    # Assistant reply
    with st.chat_message("assistant", avatar=None):
        with st.spinner("Thinking…"):
            response = client.chat.completions.create(
                model=MODEL,
                messages=groq_messages,
                max_tokens=200
            )
            reply = response.choices[0].message.content
            st.write(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()
