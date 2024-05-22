import openai
from config import apikey
import streamlit as st
# Set your OpenAI API key
openai.api_key = apikey

def ai():
    # Set your OpenAI API key
    openai.api_key = apikey

    # Take user input
    user_input = st.text_input("Enter your message: ")
    if user_input:
        # Create an instance of the OpenAI class
        try:
            client = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input},
                ],
            )
        except Exception as e:
            st.error(f"Error: {e}")
            return

        # Access the generated message
        generated_message = client['choices'][0]['message']['content']
        st.subheader(generated_message)

