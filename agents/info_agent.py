from tools.weather_tools import get_weather
from utils import get_model

model = get_model()


def travel_info(
    destination: str,
    days: int,
    budget: float,
    travel_style: str,
    travelers: int,
) -> str:
    """
    Generate a comprehensive travel guide for the specified destination,
    personalized using trip details and live weather information.
    """

    try:
        weather = get_weather(destination)
    except Exception:
        weather = {"error": "Weather data unavailable"}

    if weather and "error" not in weather:
        weather_section = f"""
Current Weather:
Temperature: {weather['temperature']}
Condition: {weather['condition']}
Humidity: {weather['humidity']}
Wind Speed: {weather['wind_speed']}
"""
    else:
        weather_section = """
Current Weather:
Not available.
"""

    prompt = f"""
You are a Senior AI Travel Information Specialist.

Prepare a professional travel guide.

Trip Details

Destination: {destination}
Trip Duration: {days} days
Budget: {budget} USD
Travel Style: {travel_style}
Travelers: {travelers}

Live Weather

{weather_section}

Personalize ALL recommendations using:

- destination
- trip duration
- budget
- travel style
- number of travelers
- live weather (if available)

Return EXACTLY the following structure.

Destination Overview:

Current Weather:

Best Time to Visit:

Local Culture:

Transportation:

Safety Tips:

Currency:

Language:

Visa Considerations:

Food Recommendations:

Estimated Daily Budget:

Travel Tips:

IMPORTANT

- Keep every section concise.
- Use bullet points where appropriate.
- Use the provided weather information.
- Do NOT invent weather.
- Do NOT provide legal advice regarding visas.
"""

    try:
        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception:
        return f"""
Destination Overview:
Information for {destination} is currently unavailable.

Current Weather:
{weather_section.strip()}

Best Time to Visit:
Unavailable.

Local Culture:
Unavailable.

Transportation:
Unavailable.

Safety Tips:
Unavailable.

Currency:
Unavailable.

Language:
Unavailable.

Visa Considerations:
Unavailable.

Food Recommendations:
Unavailable.

Estimated Daily Budget:
Unavailable.

Travel Tips:
Please try again later.
""".strip()