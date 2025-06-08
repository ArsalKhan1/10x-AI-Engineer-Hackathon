import sys
from openai_utils import generate_linkedin_post, humanize_post, openai_detect_ai
# from zerogpt_utils import is_ai_written  # No longer needed

def main():
    print("Welcome to the Linkedin Human Post Writer!")
    user_prompt = input("Enter what you want your LinkedIn post to be about: ")

    post = generate_linkedin_post(user_prompt)
    if not post:
        print("Failed to generate post. Exiting.")
        sys.exit(1)

    max_attempts = 3
    attempt = 0
    while attempt < max_attempts:
        print(f"\nAttempt {attempt+1}: Checking if the post sounds AI-written (using OpenAI)...")
        ai_result = openai_detect_ai(post)
        if ai_result is None:
            print("Error checking with OpenAI. Exiting.")
            sys.exit(1)
        print(f"Detection result: {ai_result}")
        if ai_result.strip().lower().startswith('ai') is False:
            print("\nYour LinkedIn post is ready and sounds human:")
            print("-"*50)
            print(post)
            print("-"*50)
            return
        print("OpenAI detected AI writing. Humanizing the post...")
        post = humanize_post(post)
        if not post:
            print("Failed to humanize post. Exiting.")
            sys.exit(1)
        attempt += 1

    print("\nMax attempts reached. Here is the best version of your post:")
    print("-"*50)
    print(post)
    print("-"*50)

if __name__ == "__main__":
    main() 