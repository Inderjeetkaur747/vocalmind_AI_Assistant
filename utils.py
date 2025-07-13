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

# def browser_speak(text):
#     st.components.v1.html(
#         f"""
#         <script>
#             var msg = new SpeechSynthesisUtterance("{text}");
#             msg.lang = 'en-US';
#             window.speechSynthesis.cancel();  // stop any ongoing voice
#             window.speechSynthesis.speak(msg);
#         </script>
#         """,
#         height=0,
#     )
def browser_speak(text):
    try:
        # Break long text into smaller sentences (max ~150 chars)
        chunks = []
        sentence = ""
        for word in text.split():
            if len(sentence + word) < 150:
                sentence += word + " "
            else:
                chunks.append(sentence.strip())
                sentence = word + " "
        if sentence:
            chunks.append(sentence.strip())

        # Inject each sentence as JS to speak
        js_code = "<script>"
        for chunk in chunks:
            js_code += f'var msg = new SpeechSynthesisUtterance("{chunk}"); window.speechSynthesis.speak(msg);'
        js_code += "</script>"

        components.html(js_code, height=0)

    except Exception as e:
        pass

def open_website(url):
    st.components.v1.html(
        f"""
        <script>
            window.open("{url}", "_blank");
        </script>
        """,
        height=0,
    )
