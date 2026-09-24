import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_file_path = (
            os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs
        )

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", file_path_abs]

        if args:
            command.extend(args)

        completed = subprocess.run(
            command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30
        )

        parts = []

        if completed.returncode != 0:
            parts.append(f"Process exited with code {completed.returncode}")

        if completed.stdout:
            parts.append(f"STDOUT:\n{completed.stdout}")

        if completed.stderr:
            parts.append(f"STDERR:\n{completed.stderr}")

        if not completed.stdout and not completed.stderr:
            parts.append("No output produced")

        return "\n".join(parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
