import os
import requests
from dotenv import load_dotenv

load_dotenv()
ZEROGPT_API_KEY = os.getenv("ZEROGPT_API_KEY")  # This is your RapidAPI key
ZEROGPT_API_URL = "https://zerogpt.p.rapidapi.com/api/v1/detectText"


def is_ai_written(text):
    try:
        headers = {
            "Content-Type": "application/json",
            "X-RapidAPI-Key": ZEROGPT_API_KEY,
            "X-RapidAPI-Host": "zerogpt.p.rapidapi.com"
        }
        data = {"input_text": text}
        response = requests.post(ZEROGPT_API_URL, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        # According to docs, is_gpt_generated is a percentage (0-100)
        is_gpt_generated = result.get("data", {}).get("is_gpt_generated", 0)
        # Consider AI-written if more than 50%
        return is_gpt_generated > 50
    except Exception as e:
        print(f"ZeroGPT Error: {e}")
        return None 