import os
import codecs


def has_no_bom(project_path, directories_to_skip, *args, **kwargs):
    for root, dirs, filenames in os.walk(project_path):
        dirs[:] = [
            d for d in dirs
            if d not in directories_to_skip
        ]
        for name in filenames:
            with open(os.path.join(root, name), 'rb') as file_handle:
                file_content = file_handle.read()
                if file_content.startswith(codecs.BOM_UTF8):
                    return 'has_bom', name
