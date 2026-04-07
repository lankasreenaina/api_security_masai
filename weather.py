import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    # Location data must not be logged to console or any log file.
    # Logging city names constitutes processing of personal/location data
    # under GDPR (Article 5) and HIPAA's minimum necessary principle,
    # which prohibit unnecessary retention or exposure of user information.

    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 429:
            print("Rate limit exceeded. Please wait a moment and try again.")
            return

        if response.status_code == 401:
            print("Invalid API key. Please check your .env file.")
            return

        if response.status_code == 404:
            print("City not found. Please check the city name.")
            return

        if response.status_code != 200:
            print(f"Unexpected error: {response.status_code}")
            return

        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"Temperature: {temp}°C, Condition: {description}")

    except requests.exceptions.ConnectionError:
        print("Network error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)