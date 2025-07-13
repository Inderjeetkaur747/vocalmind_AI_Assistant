import streamlit as st
from streamlit_lottie import st_lottie
from utils import load_lottie_file
import time
import streamlit.components.v1 as components  # for JS injection

def speak_js(text):
    components.html(
        f"""
        <script>
            var msg = new SpeechSynthesisUtterance("{text}");
            window.speechSynthesis.speak(msg);
        </script>
        """,
        height=0,
    )

def main():
    st.set_page_config(page_title="VocalMind", page_icon="🤖", layout="centered")

    if "welcome_done" not in st.session_state:
        st.session_state.welcome_done = False

    # UI: Welcome text & animation
    st.markdown("<h1 style='text-align:center; color:#4B0082;'>Welcome to VocalMind 🤖</h1>", unsafe_allow_html=True)
    lottie_robot = load_lottie_file("assets/robot.json")
    st_lottie(lottie_robot, height=300)

    # Speak only once on first open
    if not st.session_state.welcome_done:
        speak_js("Welcome to VocalMind, your AI-powered voice assistant ready to serve you.")
        st.session_state.welcome_done = True
        time.sleep(1)
        st.experimental_rerun()

    # Show launch button after voice
    if st.session_state.welcome_done:
        if st.button("🚀 Launch VocalMind"):
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
