import requests
from config import WEATHER_API_KEY


def get_weather(destination):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={destination}&appid={WEATHER_API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return {
                "error": data.get("message", "Weather not found")
            }

        return {
            "destination": destination,
            "temperature": f"{data['main']['temp']}°C",
            "condition": data["weather"][0]["main"],
            "humidity": f"{data['main']['humidity']}%",
            "wind_speed": f"{data['wind']['speed']} m/s"
        }

    except Exception as e:
        return {
            "error": str(e)
        }