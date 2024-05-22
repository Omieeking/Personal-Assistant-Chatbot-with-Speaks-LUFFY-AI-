import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st
import re


def send_email(sender_email, receiver_email, subject, body, password):
    try:
        # Validate email addresses
        if not re.match(r"[^@]+@[^@]+\.[^@]+", sender_email):
            raise ValueError("Invalid sender email address")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", receiver_email):
            raise ValueError("Invalid receiver email address")

        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        # Setup the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)

            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())

        st.success("Email sent successfully!")
    except Exception as e:
        st.error(f"Failed to send the email. Error: {e}")
