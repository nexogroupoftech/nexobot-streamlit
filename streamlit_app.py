import streamlit as st
from groq import Groq

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------
st.set_page_config(
    page_title="XO AI — Nexo.corp (FREE)",
    page_icon="🤖",
    layout="wide",
)

# -----------------------------------------
# GROQ CLIENT (FREE MODELS)
# -----------------------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# -----------------------------------------
# SYSTEM PROMPT (Professional + Clean)
# -----------------------------------------
SYSTEM_PROMPT = """
You are XO AI, an advanced assistant created by Nexo.corp.

Qualities:
- Professional, mature, respectful.
- Clear, correct, and structured answers.
- Can understand emotions and respond softly.
- Expert in: academics, math, science, coding, business, psychology, productivity, daily problems.
- Use short paragraphs + bullet points for readability.
- No cringe, no childish tone.
- If unsure, say “I’m not fully sure” instead of guessing.
- Tone adjusts to user mood: calm + friendly like ChatGPT, confident like Grok.
"""

# -----------------------------------------
# SAVING CHAT
# -----------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey, I’m XO AI (FREE). How can I help you today?"}
    ]

def new_chat():
    st.session_state.messages = [
        {"role": "assistant", "content": "New chat started. Ask me anything!"}
    ]

# -----------------------------------------
# UI STYLING (elegant grey-black)
# -----------------------------------------
st.markdown("""
<style>
body, .stApp {
    background: #050607;
    color: #f5f5f5;
    font-family: system-ui;
}
.block-container {
    max-width: 900px;
    padding-top: 1.4rem;
    padding-bottom: 2rem;
}
header, #MainMenu, footer {visibility: hidden;}
.chat-title {
    font-size: 1.5rem;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------
# HEADER
# -----------------------------------------
left, right = st.columns([0.7, 0.3])
with left:
    st.markdown('<div class="chat-title">XO AI (Free Mode)</div>', unsafe_allow_html=True)
with right:
    if st.button("New Chat"):
        new_chat()

st.divider()

# -----------------------------------------
# FREE MODEL SELECTOR
# -----------------------------------------
model_choice = st.selectbox(
    "Choose free model:",
    [
        "LLaMA-3.1-8B (Fast + Smart)",
        "Mixtral-8x7B (Strong Reasoning)",
        "Gemma-2-9B (Clean Tone)"
    ],
)

MODEL_MAP = {
    "LLaMA-3.1-8B (Fast + Smart)": "llama-3.1-8b-instant",
    "Mixtral-8x7B (Strong Reasoning)": "mixtral-8x7b-32768",
    "Gemma-2-9B (Clean Tone)": "gemma2-9b-it"
}

MODEL_NAME = MODEL_MAP[model_choice]

# -----------------------------------------
# SHOW CHAT HISTORY
# -----------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------------------
# USER INPUT
# -----------------------------------------
user_text = st.chat_input("Ask XO AI anything...")

if user_text:
    # User bubble
    st.chat_message("user").markdown(user_text)
    st.session_state.messages.append({"role": "user", "content": user_text})

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] +
                         st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

# -----------------------------------------
# FOOTER
# -----------------------------------------
st.markdown("---")
st.caption("By messaging XO AI, you agree to our Terms and Privacy Policy.")
st.caption("Founder: Dev • Nexo.corp")
