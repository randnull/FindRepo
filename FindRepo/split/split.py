from hash.hash import Hash

import ast
import astunparse

from typing import List

class Split:
    def __init__(self, hash_func: str, fast: bool = False):
        self.hash_class = Hash(hash_func)
        self.fast = fast

    def _split_python_code(self, code: str) -> List:
        tree = ast.parse(code)

        parts = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                parts.append(astunparse.unparse(node).strip())
        
        tree.body = [node for node in tree.body if not isinstance(node, ast.FunctionDef)]

        parts.append(astunparse.unparse(tree).strip())

        hash_list = list()

        for part in parts:
            normal_part = part.replace('\n', '')

            if normal_part == '':
                continue

            hash_list.append((normal_part, self.hash_class.hash_object(part)))

        return hash_list


    def _split_cpp_code(self, code: str) -> List:
        #Not implement
        return []


    def _split_another_code(self, code: str) -> List:
        splited_code: List = code.split('\n')
        
        words: List = list()

        for word in splited_code:
            if word != '':
                words.append(word)

        hash_list: List = list()

        for i in range(0, len(words), 3):
            part = ' '.join(words[i:i+3])

            normal_part = part.replace('\n', '')

            normal_part = normal_part.strip()

            if normal_part == '':
                continue

            hash_list.append((normal_part, self.hash_class.hash_object(part)))
        
        return hash_list


    def _split_code(self, code: str, code_lang: str) -> List:
        if code_lang == 'py':
            return self._split_python_code(code)
        if code_lang == 'cpp':
            return self._split_cpp_code(code)
        else:
            return self._split_another_code(code)

    
    def _split_text(self, text: str) -> List:
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


    def split(self, object: str, ftype: str, is_code: bool) -> List:
        if is_code:
            return self._split_code(object, ftype)
        return self._split_text(object)
