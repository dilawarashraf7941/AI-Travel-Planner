from tools.flight_tools import get_flights


def flight_info(destination):

    flight = get_flights(destination)

    return f"""
Airline:
Name: {flight['airline']['name']}

Estimated Ticket Price:
{flight['airline']['price']}

Flight Duration:
{flight['airline']['duration']}

Travel Tips:
- Reach the airport at least 2 hours before departure.
- Keep your CNIC/Passport with you.
- Confirm baggage allowance before traveling.
"""