import streamlit as st
import json
import pyttsx3
import webbrowser
from streamlit.components.v1 import html


def load_lottie_file(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        return None

def browser_speak(text):
    st.markdown(
        f"""
        <script>
            var msg = new SpeechSynthesisUtterance("{text}");
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(msg);
        </script>
        """,
        unsafe_allow_html=True,
    )

def open_website(url):
    st.markdown(
        f"""
        <script>
            window.open("{url}", "_blank");
        </script>
        """,
        unsafe_allow_html=True,
    )
