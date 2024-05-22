# -*- coding: utf-8 -*-
from time_module import get_time, get_date
from database import *
from internet import check_internet_connection, check_on_wikipedia
from web_jobs import *
from music import *
from news import get_news
from wallpaper import rotate_wallpapers
from weather import get_weather
from openaimyscricpt import *
from sending_mail import send_email
from speak_module import speak
import pyjokes
import streamlit as st

def process(query):
    if 'play' in query and 'music' not in query:
        answer = get_answer_from_memory('play')
    else:
        answer = get_answer_from_memory(query)
    if answer:
        if answer == "get time details":
            return ("Time is " + get_time())

        elif answer == "check internet connection":
            if check_internet_connection():
                return "internet is connected"
            else:
                return "internet is not connected"

        elif answer == "tell date":
            return "Date is " + get_date()

        elif "mail" in answer or "email" in answer or "gmail" in answer:
            try:
                # Get user input for email configuration
                sender_email = st.text_input("Enter your email address:")
                receiver_email = st.text_input("Enter the recipient's email address:")
                subject = st.text_input("Enter the subject of the email:")
                body = st.text_area("Enter the body of the email:")
                password = st.text_input("Enter your email password:", type="password")

                if st.button("Send Email"):
                    send_email(sender_email, receiver_email, subject, body, password)

            except Exception as e:
                st.subheader(e)
                speak("I am not able to send this email")

        # openai function chatgpt and conversation

        elif answer == "using ai":
            return ai()

        elif answer == "luffy quit":
            exit()

        elif answer == "luffy reset chat":
            chatStr = ""

        # speak on and off funtion

        elif answer == "on speak":
            return turn_on_speech()

        elif answer == "off speak":
            return turn_off_speech()

        # joke function
        elif 'joke' in answer:
            st.subheader(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        # for wikipedia search
        elif answer == "":
            return check_on_wikipedia(query)

        elif answer == "wikipedia":
            return check_on_wikipedia(query)

        elif answer == "who is":
            return check_on_wikipedia(query)

        elif answer == "tell me about":
            return check_on_wikipedia(query)

        elif answer == "what is":
            return check_on_wikipedia(query)

        elif answer == "do you know":
            return check_on_wikipedia(query)

        elif answer == "what is meant by":
            return check_on_wikipedia(query)

        elif answer == "it means":
            return check_on_wikipedia(query)

        elif answer == "when did":
            return check_on_wikipedia(query)

        # for opening and closing websites

        elif answer == "close chrome":
            close_chrome()
            return "closing chrome"

        elif answer == "close bing":
            close_bing()
            return "closing bing"

        elif answer == "close edge":
            close_edge()
            return "closing edge"

        elif answer == "open facebook":
            open_facebook()
            return "opening facebook"

        elif answer == "open google":
            open_google()
            return "opening google"

        elif answer == "open instagram":
            open_instagram()
            return "opening instagram"

        elif answer == "open twitter":
            open_twitter()
            return "opening twitter"

        elif answer == "open bing":
            open_bing()
            return "opening bing"

        elif answer == "open wikipedia":
            open_wikipedia()
            return "opening wikipedia"

        elif answer == "open stackoverflow":
            open_stackoveflow()
            return "opening stackoverflow"

        elif answer == "open i love pdf":
            open_i_love_pdf()
            return "opening i love pdf"

        elif answer == "open chatgpt":
            open_chatgpt()
            return "opening chatgpt"

        elif answer == "open youtube":
            open_youtube()
            return "opening youtube"

        # MUSIC PLAYBACK
        elif answer == "play music" or answer == "play song":
            return play_song()

        elif answer == "pause music" or answer == "pause song":
            return pause_song()
        elif answer == "unpause music" or answer == "unpause song" or answer == "resume music" or answer == "resume song":
            return resume_song()

        elif answer == "stop music" or answer == "stop song":
            return stop_song()

        elif answer == "next music" or answer == "next song":
            return next_song()

        elif answer == "previous music" or answer == "previous song":
            return previous_song()

        elif answer == "get news":
            news = get_news()
            if news:
                for i, article in enumerate(news, start=1):
                    st.write(f"News {i}: {article}")
                    speak(article)
            else:

                st.write("No news articles found.")  # Or display an appropriate message if no news articles are available

        # CHANGING WALLPAPER
        elif answer == "change wallpaper":
            wallpapers_directory = r"C:\Users\Omkar Jadhav\OneDrive\Pictures\wallapapers"
            wallpaper_changed, message = rotate_wallpapers(wallpapers_directory)

            if wallpaper_changed:
                st.markdown("LUFFY AI: Wallpaper is changed successfully")
                speak("wallpaper is changed successfully")
            else:
                st.subheader(f"Failure: {message}")

        # WEATHER API
        elif answer == "today weather":

            # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
            api_key = "Enter your openweathermap api key"

            # Get user input for the city
            city_name = st.text_input('Enter the city for weather information: ')

            if city_name:
                temperature, humidity = get_weather(api_key, city_name)

                if temperature is not None:
                    st.subheader(f'Temperature in {city_name}: {temperature}°C')
                    speak(f'Temperature in {city_name}: {temperature}°Celsius')
                    st.subheader(f'Humidity in {city_name}: {humidity}%')
                    speak(f'Humidity in {city_name}: {humidity}percent')
                else:
                    st.subheader(f'Error: {humidity}')

        else:
            return "Sorry, I couldn't find any relevant information."