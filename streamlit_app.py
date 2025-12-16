import os
import time
import streamlit as st
from groq import Groq

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="DrakFury AI — Nexo.corp",
    page_icon="🐉",
    layout="wide"
)

# ================= NIGHT FURY UI =================
CUSTOM_CSS = """
<style>
.stApp {
    background: radial-gradient(circle at top left, #0a0f1f 0%, #050816 45%, #02010a 100%);
    color: #e5e7eb;
}

header[data-testid="stHeader"] { background: transparent; }

.block-container {
    max-width: 1100px;
    padding-top: 1.2rem;
}

/* Chat */
.drak-chat { background: transparent; }

/* Rows */
.msg-row { display: flex; margin-bottom: 0.75rem; }
.msg-row.user { justify-content: flex-end; }
.msg-row.assistant { justify-content: flex-start; }

/* Bubbles */
.msg {
    max-width: 78%;
    padding: 0.75rem 0.95rem;
    border-radius: 16px;
    font-size: 0.92rem;
    line-height: 1.55;
}

.msg.user {
    background: linear-gradient(135deg, #1e40af, #2563eb);
    color: #ffffff;
    box-shadow: 0 0 14px rgba(37,99,235,0.35);
}

.msg.assistant {
    background: rgba(10,15,31,0.9);
    border: 1px solid rgba(59,130,246,0.35);
    box-shadow: 0 0 18px rgba(59,130,246,0.15);
}

/* Labels */
.label {
    font-size: 0.65rem;
    letter-spacing: 0.08em;
    opacity: 0.65;
    margin-bottom: 0.25rem;
}

/* Meta */
.meta {
    font-size: 0.65rem;
    opacity: 0.6;
    margin-top: 0.35rem;
    display: flex;
    gap: 0.9rem;
}
.meta span { cursor: pointer; }

/* Glow typing */
.glow-typing {
    font-size: 0.85rem;
    color: #60a5fa;
    animation: glow 1.4s infinite ease-in-out;
}

@keyframes glow {
    0% { opacity: .3; text-shadow: 0 0 4px #60a5fa; }
    50% { opacity: 1; text-shadow: 0 0 14px #3b82f6; }
    100% { opacity: .3; text-shadow: 0 0 4px #60a5fa; }
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ================= CONSTANTS =================
MODEL = "llama-3.1-8b-instant"
MAX_TOKENS = 260
MAX_HISTORY = 6

# ================= STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory_on" not in st.session_state:
    st.session_state.memory_on = True

if "last_user_prompt" not in st.session_state:
    st.session_state.last_user_prompt = None

if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = False

# ================= GROQ CLIENT =================
def groq_client():
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ================= SYSTEM PROMPT =================
def system_prompt():
    return (
        "You are DrakFury AI from Nexo.corp. "
        "Fast, calm, intelligent, and precise. "
        "Short answers by default. "
        "Go deep only when asked."
    )

# ================= CHAT =================
def render_chat():
    st.markdown("<div class='drak-chat'>", unsafe_allow_html=True)

    # Welcome message (once)
    if not st.session_state.welcome_shown:
        st.session_state.messages.append({
            "role": "assistant",
            "content": "🐉 **Welcome. I am DrakFury.**<br>Silent. Fast. Intelligent.<br><br>Ask me anything.",
            "time": None
        })
        st.session_state.welcome_shown = True

    # Render messages
    for m in st.session_state.messages:
        role = m["role"]
        label = "You" if role == "user" else "DrakFury"

        meta = ""
        if role == "assistant" and m.get("time") is not None:
            meta = f"""
            <div class="meta">
                <span>{m["time"]} ms</span>
                <span onclick="navigator.clipboard.writeText(`{m['content']}`)">Copy</span>
            </div>
            """

        st.markdown(
            f"""
            <div class="msg-row {role}">
                <div class="msg {role}">
                    <div class="label">{label}</div>
                    {m["content"]}
                    {meta}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    user_input = st.chat_input("Ask DrakFury...")

    if user_input:
        st.session_state.last_user_prompt = user_input
        st.session_state.messages.append({"role": "user", "content": user_input})

        history = st.session_state.messages
        history = history[-MAX_HISTORY:] if st.session_state.memory_on else history[-1:]
        messages = [{"role": "system", "content": system_prompt()}] + history

        typing_box = st.empty()
        typing_box.markdown(
            """
            <div class="msg-row assistant">
                <div class="msg assistant">
                    <div class="label">DrakFury</div>
                    <div class="glow-typing">DrakFury is thinking…</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        start = time.time()

        response = groq_client().chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS
        )

        typing_box.empty()

        reply = response.choices[0].message.content
        elapsed = int((time.time() - start) * 1000)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply, "time": elapsed}
        )

        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("### 🐉 DrakFury Controls")
    st.toggle("Memory ON", key="memory_on")

    if st.button("🔁 Regenerate"):
        if st.session_state.last_user_prompt:
            st.session_state.messages = st.session_state.messages[:-1]
            st.session_state.messages.append(
                {"role": "user", "content": st.session_state.last_user_prompt}
            )
            st.experimental_rerun()

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.session_state.welcome_shown = False
        st.experimental_rerun()

# ================= RUN =================
render_chat()
