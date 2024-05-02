import hashlib
import ast
from changer.changer import ASTChanger


class Hash:
    def __init__(self, hash_func: str = 'md5'):
        if hash_func == 'md5':
            self.hash_func = hashlib.md5


    def hash_object(self, object: str):
        tree = ast.parse(object)

        changer = ASTChanger()
        tree = changer.visit(tree)

        encoded_object = object.encode()

        hash_object = self.hash_func(encoded_object)

        hex_hash = hash_object.hexdigest()

        return hex_hash
