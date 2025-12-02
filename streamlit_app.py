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
# BASIC STYLES (Grok-like)
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
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        max-width: 900px;
    }

    /* Center header like Grok */
    .header-wrap {
        text-align: center;
        margin-bottom: 1.5rem;
    }

    .logo-circle {
        width: 42px;
        height: 42px;
        border-radius: 999px;
        border: 1px solid #3f3f3f;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1.4rem;
        margin-bottom: 0.4rem;
    }

    .brand-title {
        font-size: 1.8rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        margin-bottom: 0.25rem;
    }

    .brand-sub {
        font-size: 0.85rem;
        opacity: 0.7;
    }

    /* Chat area */
    .chat-container {
        max-height: 480px;
        overflow-y: auto;
        padding: 0.75rem 0.25rem 0.5rem 0.25rem;
        margin-bottom: 0.75rem;
    }

    .user-bubble, .bot-bubble {
        padding: 10px 14px;
        border-radius: 12px;
        font-size: 0.95rem;
        margin-bottom: 8px;
    }

    .user-bubble {
        background: #111218;
        border: 1px solid #292a33;
    }

    .bot-bubble {
        background: #08090f;
        border: 1px solid #282a34;
    }

    .role-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        opacity: 0.6;
        margin-bottom: 2px;
    }

    /* Big input bar like Grok */
    .input-wrap {
        border-radius: 999px;
        border: 1px solid #2d2f38;
        background: #050607;
        display: flex;
        align-items: center;
        padding: 4px 10px;
    }

    .input-wrap input {
        border: none !important;
        background: transparent !important;
        color: #f5f5f5 !important;
    }

    .send-button {
        border-radius: 999px !important;
    }

    .foot-note {
        font-size: 0.75rem;
        opacity: 0.6;
        text-align: center;
        margin-top: 0.6rem;
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
You are XO AI, an advanced assistant created by Nexo.corp.

Tone:
- Calm, clear, mature. Like a smart, neutral analyst.
- Use emojis rarely, only when they really add value (for example, once in a while, not every reply).
- No over-excited or cringe style.

Skills:
- Explain study concepts, maths, science, logic and technology.
- Help with planning (study routine, learning path).
- Provide grounded, practical life advice.
- When user asks for graphs/diagrams/images, describe them in words and optionally give short Python code or an image prompt.

Style:
- Prefer short paragraphs and bullet points.
- Be honest about uncertainty instead of guessing.
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
    """history: list of {'role': 'user'/'assistant', 'content': '...'}"""
    messages_for_model = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages_for_model.extend(history)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages_for_model,
        temperature=0.4,
        max_tokens=700,
    )
    return response.choices[0].message.content.strip()

# -------------------
# HEADER (Grok style)
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

# Simple "New chat" button at top-right
top_col1, top_col2 = st.columns([0.7, 0.3])
with top_col2:
    if st.button("New chat", use_container_width=True):
        new_chat()

st.markdown("")

# -------------------
# CHAT AREA
# -------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]

    if role == "user":
        st.markdown("<div class='role-label'>YOU</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='user-bubble'>{content}</div>", unsafe_allow_html=True)
    elif role == "assistant":
        st.markdown("<div class='role-label'>XO AI</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='bot-bubble'>{content}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# INPUT (Ask XO AI bar)
# -------------------
with st.form(key="chat-form", clear_on_submit=True):
    # We fake a Grok-like bar by styling the container, but real input is normal text_input
    st.markdown("<div class='input-wrap'>", unsafe_allow_html=True)
    user_input = st.text_input(
        "",
        placeholder="Ask XO AI",
        label_visibility="collapsed",
    )
    st.markdown("</div>", unsafe_allow_html=True)
    submitted = st.form_submit_button("Send", use_container_width=True)

if submitted and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})

    with st.spinner("XO AI is thinking..."):
        reply = generate_xo_reply(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

# -------------------
# FOOTER (Terms & Privacy)
# -------------------
st.markdown(
    """
    <div class="foot-note">
        By messaging XO AI, you agree to our <b>Terms</b> and <b>Privacy Policy</b>.
        (Add your real links here later.)
    </div>
    """,
    unsafe_allow_html=True,
)
