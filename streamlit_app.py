import streamlit as st
import requests
import json
import os

st.set_page_config(
    page_title="DarkFury - NexoCorp AI",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0 !important; }
    [data-testid="stVerticalBlock"] { gap: 0 !important; padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

NVIDIA_KEY = "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"

# Handle API proxy requests
params = st.query_params

if params.get("action") == "chat":
    try:
        body = json.loads(params.get("body", "{}"))
        res = requests.post(
            "https://integrate.api.nvidia.com/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {NVIDIA_KEY}"
            },
            json={
                "model": "moonshotai/kimi-k2-instruct",
                "messages": body.get("messages", []),
                "temperature": 0.7,
                "top_p": 0.9,
                "max_tokens": 4096
            },
            timeout=60
        )
        st.json(res.json())
    except Exception as e:
        st.json({"error": {"message": str(e)}})
    st.stop()

elif params.get("action") == "image":
    try:
        body = json.loads(params.get("body", "{}"))
        res = requests.post(
            "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux-dev",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {NVIDIA_KEY}",
                "Accept": "application/json"
            },
            json={
                "prompt": body.get("prompt", ""),
                "cfg_scale": 7.5,
                "aspect_ratio": body.get("aspect_ratio", "16:9"),
                "seed": body.get("seed", 42),
                "steps": body.get("steps", 30),
                "negative_prompt": "blurry, low quality, distorted, ugly, watermark"
            },
            timeout=120
        )
        st.json(res.json())
    except Exception as e:
        st.json({"error": {"message": str(e)}})
    st.stop()

# Render the UI
html_path = os.path.join(os.path.dirname(__file__), "darkfury.html")

if not os.path.exists(html_path):
    st.error("darkfury.html not found. Upload it to the same repo folder as streamlit_app.py")
    st.stop()

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Proxy script — routes API calls through Python backend to avoid CORS
proxy_script = """
<script>
const _SL = window.parent.location.href.split('?')[0];

async function callNvidiaChat(messages, systemPrompt) {
    try {
        const payload = JSON.stringify({ messages: [{role:'system',content:systemPrompt},...messages] });
        const url = _SL + '?action=chat&body=' + encodeURIComponent(payload);
        const res = await fetch(url, { credentials: 'include' });
        const text = await res.text();
        const m = text.match(/\{".*?\}/s);
        if (m) { try { return JSON.parse(m[0]); } catch(e) {} }
        const start = text.indexOf('{"');
        if (start >= 0) { try { return JSON.parse(text.slice(start)); } catch(e) {} }
        return { error: { message: 'Parse error: ' + text.slice(0,300) } };
    } catch(e) { return { error: { message: e.message } }; }
}

async function callNvidiaImage(prompt, aspect, steps, seed) {
    try {
        const payload = JSON.stringify({ prompt, aspect_ratio: aspect, steps, seed });
        const url = _SL + '?action=image&body=' + encodeURIComponent(payload);
        const res = await fetch(url, { credentials: 'include' });
        const text = await res.text();
        const start = text.indexOf('{"');
        if (start >= 0) { try { return JSON.parse(text.slice(start)); } catch(e) {} }
        return { error: { message: 'Parse error' } };
    } catch(e) { return { error: { message: e.message } }; }
}
</script>
"""

# Patch chat fetch
html = html.replace(
    "await fetch('https://integrate.api.nvidia.com/v1/chat/completions',{\n      method:'POST',\n      headers:{'Content-Type':'application/json','Authorization':'Bearer '+NVIDIA_KEY},\n      body:JSON.stringify({model:'moonshotai/kimi-k2-instruct',messages:[{role:'system',content:personas[currentPersona].system},...msgs],temperature:0.7,top_p:0.9,max_tokens:4096})\n    });\n    const data=await res.json();",
    "const data=await callNvidiaChat(msgs, personas[currentPersona].system);"
)

# Patch image fetch
html = html.replace(
    "await fetch('https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux-dev',{\n      method:'POST',\n      headers:{'Content-Type':'application/json','Authorization':'Bearer '+NVIDIA_KEY,'Accept':'application/json'},\n      body:JSON.stringify({prompt:p,cfg_scale:7.5,aspect_ratio:aspect,seed:Math.floor(Math.random()*99999),steps:parseInt(steps),negative_prompt:'blurry, low quality, distorted, ugly, watermark'})\n    });\n    const data=await res.json();",
    "const data=await callNvidiaImage(p, aspect, parseInt(steps), Math.floor(Math.random()*99999));"
)

# Inject proxy before </head>
html = html.replace("</head>", proxy_script + "\n</head>")

st.components.v1.html(html, height=900, scrolling=True)
