import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

    user_prompt = sys.argv[1]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(model=model, contents=messages)
    print(response.text)

    usage_metadata = response.usage_metadata
    print("Prompt tokens:", usage_metadata.prompt_token_count)
    print("Response tokens:", usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
