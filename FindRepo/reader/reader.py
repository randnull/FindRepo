import os
from typing import List

class Reader:
    def __init__(self):
        pass


    def _read_file(self, path: str):
        file = open(path, 'r')

        _, file_name = os.path.split(path)
        file_type = file_name.split('.')[1]

        file_text = file.read()

        return (file_text, file_type)


    def _read_direct(self, path:str) -> List:
        #по файлам директории, и вызывать для них _read_file
        pass


    def read(self, path:str):
        return self._read_file(path)