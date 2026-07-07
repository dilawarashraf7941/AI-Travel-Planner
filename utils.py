import google.generativeai as genai

from config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)


def get_model():

    return genai.GenerativeModel(MODEL_NAME)