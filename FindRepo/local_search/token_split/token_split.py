import tokenize
from io import BytesIO

from common.hash.hash import Hash

from typing import List

from common.errors.errors import *

from common.config.config import config


class TokenSplit:
    def __init__(self, hash_func: str):
        self.hash_class = Hash(hash_func)


    def _tokenize_code(self, code: str) -> List:
        '''Токенизация кода'''

        tokens: List = list()

        for toknum in tokenize.tokenize(BytesIO(code.encode('utf-8')).readline):
            if toknum.string.strip():
                tokens.append(toknum.string)

        return tokens


    def _get_shingles(self, tokens: List, shingle_size: int):
        '''Разбиение алгоритмом шилингов'''

        shingles = set()

        for i in range(len(tokens) - shingle_size + 1):
            shingle = " ".join(tokens[i:i + shingle_size])

            shingles.add(self.hash_class.hash_object(shingle))

        return shingles

    
    def split(self, code: str):
        '''Разделение кода на части'''
        
        try:
            tokens: List = self._tokenize_code(code)

            shingle_size: int = int(config['TokenSplit']['shingle_size'])

            shingles = self._get_shingles(tokens, shingle_size)
        except:
            raise ErrorNotTokenize

        return shingles
