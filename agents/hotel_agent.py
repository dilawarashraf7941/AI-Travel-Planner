from utils import get_model

model = get_model()


def hotel_info(
    destination: str,
    days: int,
    budget: float,
    travel_style: str,
    travelers: int,
) -> str:
    """
    Generate Gemini-powered hotel and accommodation recommendations for the
    given destination, adapted to trip duration, budget, travel style, and
    number of travelers.
    """

    prompt = f"""
You are a Senior AI Hotel and Accommodation Advisor.

Prepare concise, well-structured hotel recommendations for the trip
described below.

Destination: {destination}
Trip Duration: {days} days
Budget: {budget} USD
Travel Style: {travel_style}
Travelers: {travelers}

Adapt every recommendation to this specific budget, trip length, travel
style, and number of travelers, rather than giving generic advice.

Return EXACTLY the following structure.

Accommodation Overview:
Brief summary of the accommodation landscape in this destination for this
specific trip.

Recommended Areas:
Best neighborhoods/areas to stay in, with a short reason for each.

Recommended Hotel Types:
Types of accommodation suited to this destination, travel style, and
group size.

Budget Recommendations:
Guidance for staying within the given budget across the full trip
duration.

Luxury Recommendations:
Guidance for travelers seeking a premium experience, if the budget and
travel style allow.

Family Recommendations:
Guidance for families traveling with children, if relevant to the number
of travelers.

Safety Considerations:
Important safety factors to consider when choosing accommodation here.

Booking Advice:
Practical tips for booking (timing, platforms, negotiation, cancellation
policies) given the trip duration and travelers.

Estimated Hotel Cost:
Approximate nightly and total cost ranges for this budget and trip
duration.

Tips:
Additional practical tips for accommodation in this destination.

IMPORTANT

Keep every section concise and use bullet points where appropriate.

Do not invent specific hotel names; focus on areas, types, and guidance.
"""

    try:
        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception:
        return f"""
Accommodation Overview:
Hotel information for {destination} is currently unavailable.

Recommended Areas:
Unavailable.

Recommended Hotel Types:
Unavailable.

Budget Recommendations:
Unavailable.

Luxury Recommendations:
Unavailable.

Family Recommendations:
Unavailable.

Safety Considerations:
Unavailable.

Booking Advice:
Unavailable.

Estimated Hotel Cost:
Unavailable.

Tips:
Please try again later.
""".strip()
