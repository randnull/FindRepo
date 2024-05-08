from common.hash.hash import Hash

import ast
import astunparse

from colorama import init
init()
from colorama import Fore, Back, Style

from typing import List

from common.config.config import config


class Split:
    def __init__(self, hash_func: str):
        self.hash_class = Hash(hash_func)


    def _split_another_code(self, code: str) -> List:
        '''
        Разделяет код по 5 строк
        '''

        splited_code: List = code.split('\n')
        
        words: List = list()

        for word in splited_code:
            if word != '':
                words.append(word)

        hash_list: List = list()

        split_size = int(config['Split']['split_size'])

        for i in range(0, len(words), split_size):
            part = ' '.join(words[i:i+split_size]) #проверить

            normal_part = part.replace('\n', '')

            normal_part = normal_part.strip()

            if normal_part == '':
                continue

            hash_list.append((normal_part, self.hash_class.hash_object(part)))
        
        return hash_list


    def _split_python_code(self, code: str) -> List:
        '''
        Разделяет код(python) на функции (def) и весь остальной код
        '''
        try:
            tree = ast.parse(code)
        except:
            return self._split_another_code(code)

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


    def _split_code(self, code: str, code_lang: str) -> List:
        '''
        Разделяет код на части
        '''

        if code_lang == 'py':
            return self._split_python_code(code)
        # if code_lang == 'cpp':
        #     return self._split_cpp_code(code)
        else:
            return self._split_another_code(code)


    def _split_text(self, text: str) -> List:
        '''
        Разделяет текст на части
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
        Разделяет объект на части
        '''

        if is_code:
            return self._split_code(find_object, ftype)
        return self._split_text(find_object)
