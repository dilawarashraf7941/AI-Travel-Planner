from utils import get_model

model = get_model()


def planner(user_request):

    prompt = f"""
    You are an intelligent travel planner.

    Analyze the user's request carefully.

    User Request:

    {user_request}

    Answer ONLY in this format.

    Need Info: Yes/No
    Need Hotel: Yes/No
    Need Flight: Yes/No
    Need Activity: Yes/No
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Planner Error: {e}"