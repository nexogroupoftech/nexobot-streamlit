import os
import time
import streamlit as st
from groq import Groq

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="XO AI — Nexo.corp",
    page_icon="🤖",
    layout="wide"
)

# ================= CSS =================
CUSTOM_CSS = """
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #050816);
    color: #e5e7eb;
}

header[data-testid="stHeader"] { background: transparent; }

.block-container {
    max-width: 1100px;
    padding-top: 1.2rem;
}

/* Chat */
.xo-chat-wrapper { background: transparent; }

/* Messages */
.xo-msg-row { display: flex; margin-bottom: 0.6rem; }
.xo-msg-row.user { justify-content: flex-end; }
.xo-msg-row.assistant { justify-content: flex-start; }

.xo-msg-bubble {
    max-width: 78%;
    padding: 0.7rem 0.9rem;
    border-radius: 14px;
    font-size: 0.9rem;
    line-height: 1.55;
}

.xo-msg-bubble.user {
    background: linear-gradient(135deg, #2563eb, #1e40af);
    color: #fff;
}

.xo-msg-bubble.assistant {
    background: #111827;
    border: 1px solid #1f2937;
}

.xo-msg-label {
    font-size: 0.65rem;
    letter-spacing: 0.08em;
    opacity: 0.7;
    margin-bottom: 0.2rem;
}

/* Meta bar */
.xo-meta {
    font-size: 0.65rem;
    opacity: 0.6;
    margin-top: 0.25rem;
    display: flex;
    gap: 0.6rem;
}

/* Buttons */
.xo-btn {
    cursor: pointer;
    font-size: 0.65rem;
    opacity: 0.75;
}
.xo-btn:hover { opacity: 1; }

/* Auto scroll */
#scroll-anchor {
    height: 1px;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ================= CONSTANTS =================
FAST_MODEL = "llama-3.1-8b-instant"
MAX_TOKENS = 250
MAX_HISTORY = 6

# ================= STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory_on" not in st.session_state:
    st.session_state.memory_on = True

if "last_user_prompt" not in st.session_state:
    st.session_state.last_user_prompt = None

# ================= GROQ =================
def groq_client():
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ================= PROMPT =================
def system_prompt():
    return (
        "You are XO AI from Nexo.corp. "
        "Calm, helpful, clear. "
        "Short answers unless user asks deep."
    )

# ================= CHAT =================
def render_chat():
    st.markdown("<div class='xo-chat-wrapper'>", unsafe_allow_html=True)

    # Render history
    for i, m in enumerate(st.session_state.messages):
        role = m["role"]
        label = "You" if role == "user" else "XO AI"

        meta = ""
        if role == "assistant" and "time" in m:
            meta = f"""
            <div class="xo-meta">
                <span>{m["time"]} ms</span>
                <span class="xo-btn" onclick="navigator.clipboard.writeText(`{m['content']}`)">Copy</span>
            </div>
            """

        st.markdown(
            f"""
            <div class="xo-msg-row {role}">
                <div class="xo-msg-bubble {role}">
                    <div class="xo-msg-label">{label}</div>
                    {m["content"]}
                    {meta}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    user_input = st.chat_input("Ask XO AI...")

    if user_input:
        st.session_state.last_user_prompt = user_input
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        history = st.session_state.messages
        if st.session_state.memory_on:
            history = history[-MAX_HISTORY:]
        else:
            history = history[-1:]

        messages = [{"role": "system", "content": system_prompt()}] + history

        assistant_box = st.empty()
        reply = ""
        start_time = time.time()

        stream = groq_client().chat.completions.create(
            model=FAST_MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            stream=True,
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                reply += chunk.choices[0].delta.content
                assistant_box.markdown(
                    f"""
                    <div class="xo-msg-row assistant">
                        <div class="xo-msg-bubble assistant">
                            <div class="xo-msg-label">XO AI</div>
                            {reply}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        elapsed = int((time.time() - start_time) * 1000)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply, "time": elapsed}
        )

    st.markdown('<div id="scroll-anchor"></div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("### ⚙️ XO AI Controls")
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

# ================= RUN =================
render_chat()
