import os

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_file_path = (
            os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs
        )
        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # If the file_path is not a file, again, return an error string:

        if not os.path.isfile(file_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file_path_abs, "r") as f:
            content = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return content
    except Exception as e:
        return f"Error: {e}"
