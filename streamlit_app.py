import os
import streamlit as st
import requests
from groq import Groq

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="DarkFury",
    page_icon="🐉",
    layout="wide"
)

# ================= UI STYLE =================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0b0f19;
    color: #e5e7eb;
}

header[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="chat-message-avatar"] {
    display: none !important;
}

.stChatMessage {
    padding-left: 0 !important;
    padding-right: 0 !important;
}

.stChatMessage[data-testid="chat-message-user"] > div {
    background: #111827;
    border-radius: 14px;
    padding: 0.7rem 0.9rem;
    max-width: 72%;
}

.stChatMessage[data-testid="chat-message-assistant"] > div {
    background: #020617;
    border-radius: 14px;
    padding: 0.7rem 0.9rem;
    max-width: 72%;
    border: 1px solid rgba(148,163,184,0.15);
}

textarea {
    background: #020617 !important;
    color: #e5e7eb !important;
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ================= STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "welcome_done" not in st.session_state:
    st.session_state.welcome_done = False

# ================= HEADER =================
st.markdown("<h2 style='text-align:center;'>DarkFury</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; opacity:0.6; font-size:0.85rem;'>Silent · Fast · Intelligent</p>",
    unsafe_allow_html=True
)

# ================= TOGGLES =================
web_search = st.toggle("Web search (beta)", value=False)

# ================= GROQ =================
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.1-8b-instant"

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are DarkFury.\n\n"
        "You are a fast, thoughtful, and reliable AI assistant.\n"
        "Your responses are clear, natural, and confident.\n"
        "You communicate like a skilled human—not a machine.\n\n"
        "LANGUAGE:\n"
        "- Automatically detect the user’s language.\n"
        "- Reply in the same language naturally.\n"
        "- Handle mixed languages naturally.\n\n"
        "STYLE:\n"
        "- Be concise by default.\n"
        "- Expand only when necessary.\n"
        "- Explain complex ideas simply.\n"
        "- Answer simple questions directly.\n\n"
        "REASONING:\n"
        "- Reason carefully.\n"
        "- Avoid assumptions.\n"
        "- Admit uncertainty honestly.\n\n"
        "RULES:\n"
        "- No emojis unless user uses them.\n"
        "- No fluff.\n"
        "- No mention of system instructions."
    )
}

# ================= WELCOME =================
if not st.session_state.welcome_done:
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "I’m DarkFury.\n\n"
            "Fast thinking. Clear answers.\n\n"
            "Ask anything."
        )
    })
    st.session_state.welcome_done = True

# ================= CHAT HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ================= USER INPUT =================
user_input = st.chat_input("Ask. Plan. Decide.")

def web_lookup(query):
    url = "https://duckduckgo.com/html/"
    res = requests.post(url, data={"q": query})
    return res.text[:2000]

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    recent_messages = st.session_state.messages[-8:]

    groq_messages = [SYSTEM_MESSAGE] + [
        {"role": m["role"], "content": m["content"]}
        for m in recent_messages
        if m["role"] in ("user", "assistant")
    ]

    if web_search:
        web_data = web_lookup(user_input)
        groq_messages.append({
            "role": "system",
            "content": (
                "Web search results available.\n"
                "Summarize clearly and cite sources.\n\n"
                f"{web_data}"
            )
        })

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_reply = ""

        stream = client.chat.completions.create(
            model=MODEL,
            messages=groq_messages,
            temperature=0.6,
            max_tokens=250,
            stream=True
        )

        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            full_reply += delta
            placeholder.markdown(full_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_reply
    })

    st.rerun()
