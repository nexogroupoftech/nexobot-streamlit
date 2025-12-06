import os
from typing import List, Dict

import streamlit as st
from groq import Groq


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="XO AI — Nexo.corp",
    page_icon="🤖",
    layout="wide",
)


# ---------- GLOBAL CSS (CHATGPT-LIKE, NO FACES) ----------
CUSTOM_CSS = """
<style>
    .stApp {
        background: radial-gradient(circle at top left, #151b2b 0, #050816 40%, #02010a 100%) !important;
        color: #f9fafb !important;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 1200px !important;
    }

    /* HERO */
    .xo-hero {
        padding: 1.5rem 1.25rem 1.25rem 1.25rem;
        border-radius: 1.5rem;
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.35), rgba(15, 23, 42, 0.95));
        border: 1px solid rgba(148, 163, 184, 0.35);
        box-shadow: 0 26px 80px rgba(15, 23, 42, 0.9);
        animation: fadeUp 0.7s ease-out;
        position: relative;
        overflow: hidden;
    }

    .xo-hero::before {
        content: "";
        position: absolute;
        inset: -40%;
        background: radial-gradient(circle at 0 0, rgba(129, 140, 248, 0.18), transparent 55%);
        opacity: 0.9;
        pointer-events: none;
    }

    .xo-hero-title {
        font-size: 2.0rem;
        font-weight: 750;
        letter-spacing: 0.04em;
        margin-bottom: 0.35rem;
    }

    .xo-hero-subtitle {
        font-size: 0.95rem;
        color: #e5e7eb;
        opacity: 0.9;
        margin-bottom: 0.65rem;
    }

    .xo-status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        font-size: 0.75rem;
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid rgba(148, 163, 184, 0.7);
        color: #e5e7eb;
        backdrop-filter: blur(12px);
    }

    .xo-status-dot {
        width: 8px;
        height: 8px;
        border-radius: 999px;
        background: #22c55e;
        box-shadow: 0 0 0 4px rgba(34, 197, 94, 0.30);
    }

    /* CHAT WRAPPER (NO STREAMLIT AVATARS, PURE CUSTOM) */
    .xo-chat-wrapper {
        padding: 0.75rem 0.9rem 0.9rem 0.9rem;
        border-radius: 1.25rem;
        background: rgba(15, 23, 42, 0.96);
        border: 1px solid rgba(30, 64, 175, 0.7);
        box-shadow: 0 18px 55px rgba(15, 23, 42, 0.9);
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        height: 65vh;
        max-height: 65vh;
    }

    .xo-chat-scroll {
        flex: 1 1 auto;
        overflow-y: auto;
        padding-right: 0.25rem;
    }

    .xo-msg-row {
        display: flex;
        margin-bottom: 0.35rem;
    }

    .xo-msg-row.user {
        justify-content: flex-end;
    }

    .xo-msg-row.assistant {
        justify-content: flex-start;
    }

    .xo-msg-bubble {
        max-width: 80%;
        padding: 0.55rem 0.75rem;
        border-radius: 0.9rem;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    .xo-msg-bubble.user {
        background: radial-gradient(circle at top left, rgba(59, 130, 246, 0.5), rgba(15, 23, 42, 0.95));
        border: 1px solid rgba(59, 130, 246, 0.9);
    }

    .xo-msg-bubble.assistant {
        background: rgba(15, 23, 42, 0.98);
        border: 1px solid rgba(75, 85, 99, 0.9);
    }

    .xo-msg-label {
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #9ca3af;
        margin-bottom: 0.15rem;
    }

    /* INPUT BAR (CHATGPT-LIKE) */
    .xo-input-bar {
        margin-top: 0.55rem;
        border-radius: 999px;
        border: 1px solid rgba(55, 65, 81, 0.9);
        background: rgba(15, 23, 42, 0.98);
        padding: 0.3rem 0.4rem 0.35rem 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
        box-shadow: 0 18px 45px rgba(15, 23, 42, 1);
    }

    .xo-input-hint {
        font-size: 0.7rem;
        color: #6b7280;
        margin-top: 0.25rem;
    }

    /* QUICK MODES CARD */
    .xo-modes-card {
        padding: 0.8rem 0.9rem 0.9rem 0.9rem;
        border-radius: 1.25rem;
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid rgba(55, 65, 81, 0.85);
        box-shadow: 0 18px 55px rgba(15, 23, 42, 0.9);
        animation: fadeUp 0.8s ease-out;
    }

    .xo-modes-title {
        font-size: 0.9rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #9ca3af;
        margin-bottom: 0.6rem;
    }

    .xo-identity-box {
        margin-top: 0.75rem;
        padding: 0.65rem 0.75rem;
        border-radius: 0.9rem;
        background: rgba(15, 23, 42, 0.95);
        border: 1px dashed rgba(75, 85, 99, 0.9);
        font-size: 0.75rem;
        line-height: 1.4;
        color: #d1d5db;
    }

    .xo-identity-title {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 0.4rem;
        color: #9ca3af;
    }

    .xo-footer {
        margin-top: 1.2rem;
        font-size: 0.75rem;
        color: #6b7280;
        text-align: center;
        opacity: 0.9;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------- MODES & GROQ MODEL MAPPING ----------

MODES = [
    "Study Helper",
    "Idea Generator",
    "Planner",
    "Friendly Chat",
]

# UI labels -> real Groq models (current free/standard ones)
MODEL_ID_MAP = {
    "llama3-8b-8192": "llama-3.1-8b-instant",
    "llama3-70b-8192": "llama-3.3-70b-versatile",
}


def init_session_state() -> None:
    if "messages" not in st.session_state:
        # each msg: {"role": "user"|"assistant", "content": str}
        st.session_state.messages: List[Dict[str, str]] = []
    if "selected_mode" not in st.session_state:
        st.session_state.selected_mode = "Friendly Chat"


def get_mode_instructions(mode: str) -> str:
    base_rules = (
        "You are XO AI, the official assistant of Nexo.corp. "
        "Your tone is calm, clear, and respectful. "
        "You simplify explanations without losing accuracy. "
        "For study questions, you explain step-by-step. "
        "You must not give trading, stock market, crypto, or other financial advice. "
        "You must refuse harmful, unsafe, or adult content. "
        "Keep answers concise unless the user explicitly asks for a long or very detailed answer. "
    )

    if mode == "Study Helper":
        mode_text = (
            "Act as a friendly Study Helper. "
            "Break problems into clear steps and show reasoning simply. "
            "Encourage the student but do not do full homework or exam papers for them."
        )
    elif mode == "Idea Generator":
        mode_text = (
            "Act as a creative Idea Generator. "
            "Brainstorm ideas for content, projects, startups, and goals. "
            "Be practical and realistic, with examples."
        )
    elif mode == "Planner":
        mode_text = (
            "Act as a planning assistant. "
            "Design realistic study plans, routines, and simple roadmaps."
        )
    else:  # Friendly Chat
        mode_text = (
            "Act as a calm and positive friend. "
            "Talk about life, school, mindset, and self-improvement without being dramatic."
        )

    return base_rules + " " + mode_text


def build_messages(user_input: str) -> List[Dict[str, str]]:
    system_prompt = get_mode_instructions(st.session_state.selected_mode)

    msgs: List[Dict[str, str]] = [
        {"role": "system", "content": system_prompt},
    ]

    for m in st.session_state.messages:
        msgs.append({"role": m["role"], "content": m["content"]})

    msgs.append({"role": "user", "content": user_input})
    return msgs


def get_groq_client() -> Groq:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not set. Set it before using XO AI.")

    # pattern you requested
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    return client


def call_groq(messages: List[Dict[str, str]], ui_model: str) -> str:
    client = get_groq_client()

    groq_model_id = MODEL_ID_MAP.get(ui_model, ui_model)

    completion = client.chat.completions.create(
        model=groq_model_id,
        messages=messages,
        temperature=0.4,
        max_tokens=1024,
    )

    return completion.choices[0].message.content.strip()


# ---------- UI COMPONENTS ----------


def render_hero() -> None:
    st.markdown(
        """
        <div class="xo-hero">
            <div style="position: relative; z-index: 1;">
                <div class="xo-hero-title">XO AI — Nexo Assistant</div>
                <div class="xo-hero-subtitle">
                    Built by Nexo.corp for students, creators, and young professionals.
                </div>
                <div class="xo-status-pill">
                    <span class="xo-status-dot"></span>
                    <span>online</span>
                    <span style="opacity:0.35;">•</span>
                    <span class="xo-status-powered">powered by Groq</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_modes_sidebar() -> None:
    st.markdown("<div class='xo-modes-card'>", unsafe_allow_html=True)
    st.markdown("<div class='xo-modes-title'>Quick modes</div>", unsafe_allow_html=True)

    selected = st.radio(
        "",
        MODES,
        index=MODES.index(st.session_state.selected_mode),
        label_visibility="collapsed",
    )
    st.session_state.selected_mode = selected

    descriptions = {
        "Study Helper": "Break down concepts and questions step-by-step.",
        "Idea Generator": "Brainstorm content, project, and business ideas.",
        "Planner": "Design routines, timetables, and simple roadmaps.",
        "Friendly Chat": "Normal conversation, mindset, and life chat.",
    }

    st.markdown(
        f"<div style='font-size:0.8rem;color:#9ca3af;margin-bottom:0.4rem;'>{descriptions.get(selected, '')}</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="xo-identity-box">
            <div class="xo-identity-title">XO AI identity</div>
            <ul style="margin:0; padding-left:1.1rem;">
                <li>Calm, clear, and respectful tone.</li>
                <li>Simplifies explanations without losing accuracy.</li>
                <li>Step-by-step support for study questions.</li>
                <li>No trading or financial advice, ever.</li>
                <li>Refuses harmful or unsafe requests.</li>
                <li>Keeps answers short unless you ask for long.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


def render_chat_area(selected_model: str) -> None:
    # Wrapper div for chat
    st.markdown("<div class='xo-chat-wrapper'>", unsafe_allow_html=True)

    # Scroll area with custom HTML bubbles (NO st.chat_message, so no faces)
    chat_html_parts: List[str] = ["<div class='xo-chat-scroll'>"]

    for m in st.session_state.messages:
        role = m["role"]
        content = m["content"]
        cls = "user" if role == "user" else "assistant"
        label = "You" if role == "user" else "XO AI"
        # Escape basic HTML chars
        safe_content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        chat_html_parts.append(
            f"<div class='xo-msg-row {cls}'>"
            f"  <div class='xo-msg-bubble {cls}'>"
            f"    <div class='xo-msg-label'>{label}</div>"
            f"    <div>{safe_content}</div>"
            f"  </div>"
            f"</div>"
        )

    chat_html_parts.append("</div>")  # close xo-chat-scroll

    st.markdown("\n".join(chat_html_parts), unsafe_allow_html=True)

    # Input bar at bottom (we still use st.chat_input for good UX, but it does NOT create faces)
    user_input = st.chat_input("Ask XO AI anything…")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("XO AI is thinking…"):
            try:
                msgs = build_messages(user_input)
                assistant_reply = call_groq(msgs, selected_model)
            except RuntimeError as e:
                st.error(str(e))
                st.markdown("</div>", unsafe_allow_html=True)  # close wrapper
                return
            except Exception as e:
                st.error("XO AI hit a limit. Please try again in a moment.")
                st.caption(f"Debug info: {e}")
                st.markdown("</div>", unsafe_allow_html=True)
                return

        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

        # Re-render after new messages so bubbles show immediately
        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)  # close xo-chat-wrapper


# ---------- MAIN ----------


def main() -> None:
    init_session_state()

    render_hero()
    st.markdown("\n", unsafe_allow_html=True)

    with st.expander("Model settings", expanded=False):
        selected_model = st.radio(
            "Choose Groq model",
            options=["llama3-8b-8192", "llama3-70b-8192"],
            index=1,
            help="These are Groq Llama models used by XO AI.",
            horizontal=True,
        )

    left_col, right_col = st.columns([1.9, 1.1], gap="large")

    with left_col:
        render_chat_area(selected_model)

    with right_col:
        render_modes_sidebar()

    st.markdown(
        """
        <div class="xo-footer">
            <span>Powered by Groq • XO AI is built by Nexo.corp</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
