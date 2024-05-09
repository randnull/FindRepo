from typing import List


def get_whitelist() -> List:
    '''Получение whitelist'''

    with open('FindRepo/common/whitelist/code_whitelist.txt', 'r') as f:
        whitelist = [code_type for code_type in f.read().split('\n')]
        
        return whitelist
