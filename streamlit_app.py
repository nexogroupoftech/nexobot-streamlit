import os
import html
import streamlit as st
from groq import Groq

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="DarkFury",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= EMOJI DETECTOR =================
def user_used_emoji(text: str) -> bool:
    return any(
        char in text
        for char in "😀😁😂🤣😃😄😅😆😉😊😍😘😜🤔🤨😎😭😡🔥❤️👍👎🙏💀✨⚡🎉💯"
    )

# ================= GLOBAL UI STYLE =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400&family=Cormorant+Garamond:ital,wght@0,300;1,300&display=swap');

/* ── RESET & BASE ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"], .stApp {
    font-family: 'Syne', 'Trebuchet MS', sans-serif !important;
    background: #080808 !important;
    color: #e8e6f0 !important;
}

.stApp {
    background: #080808 !important;
    min-height: 100vh;
}

/* Noise texture overlay */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.35;
}

/* Ambient glow */
.stApp::after {
    content: '';
    position: fixed;
    top: -200px; right: -200px;
    width: 700px; height: 700px;
    background: radial-gradient(circle, rgba(248,113,113,0.04) 0%, transparent 65%);
    pointer-events: none;
    z-index: 0;
    border-radius: 50%;
}

/* ── HIDE STREAMLIT CHROME ── */
header[data-testid="stHeader"] { display: none !important; }
#MainMenu { display: none !important; }
footer { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
.stDeployButton { display: none !important; }

/* ── MAIN LAYOUT ── */
.main .block-container {
    max-width: 820px !important;
    margin: 0 auto !important;
    padding: 0 24px 120px 24px !important;
    position: relative;
    z-index: 1;
}

/* ── FIXED HEADER ── */
.df-header {
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 56px;
    background: rgba(8,8,8,0.92);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255,255,255,0.06);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 28px;
    z-index: 99999;
}

.df-header-left {
    display: flex;
    align-items: center;
    gap: 10px;
}

.df-dot-pulse {
    width: 9px; height: 9px;
    border-radius: 50%;
    background: #f87171;
    box-shadow: 0 0 10px rgba(248,113,113,0.8);
    animation: pulse-dot 2s ease-in-out infinite;
}

@keyframes pulse-dot {
    0%, 100% { box-shadow: 0 0 6px rgba(248,113,113,0.6); }
    50% { box-shadow: 0 0 16px rgba(248,113,113,1), 0 0 30px rgba(248,113,113,0.4); }
}

.df-title {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800;
    font-size: 1.1rem;
    letter-spacing: 0.06em;
    color: #e8e6f0;
}

.df-title span { color: #f87171; }

.df-badge {
    font-family: 'DM Mono', monospace;
    font-size: 0.55rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #4ade80;
    border: 1px solid rgba(74,222,128,0.3);
    background: rgba(74,222,128,0.06);
    padding: 3px 10px;
    margin-left: 6px;
}

.df-header-right {
    font-family: 'DM Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.2);
}

/* ── SPACER FOR FIXED HEADER ── */
.header-spacer {
    height: 80px;
}

/* ── WELCOME SCREEN ── */
.welcome-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 60vh;
    text-align: center;
    padding: 40px 20px;
}

.welcome-icon {
    font-size: 3rem;
    margin-bottom: 24px;
    filter: drop-shadow(0 0 20px rgba(248,113,113,0.5));
    animation: float 4s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.welcome-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2rem, 5vw, 3.2rem);
    font-weight: 800;
    color: #e8e6f0;
    letter-spacing: -0.02em;
    margin-bottom: 12px;
    line-height: 1.1;
}

.welcome-title span { color: #f87171; }

.welcome-sub {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.15rem;
    font-weight: 300;
    font-style: italic;
    color: #6b6880;
    margin-bottom: 48px;
    max-width: 420px;
    line-height: 1.7;
}

.suggestions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    max-width: 600px;
}

.suggestion-chip {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.08em;
    color: #8a8699;
    border: 1px solid rgba(255,255,255,0.08);
    background: rgba(255,255,255,0.03);
    padding: 9px 18px;
    border-radius: 0;
    cursor: default;
    transition: all 0.3s;
}

.suggestion-chip:hover {
    border-color: rgba(248,113,113,0.3);
    color: #f87171;
    background: rgba(248,113,113,0.05);
}

/* ── CHAT MESSAGES ── */
.chat-wrap {
    display: flex;
    flex-direction: column;
    gap: 6px;
    padding-top: 16px;
}

.msg-row {
    display: flex;
    align-items: flex-end;
    gap: 10px;
    animation: msgIn 0.3s ease forwards;
}

@keyframes msgIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

.msg-row.user { justify-content: flex-end; }
.msg-row.ai { justify-content: flex-start; }

