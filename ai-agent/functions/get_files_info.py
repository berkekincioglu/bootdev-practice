import os


def get_files_info(working_dir: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_dir)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # if directory is not directory, return error
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # iterate over the items in the target directory. For each item, record: name, size , whether it is a directory
        # for each item record name, size , whether it is a directory

        items_info = []
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            if os.path.isdir(item_path):
                item_size = 0
            else:
                item_size = os.path.getsize(item_path)
            item_info = f"- {item}: file_size={item_size} bytes, is_dir={os.path.isdir(item_path)}"
            items_info.append(item_info)

        return "\n".join(items_info)

    except Exception as e:
        return f"Error: {e}"
