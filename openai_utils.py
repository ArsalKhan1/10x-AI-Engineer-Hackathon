import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_linkedin_post(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes engaging LinkedIn posts."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return None

def humanize_post(post):
    try:
        prompt = (
            "Rewrite the following LinkedIn post to sound more human, natural, and personal. "
            "Use a conversational tone, contractions, and add a touch of personality. Avoid sounding like AI.\n\n" + post
        )
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that rewrites text to sound more human and less AI-generated."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.8
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return None

def openai_detect_ai(text):
    prompt = (
        "Analyze the following text and tell me if it is likely written by an AI or a human. "
        "Respond with 'AI', 'Human', or 'Uncertain', and provide a brief reason.\n\n"
        f"Text:\n{text}"
    )
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert at detecting AI-generated text."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return None 