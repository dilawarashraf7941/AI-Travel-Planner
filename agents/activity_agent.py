from tools.activity_tools import get_activities


def activity_info(destination):

    activities = get_activities(destination)

    return f"""
Famous Tourist Attractions:
{', '.join(activities['places'])}

Local Foods:
{', '.join(activities['food'])}

Estimated Cost:
PKR 5,000 - 15,000 per day

Recommended Activities:
- Sightseeing
- Photography
- Local Food Tasting
- Shopping
"""