import os
import streamlit as st
from groq import Groq

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="DrakFury AI — Nexo.corp",
    page_icon="🐉",
    layout="wide"
)

# ================= THEME =================
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #0a0f1f 0%, #050816 45%, #02010a 100%);
        color: #e5e7eb;
    }
    header[data-testid="stHeader"] { background: transparent; }
    </style>
    """,
    unsafe_allow_html=True
)

# ================= STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = False

# ================= GROQ =================
def groq_client():
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"

# ================= HEADER =================
st.markdown("<h2 style='text-align:center'>🐉 DrakFury AI</h2>", unsafe_allow_html=True)

if os.path.exists("drakfury_logo.png"):
    st.image("drakfury_logo.png", width=180)

# ================= WELCOME MESSAGE =================
if not st.session_state.welcome_shown:
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "Welcome. I am DrakFury.\n\n"
            "Silent. Fast. Intelligent.\n\n"
            "Ask me anything."
        )
    })
    st.session_state.welcome_shown = True

# ================= CHAT HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ================= USER INPUT =================
user_input = st.chat_input("Ask DrakFury...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("assistant"):
        with st.spinner("DrakFury is thinking…"):
            response = groq_client().chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are DrakFury AI. Calm, fast, precise."}
                ] + st.session_state.messages,
                max_tokens=250
            )

            reply = response.choices[0].message.content
            st.write(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    st.rerun()
