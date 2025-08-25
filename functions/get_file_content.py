from pathlib import Path

from config import max_file_size


def get_file_content(working_directory, file_path):
    wd_path = Path(working_directory)
    full_path = (wd_path / file_path).resolve()

    if not full_path.is_relative_to(wd_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not full_path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        content = full_path.read_text()
        if len(content) > max_file_size:
            content = content[:max_file_size] + f'[...File "{file_path}" truncated at 10000 characters]'
        return content
    except OSError as e:
        return f'Error: {e}'
