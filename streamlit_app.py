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

/* Remove avatar spacing */
.stChatMessageAvatar {
    display: none;
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
        "Talk like a calm, smart human. "
        "No robotic phrases. "
        "No explaining greetings. "
        "Keep replies short unless asked. "
        "Be friendly and natural."
    )
}

# ================= HEADER =================
st.markdown(
    "<h2 style='text-align:center; margin-bottom:0.2rem;'>DrakFury</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; opacity:0.7; font-size:0.85rem;'>Silent · Fast · Intelligent</p>",
    unsafe_allow_html=True
)

if os.path.exists("drakfury_logo.png"):
    st.image("drakfury_logo.png", width=140)

# ================= WELCOME =================
if not st.session_state.welcome_done:
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Welcome. I’m DrakFury.\n\nAsk me anything."
    })
    st.session_state.welcome_done = True

# ================= CHAT HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=None):
        st.write(msg["content"])

# ================= USER INPUT =================
user_input = st.chat_input("Type here...")

if user_input:
    # Save + show user message immediately
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user", avatar=None):
        st.write(user_input)

    # Build Groq-safe payload
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
