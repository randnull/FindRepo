from hash.hash import Hash

import ast
import astunparse

from typing import List

class Split:
    def __init__(self):
        self.hash_class = Hash()

    def split_code(self, code: str) -> List:
        tree = ast.parse(code)

        parts = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                parts.append(astunparse.unparse(node).strip())
        
        tree.body = [node for node in tree.body if not isinstance(node, ast.FunctionDef)]

        parts.append(astunparse.unparse(tree).strip())

        hash_list = list()

        for part in parts:
            hash_list.append((part, self.hash_class.hash_object(part)))

        return hash_list