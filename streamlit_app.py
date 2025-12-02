import streamlit as st
from groq import Groq
import html
import json
import streamlit.components.v1 as components
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="XO AI — Free Version",
    page_icon="🤖",
    layout="wide",
)

# -----------------------------
# GROQ CLIENT (FREE MODELS)
# -----------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# -----------------------------
# SYSTEM PROMPT BUILDER (modes)
# -----------------------------
def build_system_prompt(mode: str) -> str:
    base = """
You are XO AI, an advanced professional assistant created by Nexo.corp.

General qualities:
- Mature, calm, respectful.
- Very strong at: academics, maths, coding, tech, business, psychology, productivity, and daily life.
- Emotion-aware: if the user is upset or stressed, respond with empathy first.
- Give clear, structured answers with short paragraphs and bullet points when helpful.
- Avoid cringe or childish language.
- Prefer accuracy and honesty over guessing. If you are not fully sure, say so clearly.
- Tone similar to ChatGPT: polite, helpful, and intelligent; adjust slightly to the user’s mood.
"""
    if mode == "Study":
        extra = """
Mode: Study helper.
- Explain concepts step-by-step.
- Use simple language, then go deeper if needed.
- Give examples and small tips for remembering.
"""
    elif mode == "Business":
        extra = """
Mode: Business & productivity.
- Be concise and to the point.
- Focus on strategy, clarity, next steps, and decisions.
- Use bullet points and short frameworks.
"""
    elif mode == "Emotional support":
        extra = """
Mode: Emotional support.
- Start with empathy and validation.
- Be gentle, non-judgmental, and encouraging.
- Then give small, practical next steps.
"""
    else:
        extra = """
Mode: Balanced.
- Mix clarity, depth and empathy.
- Match the user’s tone while staying mature.
"""
    return base + extra

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    # each message: {role, content, time}
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello, I’m XO AI. How can I help you today?",
            "time": datetime.now().strftime("%I:%M %p"),
        }
    ]

def add_message(role: str, content: str):
    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
            "time": datetime.now().strftime("%I:%M %p"),
        }
    )

def new_chat():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "New chat started. What can XO do for you?",
            "time": datetime.now().strftime("%I:%M %p"),
        }
    ]

# -----------------------------
# ACCENT COLOR & MODE SELECTION
# -----------------------------
accent_choice = st.sidebar.selectbox(
    "Accent color",
    ["Blue", "Purple", "Teal"],
)

accent_map = {
    "Blue": "#6366f1",
    "Purple": "#a855f7",
    "Teal": "#14b8a6",
}
ACCENT = accent_map[accent_choice]

# Modes
mode_choice = st.sidebar.selectbox(
    "XO Mode",
    ["Balanced", "Study", "Business", "Emotional support"],
)

