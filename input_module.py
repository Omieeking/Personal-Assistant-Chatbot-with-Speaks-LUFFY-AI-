import streamlit as st

def take_input(prompt="me: "):
    # Display the prompt and get user input
    user_input = st.text_input(prompt)

    # Return the user input
    return user_input.strip() if user_input else None