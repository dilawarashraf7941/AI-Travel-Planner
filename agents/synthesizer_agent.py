from utils import get_model

model = get_model()


def create_itinerary(info: str, hotel: str, flight: str, activity: str) -> str:
    """
    Synthesize destination, hotel, flight, and activity recommendations
    into a single professional, markdown-formatted travel itinerary.
    """

    prompt = f"""
You are a Senior AI Travel Itinerary Architect.

Your responsibility is to combine information from multiple AI travel agents
into ONE professional travel itinerary.

=========================
DESTINATION INFORMATION
=========================
{info}

=========================
HOTEL INFORMATION
=========================
{hotel}

=========================
FLIGHT INFORMATION
=========================
{flight}

=========================
ACTIVITIES
=========================
{activity}

Create ONE cohesive itinerary.

Return EXACTLY the following markdown structure.

# Trip Overview

## Best Time to Visit

## Accommodation Plan

## Flight Strategy

## Daily Itinerary

### Day 1

### Day 2

(If trip duration is unknown, generate a generic 3-day itinerary.)

## Food Recommendations

## Estimated Budget Summary

## Travel Checklist

## Safety Notes

## Final Travel Tips

IMPORTANT

- Use professional travel writing.
- Keep responses concise.
- Use markdown headings.
- Use bullet points where appropriate.
- Do NOT repeat the input sections verbatim.
- Summarize and synthesize the information.
- Do NOT invent real-time weather.
- Do NOT invent hotel prices.
- Do NOT invent flight prices.
- Do NOT invent visa rules.
- When uncertain, advise the traveler to verify current information before booking.
"""

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.4,
            },
        )

        if response.text:
            return response.text.strip()

        return _fallback_itinerary(
            info,
            hotel,
            flight,
            activity,
        )

    except Exception:
        return _fallback_itinerary(
            info,
            hotel,
            flight,
            activity,
        )


def _fallback_itinerary(
    info: str,
    hotel: str,
    flight: str,
    activity: str,
) -> str:
    """
    Build a professional fallback itinerary when Gemini is unavailable.
    """

    return f"""
# Trip Overview

An AI-generated itinerary could not be produced at this time.
The itinerary below has been assembled from the available travel
information.

## Best Time to Visit

Refer to the destination information.

## Accommodation Plan

{hotel}

## Flight Strategy

{flight}

## Daily Itinerary

### Day 1

- Arrive at your destination.
- Check into your accommodation.
- Explore nearby attractions.

### Day 2

- Visit the main attractions.
- Enjoy local cuisine.
- Experience local culture.

### Day 3

- Complete remaining activities.
- Shopping and relaxation.
- Prepare for departure.

## Food Recommendations

Refer to the destination and activities section.

## Estimated Budget Summary

Review the hotel, flight and activity recommendations for estimated expenses.

## Travel Checklist

- Passport / National ID
- Visa (if required)
- Travel Insurance
- Payment Cards
- Local Currency
- Power Adapter
- Comfortable Clothing

## Safety Notes

Follow local regulations and basic travel safety practices.

## Final Travel Tips

- Confirm bookings before departure.
- Monitor weather forecasts.
- Keep digital copies of important documents.
- Verify flight schedules before travel.

---

## Destination Information

{info}

---

## Activities

{activity}

Note:

This itinerary was generated using locally available information because
the AI itinerary generation service was temporarily unavailable.
""".strip()