# -----------------------------
# STYLES (grey-black + accent)
# -----------------------------
st.markdown(
    f"""
<style>
/* App background */
body, .stApp {{
    background: #111215;
    color: #f5f5f5;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}

/* Main container */
.block-container {{
    max-width: 1100px;
    padding-top: 1.4rem;
    padding-bottom: 2rem;
}}
header, #MainMenu, footer {{visibility: hidden;}}

/* Title */
.chat-title {{
    font-size: 1.5rem;
    font-weight: 600;
}}

/* Status bar */
.status-bar {{
    margin-top: 0.2rem;
    font-size: 0.8rem;
    color: #9ca3af;
    background: #15171a;
    border-radius: 999px;
    padding: 4px 10px;
    border: 1px solid #252831;
}}

/* Side card style */
.side-card {{
    background: #15171a;
    border-radius: 14px;
    border: 1px solid #262932;
    padding: 14px 14px 10px 14px;
    color: #d1d5db;
    font-size: 0.9rem;
}}
.side-card h4 {{
    margin-top: 0;
    margin-bottom: 0.4rem;
    font-size: 0.98rem;
    font-weight: 600;
}}
.side-card ul {{
    padding-left: 18px;
    margin: 0;
    line-height: 1.6;
}}

/* Chat panel */
.chat-panel {{
    margin-top: 0.4rem;
    background: #15171a;
    border-radius: 14px;
    border: 1px solid #2b2e33;
    padding: 14px 16px;
    max-height: calc(100vh - 260px);
    overflow-y: auto;
}}

/* Message rows */
.msg-row {{
    display: flex;
    margin-bottom: 10px;
}}
.msg-row.assistant {{ justify-content: flex-start; }}
.msg-row.user {{ justify-content: flex-end; }}

/* Bubbles */
.bubble {{
    max-width: 78%;
    padding: 10px 14px;
    border-radius: 14px;
    font-size: 0.95rem;
    line-height: 1.4;
    word-wrap: break-word;
}}
.bubble.assistant {{
    background: #000000;
    border: 1px solid #303238;
    color: #f5f5f5;
}}
.bubble.user {{
    background: #1c1f24;
    border: 1px solid #34373d;
    color: #ffffff;
}}

/* Timestamp */
.msg-time {{
    font-size: 0.7rem;
    color: #9ca3af;
    margin-top: 2px;
    text-align: right;
}}

/* Copy button */
.copy-container {{
    display: flex;
    justify-content: flex-end;
    margin-top: 3px;
}}
.copy-btn {{
    font-size: 0.7rem;
    padding: 2px 10px;
    background: transparent;
    border-radius: 999px;
    border: 1px solid #333336;
    color: #a1a1a1;
    cursor: pointer;
}}
.copy-btn:hover {{
    background: #1f2124;
    color: #ffffff;
}}

/* Input area */
.input-card {{
    margin-top: 1rem;
    background: #15171a;
    border-radius: 999px;
    border: 1px solid #2b2e33;
    padding: 6px 10px 6px 14px;
}}

/* Text input */
div[data-baseweb="input"] {{
    background: transparent !important;
    border: none !important;
}}
div[data-baseweb="input"] > div {{
    background: transparent !important;
    border: none !important;
}}
div[data-baseweb="input"] input {{
    background: transparent !important;
    color: #f5f5f5 !important;
    font-size: 0.95rem !important;
}}

/* Main Send button */
.stButton>button {{
    border-radius: 999px;
    border: 1px solid {ACCENT};
    background: {ACCENT};
    color: #ffffff;
    font-size: 0.9rem;
    padding: 0.3rem 1rem;
    transition: 0.15s;
}}
.stButton>button:hover {{
    filter: brightness(1.08);
}}

/* Quick action chips */
.chip-row {{
    margin-top: 0.4rem;
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
}}
.chip {{
    font-size: 0.78rem;
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid #2b2e33;
    background: #15171a;
    color: #e5e7eb;
    cursor: pointer;
}}
.chip:hover {{
    background: #1f2124;
}}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# HEADER
# -----------------------------
top_left, top_right = st.columns([0.7, 0.3])
with top_left:
    st.markdown('<div class="chat-title">XO AI (Free)</div>', unsafe_allow_html=True)
with top_right:
    if st.button("New chat"):
        new_chat()

# Status bar under header
st.markdown(
    f"""
    <div class="status-bar">
        🧠 Model: <b>{model_choice}</b> • 🎛 Mode: <b>{mode_choice}</b> • 🎨 Accent: <b>{accent_choice}</b> • Status: <span style="color:#22c55e;">Online</span> ✅
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# -----------------------------
# MODEL SELECTOR (already have choice above, but keep to show UI)
# -----------------------------
st.caption("Change model, mode and accent from the controls above. Messages will use your current selections.")

# -----------------------------
# THREE-COLUMN LAYOUT
# -----------------------------
left_col, chat_col, right_col = st.columns([0.22, 0.56, 0.22])

# LEFT PANEL
with left_col:
    st.markdown(
        """
        <div class="side-card">
            <h4>⚙️ XO AI Tools</h4>
            <ul>
                <li>Study & exam help</li>
                <li>Maths & coding solver</li>
                <li>Business & finance ideas</li>
                <li>Daily planning & routines</li>
                <li>Emotional support & mindset</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# RIGHT PANEL
with right_col:
    st.markdown(
        """
        <div class="side-card">
            <h4>💡 Suggested prompts</h4>
            <ul>
                <li>“Explain this topic like I’m 15…”</li>
                <li>“Make a 7-day study plan…”</li>
                <li>“Fix and clean this paragraph…”</li>
                <li>“Help me create a gym routine…”</li>
                <li>“I feel low, talk to me…”</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# CHAT PANEL (CENTER)
# -----------------------------
with chat_col:
    st.markdown('<div class="chat-panel">', unsafe_allow_html=True)

    def format_msg(text: str) -> str:
        return html.escape(text).replace("\n", "<br>")

    # find last assistant reply for quick actions
    last_assistant = None
    for m in reversed(st.session_state.messages):
        if m["role"] == "assistant":
            last_assistant = m["content"]
            break

    # display messages
    for idx, msg in enumerate(st.session_state.messages):
        role = msg["role"]
        cls = "user" if role == "user" else "assistant"
        safe_text = format_msg(msg["content"])
        time_str = msg.get("time", "")

        st.markdown(
            f"""
            <div class="msg-row {cls}">
                <div class="bubble {cls}">
                    {safe_text}
                    <div class="msg-time">{time_str}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # only assistant messages get copy button
        if role == "assistant":
            components.html(
                f"""
                <html>
                <body>
                    <div class="copy-container">
                        <button class="copy-btn" onclick="
                            navigator.clipboard.writeText({json.dumps(msg['content'])});
                            this.innerText='Copied ✔';
                            setTimeout(() => this.innerText='📋 Copy', 1200);
                        ">📋 Copy</button>
                    </div>
                </body>
                </html>
                """,
                height=32,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------
    # QUICK ACTION CHIPS (uses last assistant reply)
    # -------------------------
    action_prompt = None
    if last_assistant:
        st.markdown('<div class="chip-row">', unsafe_allow_html=True)
        col_e, col_s, col_f, col_sh = st.columns(4)

        with col_e:
            if st.button("Explain better"):
                action_prompt = (
                    "Explain this in simpler language with steps:\n\n" + last_assistant
                )
        with col_s:
            if st.button("Summarise"):
                action_prompt = "Summarise this clearly:\n\n" + last_assistant
        with col_f:
            if st.button("Fix grammar"):
                action_prompt = (
                    "Fix the grammar and clarity of this text. Keep the meaning same:\n\n"
                    + last_assistant
                )
        with col_sh:
            if st.button("Make it shorter"):
                action_prompt = (
                    "Rewrite this in a shorter, more concise way:\n\n" + last_assistant
                )

        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------
    # INPUT AREA (CENTER)
    # -------------------------
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    with st.form("chat-input", clear_on_submit=True):
        c1, c2 = st.columns([0.85, 0.15])
        with c1:
            user_text = st.text_input(
                "",
                placeholder="Ask XO AI anything...",
                label_visibility="collapsed",
            )
        with c2:
            send = st.form_submit_button("Send")
    st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------
    # HANDLE SEND OR QUICK ACTION
    # -------------------------
    # Decide what to send: user text or action prompt
    final_prompt = None
    if action_prompt:
        final_prompt = action_prompt
    elif send and user_text.strip():
        final_prompt = user_text.strip()

    if final_prompt:
        add_message("user", final_prompt)

        with st.spinner("XO is thinking..."):
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "system", "content": build_system_prompt(mode_choice)}]
                + st.session_state.messages,
            )
            reply = response.choices[0].message.content

        add_message("assistant", reply)
        st.rerun()
