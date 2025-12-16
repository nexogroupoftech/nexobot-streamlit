import os
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
    background: radial-gradient(circle at top left, #151b2b 0, #050816 40%, #02010a 100%);
    color: #f9fafb;
}

header[data-testid="stHeader"] { background: transparent; }

.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
}

/* Chat wrapper */
.xo-chat-wrapper {
    background: transparent;
    border: none;
    box-shadow: none;
}

/* Message layout */
.xo-msg-row { display: flex; margin-bottom: 0.5rem; }
.xo-msg-row.user { justify-content: flex-end; }
.xo-msg-row.assistant { justify-content: flex-start; }

.xo-msg-bubble {
    max-width: 80%;
    padding: 0.65rem 0.85rem;
    border-radius: 0.9rem;
    font-size: 0.9rem;
    line-height: 1.5;
}

.xo-msg-bubble.user {
    background: rgba(59,130,246,0.35);
    border: 1px solid rgba(59,130,246,0.8);
}

.xo-msg-bubble.assistant {
    background: rgba(31,41,55,0.9);
    border: 1px solid rgba(75,85,99,0.8);
}

.xo-msg-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #9ca3af;
    margin-bottom: 0.15rem;
}

/* Typing animation */
.xo-typing {
    font-size: 0.85rem;
    color: #9ca3af;
    animation: blink 1.4s infinite both;
}

@keyframes blink {
    0% { opacity: .2; }
    20% { opacity: 1; }
    100% { opacity: .2; }
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ================= CONSTANTS =================
FAST_MODEL = "llama-3.1-8b-instant"
MAX_HISTORY = 6
MAX_TOKENS = 250

# ================= STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ================= GROQ CLIENT =================
def groq_client():
    return Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ================= SYSTEM PROMPT =================
def system_prompt():
    return (
        "You are XO AI from Nexo.corp. "
        "Be calm, simple, respectful, and clear. "
        "Give short helpful answers. "
        "Explain step-by-step only when needed."
    )

# ================= CHAT UI =================
def render_chat():
    st.markdown("<div class='xo-chat-wrapper'>", unsafe_allow_html=True)

    # Show chat history
    for m in st.session_state.messages:
        role = m["role"]
        label = "You" if role == "user" else "XO AI"
        st.markdown(
            f"""
            <div class='xo-msg-row {role}'>
                <div class='xo-msg-bubble {role}'>
                    <div class='xo-msg-label'>{label}</div>
                    {m["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    user_input = st.chat_input("Ask XO AI...")

    if user_input:
        # Save user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        messages = (
            [{"role": "system", "content": system_prompt()}]
            + st.session_state.messages[-MAX_HISTORY:]
        )

        # Typing animation
        typing_box = st.empty()
        typing_box.markdown(
            """
            <div class='xo-msg-row assistant'>
                <div class='xo-msg-bubble assistant'>
                    <div class='xo-msg-label'>XO AI</div>
                    <div class='xo-typing'>Typing...</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        reply_box = st.empty()
        reply = ""

        try:
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
                        <div class='xo-msg-row assistant'>
                            <div class='xo-msg-bubble assistant'>
                                <div class='xo-msg-label'>XO AI</div>
                                {reply}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            typing_box.empty()

            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )

        except Exception as e:
            typing_box.empty()
            st.error("XO AI is busy. Please try again.")
            st.caption(str(e))

    st.markdown("</div>", unsafe_allow_html=True)

# ================= MAIN =================
def main():
    with st.sidebar:
        st.markdown("### ⚙️ XO AI")
        if st.button("Clear chat"):
            st.session_state.messages = []

    render_chat()

main()
