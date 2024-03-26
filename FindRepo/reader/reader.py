import os


def read_file(path: str):
    file = open(path, 'r')

    _, file_name = os.path.split(path)
    file_type = file_name.split('.')[1]

    file_text = file.read()

    return (file_text, file_type)
