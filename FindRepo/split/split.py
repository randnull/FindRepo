from hash.hash import Hash

import ast
import astunparse

from colorama import init
init()
from colorama import Fore, Back, Style

from typing import List


class Split:
    def __init__(self, hash_func: str, fast: bool = False):
        self.hash_class = Hash(hash_func)
        self.fast = fast


    def _split_python_code(self, code: str) -> List:
        '''
        Разделяет код на функции (def) и весь остальной код

        :param code: код на python в формате str

        :return: list с структурой (часть кода, хэш части кода)
        '''

        tree = ast.parse(code)

        parts: List = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                parts.append(astunparse.unparse(node).strip())
        
        tree.body: List = [node for node in tree.body if not (isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef))]

        parts.append(astunparse.unparse(tree).strip())

        hash_list: List = list()

        for part in parts:
            normal_part: str = part.replace('\n', '')

            if normal_part == '':
                continue

            hash_list.append((normal_part, self.hash_class.hash_object(part)))

        return hash_list


    def _split_cpp_code(self, code: str) -> List:
        #Not implement
        return []


    def _split_another_code(self, code: str) -> List:
        '''
        Разделяет код по 5 строк

        :param code: код в формате str

        :return: list с структурой (часть кода, хэш части кода)
        '''

        splited_code: List = code.split('\n')
        
        words: List = list()

        for word in splited_code:
            if word != '':
                words.append(word)

        hash_list: List = list()

        for i in range(0, len(words), 5):
            part = ' '.join(words[i:i+5])

            normal_part = part.replace('\n', '')

            normal_part = normal_part.strip()

            if normal_part == '':
                continue

            hash_list.append((normal_part, self.hash_class.hash_object(part)))
        
        return hash_list


    def _split_code(self, code: str, code_lang: str) -> List:
        '''
        Разделяет код на части

        :param code: код в формате str
        :param code_lang: язык программирования

        :return: list с структурой (часть код, хэш части кода)
        '''

        if code_lang == 'py':
            return self._split_python_code(code)
        if code_lang == 'cpp':
            return self._split_cpp_code(code)
        else:
            return self._split_another_code(code)

    
    def _split_text(self, text: str) -> List:
        '''
        Разделяет текст на части

        :param text: текст в формате str

        :return: list с структурой (часть текста, хэш части текста)
        '''

        splited_text: List = text.split('.')
        
        hash_list: List = list()

        for i in range(0, len(splited_text)):
            part = splited_text[i]

            normal_part = part.replace('\n', '')

            normal_part = normal_part.strip()

            if normal_part == '':
                continue

            hash_list.append((normal_part, self.hash_class.hash_object(part)))
        
        return hash_list


    def split(self, find_object: str, ftype: str, is_code: bool) -> List:
        '''
        Разделяет текст на части

        :param find_object: объект в формате str
        :param ftype: тип файла
        :param is_code: является ли объект кодом

        :return: list с структурой (часть объекта, хэш части объекта)
        '''

        if is_code:
            return self._split_code(find_object, ftype)
        return self._split_text(find_object)
