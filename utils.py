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
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        html(
            f"""
            <script>
                var msg = new SpeechSynthesisUtterance("{text}");
                window.speechSynthesis.speak(msg);
            </script>
            """,
            height=0,
        )

def open_website(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        pass
