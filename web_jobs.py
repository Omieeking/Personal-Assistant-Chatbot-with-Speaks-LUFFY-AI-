import webbrowser
import os

def open_facebook():
    webbrowser.open("https://facebook.com")

def open_google():
    webbrowser.open('https://google.com')

def open_youtube():
    webbrowser.open('https://youtube.com')

def games():
    webbrowser.open('https://poki.com')

def open_chatgpt():
    webbrowser.open('https://chatgpt.com')

def open_instagram():
    webbrowser.open('https://instagram.com')

def open_wikipedia():
    webbrowser.open('https://wikipedia.com')

def open_stackoveflow():
    webbrowser.open('https://stackoverflow.com')

def open_bing():
    webbrowser.open('https://bing.com')

def open_twitter():
    webbrowser.open('https://twitter.com')

def open_i_love_pdf():
    webbrowser.open('https://i_love_pdf.com')

def close_chrome():
    os.system('taskkill /F /IM chrome.exe')

def close_bing():
    os.system('taskkill /F /IM bing.exe')

def close_edge():
    os.system("taskkill /F /IM MicrosoftEdge.exe")

