import os
import json

from typing import List


class Reader:
    def __init__(self):
        pass


    def _check_cache_files(self, path: str) -> bool:
        pass


    def _check_file_type(self, path: str) -> str:
        try:
            _, file_name = os.path.split(path)
            file_type = file_name.split('.')[1]
        except:
            return "None"
            
        return file_type


    def _parse_ipynb(self, file: str) -> str:
        file_text: str = ""

        json_format = json.loads(file)

        for cell in json_format['cells']:
            if cell['cell_type'] == 'code':
                file_text += ''.join(cell['source'])

        return file_text


    def _read_file(self, path: str):
        try:
            with open(path, 'r') as f:
                file_text: str = f.read()
        except:
            return ("", "")

        file_type: str = self._check_file_type(path)

        if file_type == 'ipynb':
            file_text = self._parse_ipynb(file_text)
            file_type = 'py'

        return (file_text, file_type)


    def _read_direct(self, path: str) -> List:
        files_texts: List = list()

        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)

                file_text, file_type = self._read_file(file_path)
                
                if not file_text or not file_type:
                    continue

                files_texts.append(self._read_file(file_path))

        return files_texts


    def read(self, path: str) -> List:
        if os.path.isdir(path):
            return self._read_direct(path)
        else:
            return [self._read_file(path)]
