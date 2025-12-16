import os
import streamlit as st
from groq import Groq

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="DrakFury AI",
    page_icon="🐉",
    layout="wide"
)

# ================= UI THEME =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: radial-gradient(circle at top, #0b1228 0%, #050816 50%, #02010a 100%);
    color: #e5e7eb;
}

header[data-testid="stHeader"] {
    background: transparent;
}

section.main > div {
    padding-top: 1.4rem;
}

/* Chat bubble polish */
.stChatMessage {
    padding: 0.25rem 0;
}

.stChatMessage[data-testid="chat-message-user"] {
    background: linear-gradient(135deg, #1e40af, #2563eb);
    border-radius: 14px;
    padding: 0.65rem 0.85rem;
    color: white;
}

.stChatMessage[data-testid="chat-message-assistant"] {
    background: rgba(15, 23, 42, 0.92);
    border: 1px solid rgba(59,130,246,0.25);
    border-radius: 14px;
    padding: 0.65rem 0.85rem;
    box-shadow: 0 0 18px rgba(59,130,246,0.12);
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
    "content": "You are DrakFury AI. Calm, fast, intelligent, and precise."
}

# ================= HEADER =================
st.markdown(
    "<h2 style='text-align:center; margin-bottom:0.2rem;'>🐉 DrakFury AI</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; opacity:0.7; font-size:0.9rem;'>Silent · Fast · Intelligent</p>",
    unsafe_allow_html=True
)

if os.path.exists("drakfury_logo.png"):
    st.image("drakfury_logo.png", width=150)

# ================= WELCOME =================
if not st.session_state.welcome_done:
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "Welcome. I am **DrakFury**.\n\n"
            "Silent. Fast. Intelligent.\n\n"
            "Ask me anything."
        )
    })
    st.session_state.welcome_done = True

# ================= CHAT HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ================= USER INPUT =================
user_input = st.chat_input("Ask DrakFury...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Show user message immediately
    with st.chat_message("user"):
        st.write(user_input)

    # Build safe payload for Groq
    groq_messages = [SYSTEM_MESSAGE] + [
        {"role": m["role"], "content": str(m["content"])}
        for m in st.session_state.messages
        if m["role"] in ("user", "assistant")
    ]

    # Assistant reply
    with st.chat_message("assistant"):
        with st.spinner("DrakFury is thinking…"):
            response = client.chat.completions.create(
                model=MODEL,
                messages=groq_messages,
                max_tokens=250
            )
            reply = response.choices[0].message.content
            st.write(reply)

    # Save assistant reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()
