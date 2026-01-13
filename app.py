import streamlit as st
import time
from PIL import Image
import os

st.set_page_config(page_title="Panda Studios Online", page_icon="🐼", layout="wide")

# CSS Styling
st.markdown("""
<style>
    .stApp { background-color: #0E1117; }
    .stTextInput input {
        background-color: #262730 !important;
        color: white !important;
        border-radius: 8px;
    }
    div.stButton > button {
        background-color: #ffffff;
        color: black;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        border: none;
        padding: 10px;
    }
    div.stButton > button:hover {
        background-color: #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# Login System
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        # GitHub లో అప్‌లోడ్ చేసిన ఇమేజ్ ని ఇది తీసుకుంటుంది
        if os.path.exists("panda_art.jpg"):
            image = Image.open("panda_art.jpg")
            st.image(image, use_container_width=True)
        else:
            st.warning("⚠️ Please upload 'panda_art.jpg' to your GitHub repository!")

    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("## 🐼 Panda Studios")
        st.caption("Director Access Only")
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if password == "1234":
                st.success("✅ Access Granted!")
                time.sleep(1)
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("❌ Wrong Password!")

else:
    st.title("📂 Director's Dashboard")
    st.write("Welcome Hitesh! System is Online.")
    st.text_area("Script Writer", height=200)
    st.button("Save Script")
