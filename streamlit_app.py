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
# STYLES
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
        padding-top: 1.2rem;
        max-width: 900px;
    }

    /* Header like Grok */
    .header-wrap {
        text-align: left;
        margin-bottom: 1.4rem;
        font-size: 1.4rem;
        font-weight: 600;
    }

    /* Chat area */
    .chat-box {
        max-height: 500px;
        overflow-y: auto;
        padding: 6px 2px 10px 2px;
        margin-bottom: 16px;
    }

    .user-bubble {
        background: #13141a;
        border-radius: 999px;
        border: 1px solid #30323a;
        padding: 8px 14px;
        margin-bottom: 10px;
        max-width: 65%;
        float: right;
        clear: both;
        font-size: 0.95rem;
        text-align: left;
    }

    .bot-text {
        margin-bottom: 12px;
        font-size: 0.95rem;
        max-width: 80%;
        float: left;
        clear: both;
    }

    /* Input bar */
    .input-wrapper {
        background: #050607;
        border-radius: 999px;
        border: 1px solid #2b2b2b;
        padding: 4px 10px;
    }

    .input-wrapper input {
        border: none !important;
        background: transparent !important;
        color: #ffffff !important;
        font-size: 0.95rem;
    }

    .input-wrapper input:focus {
        outline: none !important;
    }

    .stButton>button {
        border-radius: 999px;
        border: 1px solid #3b3b3b;
        background: #121212;
        color: #f5f5f5;
        padding: 6px 10px;
        font-size: 0.9rem;
    }

    .footer-note {
        font-size: 0.75rem;
        opacity: 0.65;
        text-align: center;
        margin-top: 0.6rem;
    }

    .founder-tag {
        font-size: 0.75rem;
        opacity: 0.55;
        position: fixed;
        left: 15px;
        bottom: 8px;
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
You are XO AI, an assistant created by Nexo.corp.

Tone:
- Calm, clear, mature.
- Few emojis, only when really helpful.
- No cringe or over-excited style.

Skills:
- Study help, explanations, reasoning, tech, maths, science.
- Simple, practical advice for life and productivity.
- For graphs/diagrams/images, describe them in words; optionally give short Python code or image prompts.

Style:
- Short paragraphs, bullet points when useful.
- Be honest if you are unsure instead of making things up.
"""

# -------------------
# STATE
# -------------------
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {role: "user"/"assistant", content: str}

def new_chat():
    st.session_state.messages = []

# -------------------
# MODEL CALL
# -------------------
def xo_reply(history):
    msgs = [{"role": "system", "content": SYSTEM_PROMPT}]
    msgs.extend(history)
    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=msgs,
        temperature=0.4,
        max_tokens=700,
    )
    return res.choices[0].message.content.strip()

# -------------------
# HEADER
# -------------------
top1, top2 = st.columns([0.8, 0.2])
with top1:
    st.markdown('<div class="header-wrap">XO AI</div>', unsafe_allow_html=True)
with top2:
    if st.button("New chat"):
        new_chat()

# -------------------
# CHAT DISPLAY
# -------------------
st.markdown('<div class="chat-box">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-text">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# INPUT AREA (Ask XO AI, send button on right)
# -------------------
with st.form("chat-input", clear_on_submit=True):
    cols = st.columns([0.9, 0.1])
    with cols[0]:
        st.markdown('<div class="input-wrapper">', unsafe_allow_html=True)
        user_text = st.text_input(
            "",
            placeholder="Ask XO AI",
            label_visibility="collapsed",
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with cols[1]:
        send = st.form_submit_button("➤")

if send and user_text.strip():
    st.session_state.messages.append({"role": "user", "content": user_text.strip()})
    with st.spinner("Thinking..."):
        answer = xo_reply(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": answer})
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

st.markdown(
    '<div class="founder-tag">Founder: Dev • Nexo.corp</div>',
    unsafe_allow_html=True,
)
