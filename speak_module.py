import pyttsx3
import streamlit as st

# Initialize session state to store speak_called flag
if 'speak_called' not in st.session_state:
    st.session_state.speak_called = False

def speak(text, male_voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'):
    if text:
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()

        # Set the male voice by ID
        engine.setProperty('voice', male_voice_id)

        # Set the speaking rate (optional)
        engine.setProperty('rate', 150)

        # Speak the text
        engine.say(text)
        engine.runAndWait()

    else:
        st.subheader("")

# Example usage:
text_to_speak = "Hello, I am LUFFY, how can I help you?"
# Check if the function has not been called before
if not st.session_state.speak_called:
    speak(text_to_speak)
    # Set the flag to indicate that the function has been called
    st.session_state.speak_called = True
