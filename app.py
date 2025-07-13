# app.py

import streamlit as st
from utils import browser_speak, load_lottie_file
from streamlit_lottie import st_lottie
import time

def main():
    st.set_page_config(page_title="VocalMind", page_icon="🤖", layout="centered")

    # Initialize session states
    if "welcome_done" not in st.session_state:
        st.session_state.welcome_done = False

    # 1. Welcome screen UI (ALWAYS shown)
    st.markdown("<h1 style='text-align:center; color:#4B0082;'>Welcome to VocalMind 🤖</h1>", unsafe_allow_html=True)
    lottie_robot = load_lottie_file("assets/robot.json")
    st_lottie(lottie_robot, height=300)

    # 2. Voice only on FIRST load
    if not st.session_state.welcome_done:
        browser_speak("Welcome to VocalMind, your AI-powered voice assistant ready to serve you.")
        st.session_state.welcome_done = True
        time.sleep(1)  # Let speech JS render fully
        st.experimental_rerun()  # Rerun to show Launch button after speech

    # 3. Now show Launch button (in second run)
    if st.button("🚀 Launch Chatbot"):
        st.session_state.page = "home"
        st.rerun()

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "welcome"

    if st.session_state.page == "welcome":
        main()
    elif st.session_state.page == "home":
        from home import main as home_main
        home_main()
