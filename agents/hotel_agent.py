from tools.hotel_tools import get_hotels


def hotel_info(destination):

    hotels = get_hotels(destination)

    return f"""
Luxury Hotel:
Name: {hotels['luxury']['name']}
Price: {hotels['luxury']['price']}

Mid-Range Hotel:
Name: {hotels['mid_range']['name']}
Price: {hotels['mid_range']['price']}

Budget Hotel:
Name: {hotels['budget']['name']}
Price: {hotels['budget']['price']}
"""