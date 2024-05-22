import requests
from output_module import output
from internet import check_internet_connection
import streamlit as st


def get_news():
    try:
        if check_internet_connection():
            # BBC news api
            main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=c3b70390df514bb6b2aba26e93baf34d"

            # Fetching data in JSON format
            open_bbc_page = requests.get(main_url).json()

            # Getting all articles in a string article
            articles = open_bbc_page.get("articles", [])

            if not articles:
                st.subheader("No articles found.")
                return []

            # Outputting news articles with indices
            for idx, article in enumerate(articles, start=1):
                output(f"News {idx}: {article['title']}")

            # Extracting titles for returning
            titles = [article['title'] for article in articles]
            return titles
        else:
            st.subheader("Error: Please check your internet connection.")
            return []
    except requests.exceptions.ConnectionError:
        st.subheader("Error: Unable to connect to the news server. Please check your internet connection.")
        return []
    except requests.exceptions.RequestException as e:
        st.subheader(f"An error occurred: {e}")
        return []


# Example usage
get_news()