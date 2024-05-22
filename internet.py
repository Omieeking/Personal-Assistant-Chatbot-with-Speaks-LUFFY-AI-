import urllib.request
import wikipedia

def check_internet_connection():

    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False


def check_on_wikipedia(query):
    query = query.lower()
    query = query.replace("who is", "")
    query = query.replace("what is", "")
    query = query.replace("do you know", "")
    query = query.replace("tell me about", "")

    query = query.strip()

    try:
         data = wikipedia.summary(query,  sentences=2)
         return data
    except Exception as e:
        return ""