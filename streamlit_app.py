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

header[data-testid="stHeader"] {display: none;}
#MainMenu, footer {visibility: hidden;}

body, .stApp {
    background: #050505;
    color: #ffffff;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* Main container */
.block-container {
    padding-top: 1rem;
    padding-bottom: 0;
    max-width: 900px;
}

/* Header */
.header-wrap {
    text-align: left;
    margin-bottom: 1.5rem;
    font-size: 1.1rem;
    font-weight: 600;
    opacity: 0.9;
}

/* Chat list area (scrolls) */
.chat-box {
    max-width: 750px;
    margin: 0 auto;
    padding-bottom: 150px; /* space above bottom bar */
    max-height: calc(100vh - 140px);
    overflow-y: auto;
}

/* User bubble */
.user-bubble {
    background: #14151b;
    border-radius: 999px;
    padding: 8px 14px;
    margin: 10px 0;
    float: right;
    clear: both;
    max-width: 70%;
    border: 1px solid #30323a;
    font-size: 0.95rem;
}

/* Bot text */
.bot-text {
    float: left;
    clear: both;
    font-size: 0.95rem;
    margin: 10px 0;
    max-width: 70%;
}

/* First greeting a bit larger */
.bot-greeting {
    float: left;
    clear: both;
    font-size: 1.05rem;
    margin: 14px 0 18px 0;
    max-width: 70%;
}

/* ---------- GROK-LIKE BOTTOM BAR ---------- */
.bottom-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;

    padding: 12px 16px 14px 16px;
    border-top: 1px solid #2b2b2b;
    background: #050505;
    z-index: 9999;
}

/* center content */
.bottom-inner {
    max-width: 850px;
    margin: 0 auto;
}

/* input + button row */
.input-row {
    display: flex;
    align-items: center;
}

/* clean pill input */
.input-shell {
    flex: 1;
    display: flex;
    align-items: center;

    background: #111214;
    border-radius: 999px;
    padding: 6px 14px;
    border: 1px solid #2b2b2b;
}

.input-shell input {
    background: transparent !important;
    border: none !important;
    color: #ffffff !important;
    width: 100%;
    padding: 6px 0;
    font-size: 0.95rem;
}
.input-shell input:focus { outline: none !important; }

/* send button */
.stButton>button {
    height: 34px;
    width: 34px;
    border-radius: 999px;
    background: #151515;
    border: 1px solid #3b3b3b;
    color: #ffffff;
    font-size: 16px;
    margin-left: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* terms text under input */
.footer-note {
    font-size: 0.75rem;
    opacity: 0.65;
    text-align: center;
    margin-top: 0.3rem;
}

/* Founder tag */
.founder-tag {
    position: fixed;
    left: 20px;
    bottom: 60px;
    opacity: 0.55;
    font-size: 0.8rem;
    z-index: 9000;
}

/* mobile */
@media (max-width: 768px) {
    .block-container {
        padding-top: 0.6rem;
    }
    .chat-box {
        max-width: 100%;
        padding: 0 6px 150px 6px;
    }
    .bottom-bar {
        padding: 10px 10px 12px 10px;
    }
    .founder-tag {
        bottom: 64px;
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
st.markdown('<div class="chat-box">', unsafe_allow_html=True)

first_assistant_done = False
for msg in st.session_state.messages:
    if msg["role"] == "assistant" and not first_assistant_done:
        st.markdown(
            f'<div class="bot-greeting">{msg["content"]}</div>',
            unsafe_allow_html=True,
        )
        first_assistant_done = True
    elif msg["role"] == "assistant":
        st.markdown(
            f'<div class="bot-text">{msg["content"]}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="user-bubble">{msg["content"]}</div>',
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# BOTTOM BAR (Grok-style)
# -------------------
st.markdown(
    '<div class="bottom-bar"><div class="bottom-inner">',
    unsafe_allow_html=True,
)

with st.form("chat-input", clear_on_submit=True):
    st.markdown('<div class="input-row">', unsafe_allow_html=True)

    # pill input
    st.markdown('<div class="input-shell">', unsafe_allow_html=True)
    user_text = st.text_input(
        "",
        placeholder="How can XO help?",
        label_visibility="collapsed",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # send button
    send = st.form_submit_button("↑")

    st.markdown("</div>", unsafe_allow_html=True)  # close input-row

# terms text
st.markdown(
    """
    <div class="footer-note">
        By messaging XO AI, you agree to our <b>Terms</b> and <b>Privacy Policy</b>.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div></div>", unsafe_allow_html=True)  # bottom-inner + bottom-bar

# -------------------
# SEND HANDLING
# -------------------
if send and user_text.strip():
    st.session_state.messages.append(
        {"role": "user", "content": user_text.strip()}
    )
    with st.spinner("Thinking..."):
        answer = xo_reply(st.session_state.messages)
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
    st.rerun()

# -------------------
# FOUNDER TAG
# -------------------
st.markdown(
    '<div class="founder-tag">Founder: Dev • Nexo.corp</div>',
    unsafe_allow_html=True,
)
