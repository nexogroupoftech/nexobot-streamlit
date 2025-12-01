import time
import streamlit as st
from groq import Groq

# ---------- CONFIG ----------
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

SYSTEM_MESSAGE = """
You are NexoBot, an AI assistant created by Nexo.corp.

Your role:
- Help with studies, motivation, basic tech/AI questions and life doubts.
- Speak simple English with a little friendly Hinglish.
- Be kind, calm, supportive, and non-judgmental.

Style:
- Talk like a smart, chill older brother from India.
- Never be rude.
- Keep answers clear and not too long unless user asks for more detail.
"""

# ---------- PAGE & THEME ----------
st.set_page_config(
    page_title="Nexo.corp AI Chatbot",
    page_icon="🤖",
    layout="wide",
)

# Custom CSS (dark gradient + bubble tweaks + footer styling)
CUSTOM_CSS = """
<style>
    .stApp {
        background: radial-gradient(circle at top, #020617 0%, #020617 40%, #000000 100%);
        color: #e5e7eb;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    .main-block {
        max-width: 900px;
        margin: 0 auto;
        padding-bottom: 60px;
    }
    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 14px;
        margin-top: 40px;
        opacity: 0.55;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------- HEADER ----------
with st.container():
    st.markdown('<div class="main-block">', unsafe_allow_html=True)

    cols = st.columns([0.15, 0.85])
    with cols[0]:
        try:
            st.image("nexo_logo.png", width=64)
        except:
            st.markdown("## 🤖")

    with cols[1]:
        st.markdown("### NexoBot — your calm AI big brother")
        st.caption("Built by Nexo.corp • Powered by Groq Llama 3")

    st.markdown("---")

# ---------- SESSION MEMORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- AI CALL ----------
def get_ai_response(user_msg: str) -> str:
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
    messages.extend(st.session_state.messages)
    messages.append({"role": "user", "content": user_msg})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content

# ----------- SHOW HISTORY ----------
st.markdown('<div class="main-block">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------- USER INPUT ----------
user_input = st.chat_input("Type your message...")

if user_input:
    # User bubble
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI response
    ai_reply = get_ai_response(user_input)

    # Typing animation
    with st.chat_message("assistant"):
        placeholder = st.empty()
        display = ""
        for ch in ai_reply:
            display += ch
            placeholder.markdown(display)
            time.sleep(0.01)

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown(
    """
    <div class="footer">
        Made by <strong>Dev</strong> • Nexo.corp 💙
    </div>
    """,
    unsafe_allow_html=True,
)
