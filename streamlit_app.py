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
    /* Remove default Streamlit top bar & menu */
    header[data-testid="stHeader"] {
        display: none;
    }
    #MainMenu, footer {
        visibility: hidden;
    }

    html, body, .stApp {
        height: 100%;
        background: #050505;
        color: #f5f5f5;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    .block-container {
        padding-top: 1.0rem;
        padding-bottom: 0;
        max-width: 900px;
    }

    /* Header simple text */
    .header-wrap {
        text-align: left;
        margin-bottom: 1.8rem;
        font-size: 1.1rem;
        font-weight: 600;
        opacity: 0.9;
    }

    /* Chat wrapper so bottom bar doesn't overlap */
    .chat-wrapper {
        padding-bottom: 120px; /* space for bottom bar */
    }

    /* Chat area centered like Grok */
    .chat-box {
        max-width: 680px;
        margin: 0 auto;
        max-height: calc(100vh - 220px);
        overflow-y: auto;
        padding: 4px 2px 4px 2px;
    }

    .user-bubble {
        background: #14151b;
        border-radius: 999px;
        border: 1px solid #30323a;
        padding: 8px 14px;
        margin-bottom: 10px;
        max-width: 70%;
        float: right;
        clear: both;
        font-size: 0.95rem;
        text-align: left;
    }

    .bot-text {
        margin-bottom: 12px;
        font-size: 0.95rem;
        max-width: 70%;
        float: left;
        clear: both;
    }

    .bot-text-center {
        margin-bottom: 18px;
        font-size: 1.05rem;
        text-align: left;
        max-width: 70%;
        margin-left: 0;
        clear: both;
    }

    /* Bottom dock bar like Grok */
    .bottom-bar {
        position: fixed;
        left: 0;
        right: 0;
        bottom: 0;
        background: #050505;
        border-top: 1px solid #2b2b2b;
        padding: 10px 16px 12px 16px;
        z-index: 999;
    }

    .bottom-inner {
        max-width: 900px;
        margin: 0 auto;
    }

    .input-shell {
        background: #050607;
        border-radius: 999px;
        border: 1px solid #2b2b2b;
        padding: 4px 6px 4px 14px;
        display: flex;
        align-items: center;
    }

    .input-shell input {
        border: none !important;
        background: transparent !important;
        color: #ffffff !important;
        font-size: 0.95rem;
    }

    .input-shell input:focus {
        outline: none !important;
    }

    /* Send button: small circle with arrow */
    .stButton>button {
        border-radius: 999px;
        border: 1px solid #3b3b3b;
        background: #151515;
        color: #f5f5f5;
        padding: 0;
        height: 32px;
        width: 32px;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .footer-note {
        font-size: 0.75rem;
        opacity: 0.65;
        text-align: center;
        margin-top: 0.35rem;
    }

    .founder-tag {
        font-size: 0.75rem;
        opacity: 0.55;
        position: fixed;
        left: 15px;
        bottom: 46px;  /* a bit above bar */
        z-index: 900;
    }

    @media (max-width: 768px) {
        .block-container {
            padding-top: 0.6rem;
        }
        .chat-box {
            max-width: 100%;
            padding: 0 4px;
        }
        .bottom-bar {
            padding: 8px 10px 10px 10px;
        }
        .founder-tag {
            bottom: 56px;
            font-size: 0.7rem;
        }
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
- Use emojis rarely, only when they truly add value.
- No cringe or over-excited style.

Skills:
- Study help, explanations, reasoning, tech, maths, science.
- Simple, practical life and productivity advice.
- For graphs/diagrams/images, describe them in words; optionally give short Python code or image prompts.

Style:
- Short paragraphs and bullet points when helpful.
- Be honest if unsure instead of guessing.
"""

# -------------------
# STATE
# -------------------
if "messages" not in st.session_state:
    # Start with a Grok-style greeting from XO AI
    st.session_state.messages = [
        {"role": "assistant", "content": "hey, what’s up? 🙂"}
    ]

def new_chat():
    st.session_state.messages = [
        {"role": "assistant", "content": "hey, what’s up? 🙂"}
    ]

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
top1, top2 = st.columns([0.85, 0.15])
with top1:
    st.markdown('<div class="header-wrap">XO AI</div>', unsafe_allow_html=True)
with top2:
    if st.button("New chat"):
        new_chat()

# -------------------
# CHAT DISPLAY
# -------------------
st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="chat-box">', unsafe_allow_html=True)

first = True
for msg in st.session_state.messages:
    if msg["role"] == "assistant" and first:
        # first assistant message a bit bigger (like Grok greeting)
        st.markdown(
            f'<div class="bot-text-center">{msg["content"]}</div>',
            unsafe_allow_html=True,
        )
        first = False
    elif msg["role"] == "user":
        st.markdown(
            f'<div class="user-bubble">{msg["content"]}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="bot-text">{msg["content"]}</div>',
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# BOTTOM INPUT BAR (fixed like Grok)
# -------------------
st.markdown('<div class="bottom-bar"><div class="bottom-inner">', unsafe_allow_html=True)

with st.form("chat-input", clear_on_submit=True):
    cols = st.columns([0.92, 0.08])
    with cols[0]:
        st.markdown('<div class="input-shell">', unsafe_allow_html=True)
        user_text = st.text_input(
            "",
            placeholder="How can XO help?",
            label_visibility="collapsed",
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with cols[1]:
        send = st.form_submit_button("↑")

# Terms below input, still inside bottom bar
st.markdown(
    """
    <div class="footer-note">
        By messaging XO AI, you agree to our <b>Terms</b> and <b>Privacy Policy</b>.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div></div>", unsafe_allow_html=True)  # close bottom-inner + bottom-bar

if send and user_text.strip():
    st.session_state.messages.append({"role": "user", "content": user_text.strip()})
    with st.spinner("Thinking..."):
        answer = xo_reply(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()

# -------------------
# FOUNDER TAG
# -------------------
st.markdown(
    '<div class="founder-tag">Founder: Dev • Nexo.corp</div>',
    unsafe_allow_html=True,
)
