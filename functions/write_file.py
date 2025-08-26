from pathlib import Path


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
