import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key="AIzaSyCOv5fyBPyvS8nHbJank75M5hT9JB9kZc8")

def get_gemini_model():
    return genai.GenerativeModel("gemini-1.5-flash")