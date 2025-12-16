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

/* Chat wrapper */
.drak-chat { background: transparent; }

/* Message rows */
.msg-row { display: flex; margin-bottom: 0.7rem; }
.msg-row.user { justify-content: flex-end; }
.msg-row.assistant { justify-content: flex-start; }

/* Message bubbles */
.msg {
    max-width: 78%;
    padding: 0.75rem 0.95rem;
    border-radius: 16px;
    font-size: 0.92rem;
    line-height: 1.55;
}

/* User */
.msg.user {
    background: linear-gradient(135deg, #1e40af, #2563eb);
    color: #ffffff;
    box-shadow: 0 0 12px rgba(37,99,235,0.35);
}

/* Assistant */
.msg.assistant {
    background: rgba(10,15,31,0.85);
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
    margin-top: 0.3rem;
    display: flex;
    gap: 0.8rem;
}

/* Buttons */
.meta span {
    cursor: pointer;
}
.meta span:hover { opacity: 1; }

/* Glow typing animation */
.glow-typing {
    font-size: 0.85rem;
    color: #60a5fa;
    animation: glow 1.4s infinite ease-in-out;
}

@keyframes glow {
    0% { opacity: .3; text-shadow: 0 0 4px #60a5fa; }
    50% { opacity: 1; text-shadow: 0 0 12px #3b82f6; }
    100% { opacity: .3; text-shadow: 0 0 4px #60a5fa; }
}

/* Auto-scroll anchor */
#scroll-anchor { height: 1px; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ================= CONSTANTS =================
FAST_MODEL = "llama-3.1-8b-instant"
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

# ================= GROQ =================
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

    # Welcome message (ONCE)
    if not st.session_state.welcome_shown:
        st.session_state.messages.append({
            "role": "assistant",
            "content": "🐉 **Welcome. I am DrakFury.**\n\nSilent. Fast. Intelligent.\nAsk me anything.",
            "time": None
        })
        st.session_state.welcome_shown = True

    # Render history
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

        reply_box = st.empty()
        reply = ""
        start = time.time()

        stream = groq_client().chat.completions.create(
            model=FAST_MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            stream=True
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                reply += chunk.choices[0].delta.content
                reply_box.markdown(
                    f"""
                    <div class="msg-row assistant">
                        <div class="msg assistant">
                            <div class="label">DrakFury</div>
                            {reply}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        typing_box.empty()
        elapsed = int((time.time() - start) * 1000)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply, "time": elapsed}
        )

    st.markdown('<div id="scroll-anchor"></div>', unsafe_allow_html=True)
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

# ================= RUN =================
render_chat()
