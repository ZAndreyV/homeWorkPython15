import os
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_folder'])


def get_directory_content_info(directory_path):
    content_info = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(item_path)
        name, extension = os.path.splitext(item)
        if is_directory:
            content_info.append(FileInfo(name, None, True, directory_path))
        else:
            content_info.append(FileInfo(name, extension[1:], False, directory_path))

    return content_info


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process directory path')
    parser.add_argument('directory_path', type=str, help='directory path')
    args = parser.parse_args()
    directory_content_info = get_directory_content_info(args.directory_path)
    for info in directory_content_info:
        print(info)