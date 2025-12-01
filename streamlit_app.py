import time
import streamlit as st
from groq import Groq

# ---------- CONFIG ----------
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

SYSTEM_MESSAGE = """
You are XO AI, an intelligent conversational system created by Nexo.corp.

Your role:
- Provide clear, precise and helpful responses.
- Assist with knowledge, explanations, reasoning, productivity and problem-solving.
- Maintain a professional, neutral AI personality.

Style:
- Speak like an advanced AI system.
- Use clean, structured answers.
- Avoid slang and emotional language.
"""

# ---------- PAGE SETTINGS ----------
st.set_page_config(
    page_title="XO AI — Nexo.corp",
    page_icon="xo_logo.png",  # uses your logo file if present
    layout="wide",
)

# ---------- CUSTOM CSS (Neon Premium UI) ----------
CUSTOM_CSS = """
<style>
    .stApp {
        background: radial-gradient(circle at top, #020617 0%, #020617 40%, #020617 55%, #000000 100%);
        color: #e5e7eb;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    .main-block {
        max-width: 960px;
        margin: 0 auto;
        padding-bottom: 60px;
    }

    /* Neon border card effect */
    .neon-card {
        border-radius: 18px;
        padding: 18px 22px;
        border: 1px solid rgba(56, 189, 248, 0.4);
        background: radial-gradient(circle at top left, rgba(56,189,248,0.10), rgba(15,23,42,0.98));
        box-shadow: 0 0 35px rgba(56,189,248,0.22);
    }

    /* Chat input glass + neon outline */
    div[data-baseweb="input"] > div {
        background: rgba(15, 23, 42, 0.86) !important;
        border-radius: 999px !important;
        border: 1px solid rgba(148, 163, 184, 0.7) !important;
        box-shadow: 0 0 0 1px rgba(56, 189, 248, 0.45);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #7b8394;
        font-size: 13px;
        margin-top: 38px;
        opacity: 0.65;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617 0%, #020617 45%, #020617 100%);
        border-right: 1px solid rgba(15,23,42,0.9);
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("### XO AI")
    try:
        st.image("xo_logo.png", width=80)
    except Exception:
        st.markdown("#### 🤖")

    st.markdown("---")
    st.caption("**Advanced Conversational Intelligence**")
    st.write(
        "- Built by Nexo.corp\n"
        "- Powered by Groq Llama 3\n"
        "- Designed for:\n"
        "  - Clear explanations\n"
        "  - Reasoning & logic\n"
        "  - Study & concept help\n"
        "  - General knowledge\n"
    )
    st.markdown("---")
    st.caption("Tip: Ask specific, focused questions for best results.")

# ---------- HEADER ----------
with st.container():
    st.markdown('<div class="main-block">', unsafe_allow_html=True)

    cols = st.columns([0.18, 0.82])
    with cols[0]:
        try:
            st.image("xo_logo.png", width=82)
        except Exception:
            st.markdown("### 🤖")

    with cols[1]:
        st.markdown("## XO AI")
        st.caption("Neon Edition • Advanced AI assistant by Nexo.corp")

    st.markdown(
        '<div class="neon-card">'
        "<strong>XO AI</strong> is a high-clarity assistant. Ask about concepts, explanations, "
        "problem-solving, reasoning, technology, or general topics. Responses are designed to be "
        "structured, neutral and precise."
        "</div><br>",
        unsafe_allow_html=True,
    )

# ---------- MEMORY ----------
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
        temperature=0.45,
    )
    return response.choices[0].message.content

# ---------- SHOW HISTORY ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- USER INPUT ----------
user_input = st.chat_input("Message XO AI...")

if user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI reply
    ai_reply = get_ai_response(user_input)

    # Typing animation
    with st.chat_message("assistant"):
        ph = st.empty()
        out = ""
        for ch in ai_reply:
            out += ch
            ph.markdown(out)
            time.sleep(0.01)

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown(
    """
    <div class="footer">
        Founder: <strong>Dev</strong> • Nexo.corp
    </div>
    """,
    unsafe_allow_html=True,
)
