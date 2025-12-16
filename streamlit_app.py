import os
import streamlit as st
from groq import Groq

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="DrakFury AI",
    page_icon="🐉",
    layout="wide"
)

# ================= THEME =================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #0a0f1f, #050816, #02010a);
    color: #e5e7eb;
}
header[data-testid="stHeader"] { background: transparent; }
</style>
""", unsafe_allow_html=True)

# ================= STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = False

# ================= GROQ =================
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.1-8b-instant"

# ================= HEADER =================
st.markdown("<h2 style='text-align:center'>🐉 DrakFury AI</h2>", unsafe_allow_html=True)

if os.path.exists("drakfury_logo.png"):
    st.image("drakfury_logo.png", width=160)

# ================= WELCOME =================
if not st.session_state.welcome_shown:
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Welcome. I am DrakFury.\n\nSilent. Fast. Intelligent.\n\nAsk me anything."
    })
    st.session_state.welcome_shown = True

# ================= CHAT HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ================= INPUT =================
user_input = st.chat_input("Ask DrakFury...")

if user_input:
    # add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("assistant"):
        with st.spinner("DrakFury is thinking…"):
            response = client.chat.completions.create(
                model=MODEL,
                messages=st.session_state.messages,
                max_tokens=250
            )
            reply = response.choices[0].message.content
            st.write(reply)

    # add assistant reply (ONLY role + content)
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
