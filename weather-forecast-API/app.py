from fastapi import FastAPI
import requests
import os   # <-- REQUIRED IMPORT

app = FastAPI(title="Weather Forecast API")

# Load API key from environment variable (recommended)
API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

@app.get("/")
def home():
    return {"message": "Weather Forecast API is running!"}

@app.get("/weather/{city}")
def get_weather(city: str):
    url = BASE_URL.format(city, API_KEY)
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "City not found or API request failed"}

    data = response.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }
