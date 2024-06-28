# -*- coding: utf-8 -*-

import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"




    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Use 'metric' for Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        data = response.json()

        if response.status_code == 200:
            # Extract relevant information from the response
            temperature = data['main']['temp']
            humidity = data['main']['humidity']

            return temperature, humidity
        else:
            return None, f'Error: {data["message"]}'

    except requests.RequestException as e:
        return None, f'Request error: {e}'

    except Exception as e:
        return None, f'An unexpected error occurred: {e}'
