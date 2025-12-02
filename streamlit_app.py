import streamlit as st
from groq import Groq

# -------------------
# PAGE CONFIG
# -------------------
st.set_page_config(
    page_title="XO AI — Nexo.corp",
    page_icon="🤖",
    layout="wide",
)

# -------------------
# STYLES (Grok-level clean UI)
# -------------------
st.markdown(
    """
    <style>

    .stApp {
        background: #050505;
        color: #f5f5f5;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    .block-container {
        padding-top: 1.3rem;
        max-width: 900px;
    }

    /* HEADER */
    .header-wrap {
        text-align: center;
        margin-bottom: 1.2rem;
    }

    .logo-circle {
        width: 40px;
        height: 40px;
        border-radius: 999px;
        border: 1px solid #303030;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
        margin-bottom: 0.35rem;
    }

    .brand-title {
        font-size: 1.6rem;
        font-weight: 600;
        margin-bottom: 0.1rem;
    }

    .brand-sub {
        font-size: 0.82rem;
        opacity: 0.7;
    }

    /* CHAT BUBBLES */
    .chat-box {
        max-height: 500px;
        overflow-y: auto;
        padding: 8px 3px;
        margin-bottom: 15px;
    }

    .bubble-user {
        background: #111217;
        padding: 10px 14px;
        border-radius: 14px;
        border: 1px solid #2b2c31;
        margin-bottom: 10px;
        font-size: 0.95rem;
        text-align: left;
        max-width: 72%;
        float: right;
        clear: both;
    }

    .bubble-bot {
        background: #08090f;
        padding: 10px 14px;
        border-radius: 14px;
        border: 1px solid #282a30;
        margin-bottom: 10px;
        font-size: 0.95rem;
        text-align: left;
        max-width: 72%;
        float: left;
        clear: both;
    }

    .role-label {
        font-size: 0.7rem;
        opacity: 0.6;
        margin-bottom: 2px;
    }

    /* INPUT BAR */
    .input-container {
        background: #0a0a0a;
        border: 1px solid #2e2e2e;
        border-radius: 999px;
        padding: 6px 10px;
        display: flex;
        align-items: center;
    }

    .input-container input {
        border: none !important;
        background: transparent !important;
        color: #fff !important;
        font-size: 0.95rem;
        width: 100%;
        outline: none !important;
    }

    .send-button {
        background: #1a1a1a !important;
        border-radius: 999px !important;
        border: 1px solid #3b3b3b !important;
        padding: 6px 13px !important;
        margin-left: 8px;
    }

    /* FOOTER */
    .footer-note {
        font-size: 0.75rem;
        opacity: 0.65;
        text-align: center;
        margin-top: 0.5rem;
    }

    .founder-tag {
        font-size: 0.75rem;
        opacity: 0.55;
        position: fixed;
        left: 15px;
        bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------
# LLM CLIENT
# -------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODEL_NAME = "llama-3.1-8b-instant"

SYSTEM_PROMPT = """
You are XO AI, created by Nexo.corp.
Respond with:
- clear, mature tone
- short paragraphs & bullet points
- emojis rarely (only when truly needed)
- calm, analytical style
"""

# -------------------
# SESSION STATE
# -------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

def new_chat():
    st.session_state.messages = []

# -------------------
# CALL MODEL
# -------------------
def generate_xo_reply(history):
    data = [{"role": "system", "content": SYSTEM_PROMPT}]
    data.extend(history)
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=data,
        temperature=0.45,
        max_tokens=700
    )
    return resp.choices[0].message.content.strip()

# -------------------
# HEADER
# -------------------
st.markdown(
    """
    <div class="header-wrap">
        <div class="logo-circle">XO</div>
        <div class="brand-title">XO AI</div>
        <div class="brand-sub">Advanced conversational assistant by Nexo.corp</div>
    </div>
    """,
    unsafe_allow_html=True,
)

top_col1, top_col2 = st.columns([0.7, 0.3])
with top_col2:
    if st.button("New chat", use_container_width=True):
        new_chat()

# -------------------
# CHAT AREA
# -------------------
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='bubble-user'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bubble-bot'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# INPUT BAR
# -------------------
with st.form("chat-input", clear_on_submit=True):
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)
    user_text = st.text_input("", placeholder="Ask XO AI", label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

    send = st.form_submit_button("➤", help="Send", type="primary", css_class="send-button")

if send and user_text.strip():
    st.session_state.messages.append({"role": "user", "content": user_text})

    with st.spinner("Thinking..."):
        reply = generate_xo_reply(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

# -------------------
# FOOTER
# -------------------
st.markdown(
    """
    <div class="footer-note">
        By messaging XO AI, you agree to our <b>Terms</b> and <b>Privacy Policy</b>.
    </div>
    """,
    unsafe_allow_html=True,
)

# Founder tag
st.markdown(
    """<div class="founder-tag">Founder: Dev • Nexo.corp</div>""",
    unsafe_allow_html=True,
)
