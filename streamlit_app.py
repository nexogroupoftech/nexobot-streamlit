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

params = st.query_params

if params.get("action") == "chat":
    try:
        body = json.loads(params.get("body", "{}"))
        res = requests.post(
            "https://integrate.api.nvidia.com/v1/chat/completions",
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {NVIDIA_KEY}"},
            json={"model": "moonshotai/kimi-k2-instruct", "messages": body.get("messages", []),
                  "temperature": 0.6, "top_p": 0.9, "max_tokens": 4096},
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
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {NVIDIA_KEY}", "Accept": "application/json"},
            json={"prompt": body.get("prompt", ""), "cfg_scale": 7.5,
                  "aspect_ratio": body.get("aspect_ratio", "16:9"),
                  "seed": body.get("seed", 42), "steps": body.get("steps", 30),
                  "negative_prompt": "blurry, low quality, distorted, ugly, watermark"},
            timeout=120
        )
        st.json(res.json())
    except Exception as e:
        st.json({"error": {"message": str(e)}})
    st.stop()

html_path = os.path.join(os.path.dirname(__file__), "darkfury.html")
if not os.path.exists(html_path):
    st.error("darkfury.html not found.")
    st.stop()

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=900, scrolling=True)
