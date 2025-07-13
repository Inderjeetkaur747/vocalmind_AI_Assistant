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
    st.components.v1.html(
        f"""
        <script>
            var msg = new SpeechSynthesisUtterance("{text}");
            msg.lang = 'en-US';
            window.speechSynthesis.cancel();  // stop any ongoing voice
            window.speechSynthesis.speak(msg);
        </script>
        """,
        height=0,
    )


def open_website(url):
    st.components.v1.html(
        f"""
        <script>
            window.open("{url}", "_blank");
        </script>
        """,
        height=0,
    )
