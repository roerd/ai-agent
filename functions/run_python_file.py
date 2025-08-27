import subprocess
from pathlib import Path

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    wd_path = Path(working_directory)
    full_path = (wd_path / file_path).resolve()
    if args is None:
        args = []

    if not full_path.is_relative_to(wd_path.resolve()):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not full_path.exists():
        return f'Error: File "{file_path}" not found.'

    if not full_path.suffix == '.py':
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(['uv', 'run', str(full_path)] + args, cwd=wd_path, capture_output=True, timeout=30)
        output = []
        if completed_process.stdout:
            output.append('STDOUT:' + completed_process.stdout.decode("utf-8"))
        if completed_process.stderr:
            output.append('STDERR:' + completed_process.stderr.decode("utf-8"))
        if not output:
            output.append("No output produced.")
        if completed_process.returncode != 0:
            output.append(f'Process exited with code {completed_process.returncode}')
        return '\n'.join(output)
    except subprocess.SubprocessError as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute the specified Python file with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The arguments to be passed to the Python file. If not provided, execute the Python file with no arguments.",
            ),
        },
    ),
)