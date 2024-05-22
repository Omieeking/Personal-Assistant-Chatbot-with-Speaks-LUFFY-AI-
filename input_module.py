import streamlit as st
import numpy as np
import time

# def take_input():
#     # command line input
#     key = np.random.randint(0, 1000)
#
#     i = st.text_input("me: ", key=key)
#
#     if i:
#         st.title(i)
#         return i



def take_input(prompt="me: "):
    # Display the prompt and get user input
    user_input = st.text_input(prompt)

    # Return the user input
    return user_input.strip() if user_input else None




# import streamlit as st
#
# def take_input(key_suffix):
#     try:
#         i = st.text_input("me: ", key="input_" + key_suffix)
#     except Exception as e:
#         st.error(f"Error occurred: {e}")
#         i = None
#     return i









    # else:
    #     st.subheader(" ")

import sys

# def take_input(entry_widget):
#     return entry_widget




        # sys.exit()

# backend/input_handler.py

# def take_input(entry_text):
#     # Instead of command line input, use the entry text passed from the GUI
#     return entry_text




# backend/input_handler.py

# def take_input(user_input):
#     # Your processing logic here
#     print(f"Received input from GUI: {user_input}")