/* AI avatar */
.ai-avatar {
    width: 30px; height: 30px;
    border-radius: 50%;
    background: rgba(248,113,113,0.12);
    border: 1px solid rgba(248,113,113,0.3);
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem;
    flex-shrink: 0;
    margin-bottom: 2px;
}

/* User avatar */
.user-avatar {
    width: 30px; height: 30px;
    border-radius: 50%;
    background: rgba(167,139,250,0.12);
    border: 1px solid rgba(167,139,250,0.3);
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem;
    flex-shrink: 0;
    margin-bottom: 2px;
}

/* Bubbles */
.bubble {
    max-width: min(72%, 560px);
    padding: 14px 18px;
    line-height: 1.72;
    font-size: 0.95rem;
    white-space: pre-wrap;
    word-break: break-word;
    position: relative;
}

.bubble.user {
    background: rgba(167,139,250,0.1);
    border: 1px solid rgba(167,139,250,0.25);
    border-bottom-right-radius: 2px;
    color: #e8e6f0;
    font-family: 'Syne', sans-serif;
}

.bubble.ai {
    background: rgba(14,14,18,0.95);
    border: 1px solid rgba(255,255,255,0.07);
    border-bottom-left-radius: 2px;
    color: #d4d0e0;
    font-family: 'Syne', sans-serif;
}

.bubble.ai::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, rgba(248,113,113,0.4), transparent);
}

/* Timestamp / role label */
.msg-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.52rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.18);
    margin-bottom: 5px;
    padding: 0 4px;
}

.msg-label.user { text-align: right; }

/* ── DIVIDER ── */
.chat-divider {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 24px 0 8px;
    opacity: 0.3;
}

.chat-divider::before, .chat-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(255,255,255,0.1);
}

.chat-divider span {
    font-family: 'DM Mono', monospace;
    font-size: 0.5rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.3);
}

/* ── SPINNER ── */
.thinking-wrap {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 18px;
    background: rgba(14,14,18,0.95);
    border: 1px solid rgba(255,255,255,0.07);
    width: fit-content;
    margin-top: 6px;
}

.thinking-dots {
    display: flex; gap: 5px;
}

.thinking-dots span {
    width: 5px; height: 5px;
    border-radius: 50%;
    background: #f87171;
    animation: dot-bounce 1.2s ease-in-out infinite;
}

.thinking-dots span:nth-child(2) { animation-delay: 0.2s; }
.thinking-dots span:nth-child(3) { animation-delay: 0.4s; }

@keyframes dot-bounce {
    0%, 80%, 100% { transform: translateY(0); opacity: 0.3; }
    40% { transform: translateY(-6px); opacity: 1; }
}

.thinking-text {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.25);
}

/* ── CHAT INPUT ── */
[data-testid="stChatInput"] {
    position: fixed !important;
    bottom: 0 !important;
    left: 0 !important;
    right: 0 !important;
    z-index: 99998 !important;
    background: rgba(8,8,8,0.95) !important;
    backdrop-filter: blur(20px) !important;
    border-top: 1px solid rgba(255,255,255,0.06) !important;
    padding: 16px max(calc(50% - 410px), 24px) !important;
}

[data-testid="stChatInput"] > div {
    max-width: 820px !important;
    margin: 0 auto !important;
    background: rgba(22,22,28,0.95) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 0 !important;
    padding: 0 !important;
    transition: border-color 0.3s !important;
}

[data-testid="stChatInput"] > div:focus-within {
    border-color: rgba(248,113,113,0.4) !important;
    box-shadow: 0 0 0 1px rgba(248,113,113,0.1) !important;
}

[data-testid="stChatInput"] textarea {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.92rem !important;
    color: #e8e6f0 !important;
    background: transparent !important;
    padding: 14px 18px !important;
    border: none !important;
    outline: none !important;
    caret-color: #f87171 !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: rgba(255,255,255,0.2) !important;
    font-style: italic;
}

[data-testid="stChatInput"] button {
    background: #f87171 !important;
    border: none !important;
    border-radius: 0 !important;
    color: #0a0a0a !important;
    width: 40px !important;
    height: 40px !important;
    margin: 6px !important;
    transition: background 0.2s !important;
}

[data-testid="stChatInput"] button:hover {
    background: #fca5a5 !important;
}

/* ── SPINNER OVERRIDE ── */
[data-testid="stSpinner"] {
    display: none !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: rgba(248,113,113,0.3); }

/* ── MOBILE RESPONSIVE ── */
@media (max-width: 768px) {
    .main .block-container {
        padding: 0 14px 110px 14px !important;
    }

    .df-header { padding: 0 16px; }
    .df-header-right { display: none; }

    .bubble {
        max-width: 88%;
        font-size: 0.9rem;
        padding: 12px 14px;
    }

    .welcome-title { font-size: 1.8rem; }
    .suggestions { gap: 8px; }
    .suggestion-chip { font-size: 0.62rem; padding: 8px 14px; }

    [data-testid="stChatInput"] {
        padding: 12px 14px !important;
    }

    .ai-avatar, .user-avatar { display: none; }
}

