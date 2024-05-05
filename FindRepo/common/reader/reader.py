import os
import json

from colorama import init
init()
from colorama import Fore, Style

from typing import List

from common.errors.errors import ErrorBadPath


class Reader:
    def __init__(self, types: List = None):
        if types is None:
            self.is_types = False
        else:
            self.is_types = True
            self.types = types


    def _check_file_type(self, path: str) -> str | None:
        '''
        Определяет формат файла по пути до него

        :param path: путь к файлу в формате str

        :return: расширение файла (.py, .cpp, ...) или None
        '''

        try:
            _, file_name = os.path.split(path)
            file_type = file_name.split('.')[1]
        except:
            return None

        if self.is_types and not (file_type in self.types):
            return None
        
        return file_type


    def _parse_ipynb(self, file: str) -> str:
        '''
        Выделяет из .ipynb только часть с кодом, пропуская все другие элементы

        :param file: Изначальный текст .ipynb

        :return: часть с кодом в формате str
        '''

        file_text: str = ""

        json_format = json.loads(file)

        for cell in json_format['cells']:
            if cell['cell_type'] == 'code':
                file_text += ''.join(cell['source'])

        return file_text


    def _read_file(self, path: str):
        '''
        Считывает файл по пути

        :param path: путь к файлу в формате str

        :return: текст файла и тип файла
        '''

        try:
            with open(path, 'r') as f:
                file_text: str = f.read()
        except:
            return (None, None)

        file_type: str = self._check_file_type(path)

        if file_type is None:
            return (None, None)

        if file_type == 'ipynb':
            file_text = self._parse_ipynb(file_text)
            file_type = 'py'

        return (file_text, file_type)


    def _read_direct(self, path: str) -> List:
        '''
        Считывает все файлы в директории по пути

        :param path: путь к директории в формате str

        :return: list с считанными результатами по каждому файлу
        '''

        files_texts: List = list()

        for root, _, files in os.walk(path):
            for file in files:

                file_path = os.path.join(root, file)
                
                file_text, file_type = self._read_file(file_path)

                if not file_text or not file_type:
                    continue
                    
                files_texts.append((file_text, file_type))
                
                print(Fore.GREEN + f'Добавлено: {file}' + Style.RESET_ALL)

        return files_texts


    def read(self, path: str) -> List:
        '''
        Считывает все файлы по пути

        :param path: путь к объекту в формате str

        :return: list с считанными результатами по каждому файлу
        '''

        if os.path.isdir(path):
            return self._read_direct(path)
        elif os.path.isfile(path):
            print(Fore.GREEN + f'Добавлено: {path}' + Style.RESET_ALL)

            return [(self._read_file(path))]

        raise ErrorBadPath
