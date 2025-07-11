# home.py

import streamlit as st
import cohere
from utils import browser_speak, load_lottie_file, open_website
from streamlit_lottie import st_lottie
import re

# Cohere API setup
COHERE_API_KEY = "lWIySBzBjfdDMVbCYRB4bGBT8s7lp6i3mvXLHM6r"
co = cohere.Client(COHERE_API_KEY)

def get_ai_response(prompt):
    try:
        response = co.chat(message=prompt)
        reply = response.text
        if not reply:
            reply = "Sorry, I don't know the answer to that."
        return reply
    except Exception as e:
        return "Error: " + str(e)

# Special commands like YouTube, Google
def process_special_commands(user_input):
    user_input_lower = user_input.lower()

    # YouTube Search
    if "youtube" in user_input_lower:
        match = re.search(r'play\s+(.*?)\s*(on\s+youtube|youtube)', user_input_lower)
        search_query = match.group(1).strip() if match else ""
        url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}" if search_query else "https://www.youtube.com"
        open_website(url)
        return f"Opening YouTube for '{search_query}'." if search_query else "Opening YouTube."

    # Google Search
    elif "google" in user_input_lower:
        match = re.search(r'search\s+(.*?)\s*(on\s+google|google)', user_input_lower)
        search_query = match.group(1).strip() if match else ""
        url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}" if search_query else "https://www.google.com"
        open_website(url)
        return f"Searching Google for '{search_query}'." if search_query else "Opening Google."

    # Spotify
    elif "spotify" in user_input_lower:
        open_website("https://open.spotify.com")
        return "Opening Spotify for you."

    return None

def main():
    st.set_page_config(page_title="VocalMind Home", page_icon="🤖", layout="centered")

    # Welcome voice once
    if "home_welcome_done" not in st.session_state:
        browser_speak("Welcome back to VocalMind Chat. How can I assist you today?")
        st.session_state.home_welcome_done = True

    # Init states
    st.session_state.setdefault("chat_history", [])
    st.session_state.setdefault("voice_enabled", True)

    # Header + Animation
    st_lottie(load_lottie_file("assets/robot.json"), height=250)
    st.markdown("<h2 style='text-align:center; color:#4B0082;'>VocalMind Chat 🤖</h2>", unsafe_allow_html=True)

    # Voice Toggle
    st.session_state.voice_enabled = st.toggle("🔊 Voice Responses", value=st.session_state.voice_enabled)

    # Show chat history
    for chat in st.session_state.chat_history:
        sender, message = chat["sender"], chat["message"]
        align = "right" if sender == "user" else "left"
        bg_color = "#DCF8C6" if sender == "user" else "#E6E6E6"
        st.markdown(f"""
            <div style='text-align:{align}; margin:10px;'>
                <div style='display:inline-block; padding:10px 15px; background-color:{bg_color}; border-radius:15px; max-width:70%; font-size:16px;'>
                    <b>{sender.capitalize()}:</b> {message}
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Input box (clears automatically after send)
    user_input = st.text_input("Ask me something...", placeholder="Type your question here...", key=str(len(st.session_state.chat_history)))

    # Process user input
    if user_input and "input_processed" not in st.session_state:
        st.session_state.chat_history.append({"sender": "user", "message": user_input})

        # Special or AI response
        special_reply = process_special_commands(user_input)
        reply = special_reply if special_reply else get_ai_response(user_input)

        # Add AI response to chat
        st.session_state.chat_history.append({"sender": "vocalmind", "message": reply})

        # Save last reply → speak in next rerun
        st.session_state.last_reply = reply
        st.session_state.input_processed = True
        st.rerun()

    # Speak after showing text (only if voice is enabled)
    if "last_reply" in st.session_state:
        if st.session_state.voice_enabled:
            browser_speak(st.session_state.last_reply)

        # Clear session flags
        del st.session_state.last_reply
        del st.session_state.input_processed

    # Back Button
    if st.button("🔙 Back"):
        st.session_state.clear()
        st.session_state.page = "welcome"
        st.rerun()
