from utils import get_model

model = get_model()


def flight_info(
    destination: str,
    days: int,
    budget: float,
    travel_style: str,
    travelers: int,
) -> str:
    """
    Generate Gemini-powered flight recommendations for the given
    destination, adapted to trip duration, budget, travel style, and
    number of travelers.
    """

    prompt = f"""
You are a Senior AI Flight Travel Advisor.

Prepare concise, well-structured flight recommendations for the trip
described below.

Destination: {destination}
Trip Duration: {days} days
Budget: {budget} USD
Travel Style: {travel_style}
Travelers: {travelers}

Adapt every recommendation to this specific budget, trip length, travel
style, and number of travelers, rather than giving generic advice.

Consider both domestic and international travel scenarios as relevant to
this destination.

Return EXACTLY the following structure.

Flight Overview:
Brief summary of flight connectivity and travel considerations for this
specific trip.

Best Airports:
Major airports serving this destination and nearby alternatives.

Recommended Airlines:
Types/categories of airlines suited to this route and travel style (e.g.
full-service, budget, regional) without naming real-time schedules.

Budget Flight Tips:
Practical tips for finding lower-cost flights within the given budget.

Business Class Advice:
Guidance on whether business class is worthwhile given the travel style,
budget, and number of travelers.

Best Booking Time:
General guidance on when to book for the best value.

Baggage Advice:
Practical baggage allowance and packing considerations for this group
size and trip duration.

Estimated Flight Cost:
General relative cost guidance (e.g. budget/mid-range/premium ranges)
for this number of travelers, without stating specific real-time prices.

Travel Documents:
Documents travelers should prepare (passport, visa, ID) at a general
level, without providing legal advice.

Tips:
Additional practical tips for flying to this destination for this trip.

IMPORTANT

Keep every section concise and use bullet points where appropriate.

Do NOT invent specific flight prices, fares, or airline schedules, since
this information changes frequently and must be verified by the traveler
at the time of booking.
"""

    try:
        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception:
        return f"""
Flight Overview:
Flight information for {destination} is currently unavailable.

Best Airports:
Unavailable.

Recommended Airlines:
Unavailable.

Budget Flight Tips:
Unavailable.

Business Class Advice:
Unavailable.

Best Booking Time:
Unavailable.

Baggage Advice:
Unavailable.

Estimated Flight Cost:
Unavailable.

Travel Documents:
Unavailable.

Tips:
Please try again later.
""".strip()
