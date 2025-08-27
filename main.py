import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt> [--verbose]")
        sys.exit(1)

    user_prompt = sys.argv[1]
    verbose = len(sys.argv) > 2 and sys.argv[2] == "--verbose"

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    if verbose:
        print("User prompt:", user_prompt)
        usage_metadata = response.usage_metadata
        print("Prompt tokens:", usage_metadata.prompt_token_count)
        print("Response tokens:", usage_metadata.candidates_token_count)

    print("Response:", response.text)
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")


if __name__ == "__main__":
    main()
