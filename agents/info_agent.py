from tools.info_tools import get_info


def travel_info(destination):

    info = get_info(destination)

    return f"""
Destination: {info['destination']}

Best Time to Visit:
{info['best_time']}

Currency:
{info['currency']}

Language:
{info['language']}

Famous Places:
{', '.join(info['places'])}
"""