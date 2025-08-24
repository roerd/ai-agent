import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(full_path)

    if not abs_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'

    try:
        files = os.listdir(abs_path)
        files = [(file, os.path.join(abs_path, file)) for file in files]
        file_descriptions = [
            f' - {file} file_size={os.path.getsize(file_abspath)} bytes, is_dir={os.path.isdir(file_abspath)}'
            for file, file_abspath in files
        ]
        return '\n'.join(file_descriptions)
    except OSError as e:
        return f'Error: {e}'
