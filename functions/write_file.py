from pathlib import Path

from google.genai import types


def write_file(working_directory, file_path, content):
    wd_path = Path(working_directory)
    full_path = (wd_path / file_path).resolve()

    if not full_path.is_relative_to(wd_path.resolve()):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        # This will either create a new file or overwrite an existing file, depending on whether it already exists.
        full_path.write_text(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except OSError as e:
        return f'Error: {e}'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite file at the specified file path with the specified content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to be written or overwritten, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the file.",
            ),
        },
    ),
)