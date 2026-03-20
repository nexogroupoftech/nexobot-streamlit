import streamlit as st
import os

st.set_page_config(
    page_title="DarkFury - NexoCorp AI",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI chrome
st.markdown("""
<style>
    #MainMenu, header, footer { visibility: hidden; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"] { padding: 0 !important; }
    [data-testid="stVerticalBlock"] { gap: 0 !important; padding: 0 !important; }
    iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

# Read the HTML file from the same directory
html_path = os.path.join(os.path.dirname(__file__), "darkfury.html")

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=900, scrolling=False)
else:
    st.error("darkfury.html not found. Make sure it is in the same folder as streamlit_app.py")
