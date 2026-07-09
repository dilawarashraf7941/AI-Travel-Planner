from utils import get_model

model = get_model()


def activity_info(
    destination: str,
    days: int,
    budget: float,
    travel_style: str,
    travelers: int,
) -> str:
    """
    Generate Gemini-powered activity and experience recommendations for the
    given destination, adapted to trip duration, budget, travel style, and
    number of travelers.
    """

    prompt = f"""
You are a Senior AI Travel Activities Specialist.

Prepare concise, well-structured activity recommendations for the trip
described below.

Destination: {destination}
Trip Duration: {days} days
Budget: {budget} USD
Travel Style: {travel_style}
Travelers: {travelers}

Adapt every recommendation to this specific budget, trip length, travel
style, and number of travelers, rather than giving generic advice.

Return EXACTLY the following format.

Destination Highlights:
Provide a short overview of what makes this destination special for this
trip.

Must-Visit Attractions:
List key attractions travelers should prioritize given the trip duration.

Outdoor Activities:
Recommend outdoor activities suited to this destination and travel style.

Indoor Activities:
Recommend indoor activities suited to this destination and travel style.

Family Activities:
Recommend activities suitable for the given number and type of
travelers, if relevant.

Adventure Activities:
Recommend activities suited to adventure travelers, if relevant to the
travel style.

Food Experiences:
Recommend notable local food and dining experiences within the given
budget.

Shopping Recommendations:
Recommend types of shopping experiences and areas.

Nightlife:
Describe the nightlife scene and options available, if relevant to the
travel style and travelers.

Estimated Activity Budget:

Budget:
Mid-range:
Luxury:

Provide relative cost guidance rather than exact figures, scaled to the
given trip duration and number of travelers.

Local Etiquette:
Mention important cultural etiquette and customs to respect.

Travel Tips:
Provide useful, practical tips for enjoying activities at this
destination given the trip duration and travel style.

IMPORTANT

Keep every section concise.

Use bullet points where appropriate.

Do NOT invent exact ticket prices.

Do NOT invent opening hours.

Focus on travel strategy rather than advertisements.
"""

    try:
        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception:
        return f"""
Destination Highlights:
Activity information for {destination} is currently unavailable.

Must-Visit Attractions:
Unavailable.

Outdoor Activities:
Unavailable.

Indoor Activities:
Unavailable.

Family Activities:
Unavailable.

Adventure Activities:
Unavailable.

Food Experiences:
Unavailable.

Shopping Recommendations:
Unavailable.

Nightlife:
Unavailable.

Estimated Activity Budget:
Unavailable.

Local Etiquette:
Unavailable.

Travel Tips:
Please try again later.
""".strip()
