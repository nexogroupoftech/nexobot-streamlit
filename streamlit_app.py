import streamlit as st
from openai import OpenAI

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="XO AI — Nexo.corp",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# OPENAI CLIENT
# -------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
MODEL_NAME = "gpt-4o"

# -------------------------
# PROFESSIONAL SYSTEM PROMPT
# -------------------------
SYSTEM_PROMPT = """
You are XO AI, an advanced assistant created by Nexo.corp.

Your qualities:
- Professional, calm, accurate.
- Emotion-aware; respond with empathy when needed.
- Expert in all major fields: science, maths, coding, business, finance, psychology, productivity, daily life.
- Give clean, structured, well-reasoned answers.
- If unsure about something, admit uncertainty.
- Use short paragraphs and bullet points when helpful.
- Tone adjusts based on user emotion (friendly, calm, mature).
- No cringe, no childish behaviour.
- Be smart like ChatGPT + confident like Grok.
"""

# -------------------------
# STATE
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I’m XO AI. How can I help you today?"}
    ]

def new_chat():
    st.session_state.messages = [
        {"role": "assistant", "content": "New chat started. How can XO assist you?"}
    ]

# -------------------------
# STYLING (grey-black elegant)
# -------------------------
st.markdown("""
<style>
body, .stApp {
    background: #050607;
    color: #f5f5f5;
    font-family: system-ui;
}
.block-container {
    max-width: 900px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}
header, #MainMenu, footer {visibility: hidden;}

.chat-title {
    font-size: 1.4rem;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.markdown('<div class="chat-title">XO AI</div>', unsafe_allow_html=True)
with col2:
    if st.button("New chat"):
        new_chat()

st.divider()

# -------------------------
# CHAT HISTORY UI
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# USER INPUT
# -------------------------
user_text = st.chat_input("Ask XO AI anything...")

if user_text:
    # show + store user msg
    st.chat_message("user").markdown(user_text)
    st.session_state.messages.append({"role": "user", "content": user_text})

    # call GPT-4o
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] +
                         st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    # save bot reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
