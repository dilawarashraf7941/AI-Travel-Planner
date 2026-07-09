from utils import get_model

model = get_model()


def planner(user_request: str) -> str:
    """
    Analyze the user's travel request and produce a planning strategy
    for downstream travel agents.
    """

    prompt = f"""
You are a Senior AI Travel Planning Agent.

Your job is to analyze the user's travel request and decide which travel
services are required before creating the final itinerary.

User Request

{user_request}

Carefully analyze:

- Destination
- Number of Days
- Budget
- Travel Style
- Number of Travelers

Based on the above information determine whether the following services
are required.

Need Info: Yes/No
Need Hotel: Yes/No
Need Flight: Yes/No
Need Activities: Yes/No

Then provide the following sections.

Trip Summary:
Provide a concise overview of the trip.

Budget Strategy:
Suggest how the budget should be distributed across:
- Flights
- Hotels
- Food
- Activities
- Emergency Expenses

Travel Advice:
Give practical recommendations considering:
- destination
- weather (if available)
- travel style
- number of travelers
- trip duration

IMPORTANT

Return EXACTLY this structure.

Need Info:
Need Hotel:
Need Flight:
Need Activities:

Trip Summary:

Budget Strategy:

Travel Advice:
"""

    try:
        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as exc:
        return f"Planner Error: {str(exc)}"