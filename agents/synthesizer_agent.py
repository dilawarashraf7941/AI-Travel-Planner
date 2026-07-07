from utils import get_model

model = get_model()


def create_itinerary(info, hotel, flight, activity):

    prompt = f"""
You are an expert AI Travel Planner.

Using the following information, create a complete and professional travel itinerary.

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

Instructions:
1. Create a beautiful travel itinerary.
2. Use proper headings.
3. Recommend the best hotel.
4. Mention flight details.
5. Include famous attractions.
6. Include local foods.
7. Add estimated budget.
8. Add useful travel tips.
9. Make the response clean and professional.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:

        # Fallback Itinerary
        return f"""
==============================
        TRAVEL ITINERARY
==============================

Destination Information
------------------------
{info}

Hotel Information
-----------------
{hotel}

Flight Information
------------------
{flight}

Activities
----------
{activity}

Estimated Budget
----------------
PKR 40,000 - 70,000

Travel Tips
-----------
• Carry your CNIC/Passport.
• Book hotels in advance.
• Keep cash for local shopping.
• Check the weather before travelling.

Note:
AI itinerary could not be generated because the Gemini API quota has been exceeded.
The above itinerary was generated using locally available travel information.
"""