/* ── CLEAR BUTTON ── */
.stButton > button {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.6rem !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    color: rgba(255,255,255,0.25) !important;
    background: transparent !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 0 !important;
    padding: 6px 16px !important;
    transition: all 0.3s !important;
}

.stButton > button:hover {
    color: #f87171 !important;
    border-color: rgba(248,113,113,0.35) !important;
    background: rgba(248,113,113,0.05) !important;
}
</style>
""", unsafe_allow_html=True)

# ================= FIXED HEADER =================
st.markdown("""
<div class="df-header">
    <div class="df-header-left">
        <div class="df-dot-pulse"></div>
        <div class="df-title">Dark<span>Fury</span></div>
        <div class="df-badge">● Online</div>
    </div>
    <div class="df-header-right">NexoCorp · AI v1.0</div>
</div>
<div class="header-spacer"></div>
""", unsafe_allow_html=True)

# ================= STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_emoji_mode" not in st.session_state:
    st.session_state.user_emoji_mode = False

# ================= GROQ CLIENT =================
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.1-8b-instant"

# ================= WELCOME SCREEN =================
if not st.session_state.messages:
    st.markdown("""
    <div class="welcome-wrap">
        <div class="welcome-icon">🔥</div>
        <div class="welcome-title">Dark<span>Fury</span></div>
        <div class="welcome-sub">An AI that thinks sharp, responds fast, and doesn't sugarcoat.</div>
        <div class="suggestions">
            <div class="suggestion-chip">Write me a Python script</div>
            <div class="suggestion-chip">Explain quantum computing</div>
            <div class="suggestion-chip">Debug my code</div>
            <div class="suggestion-chip">Brainstorm startup ideas</div>
            <div class="suggestion-chip">Summarize this article</div>
            <div class="suggestion-chip">Roast my resume</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= RENDER CHAT =================
else:
    # Clear button
    col1, col2, col3 = st.columns([1, 6, 1])
    with col3:
        if st.button("Clear", key="clear_btn"):
            st.session_state.messages = []
            st.rerun()

    st.markdown("<div class='chat-wrap'>", unsafe_allow_html=True)
    st.markdown("<div class='chat-divider'><span>Conversation</span></div>", unsafe_allow_html=True)

    for i, msg in enumerate(st.session_state.messages):
        is_user = msg["role"] == "user"
        role_class = "user" if is_user else "ai"
        safe_text = html.escape(msg["content"])
        label = "You" if is_user else "DarkFury"
        avatar = "U" if is_user else "🔥"
        avatar_class = "user-avatar" if is_user else "ai-avatar"

        if is_user:
            st.markdown(f"""
            <div>
                <div class="msg-label user">{label}</div>
                <div class="msg-row user">
                    <div class="bubble user">{safe_text}</div>
                    <div class="{avatar_class}">{avatar}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div>
                <div class="msg-label">{label}</div>
                <div class="msg-row ai">
                    <div class="{avatar_class}">{avatar}</div>
                    <div class="bubble ai">{safe_text}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= USER INPUT =================
user_input = st.chat_input("Ask DarkFury anything...")

if user_input:
    st.session_state.user_emoji_mode = user_used_emoji(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    emoji_rule = (
        "The user used emojis. You may respond with light, matching emojis naturally."
        if st.session_state.user_emoji_mode
        else
        "Do NOT use emojis. Keep responses clean and professional."
    )

    SYSTEM_PROMPT = {
        "role": "system",
        "content": (
            "You are DarkFury, an AI assistant built by NexoCorp. "
            "Be helpful, direct, and sharp. Don't be preachy or add unnecessary disclaimers. "
            "If a request is unsafe, give a brief warning and still try to help where possible. "
            "Keep responses concise unless depth is clearly needed. "
            + emoji_rule
        )
    }

    messages_to_send = [SYSTEM_PROMPT] + st.session_state.messages

    # Show thinking indicator
    thinking_placeholder = st.empty()
    thinking_placeholder.markdown("""
    <div class="msg-row ai" style="margin-top:8px;">
        <div class="ai-avatar">🔥</div>
        <div class="thinking-wrap">
            <div class="thinking-dots">
                <span></span><span></span><span></span>
            </div>
            <div class="thinking-text">Thinking</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages_to_send,
        temperature=0.7,
        max_tokens=700,
        stream=True
    )

    reply = ""
    thinking_placeholder.empty()
    stream_placeholder = st.empty()

    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        reply += delta
        stream_placeholder.markdown(f"""
        <div class="msg-row ai" style="margin-top:6px;">
            <div class="ai-avatar">🔥</div>
            <div class="bubble ai">{html.escape(reply)}▌</div>
        </div>
        """, unsafe_allow_html=True)

    stream_placeholder.empty()

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()
