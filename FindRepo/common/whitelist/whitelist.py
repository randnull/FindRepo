from typing import List


def get_code_whitelist() -> List:
    '''Получение whitelist'''

    with open('FindRepo/common/whitelist/code_whitelist.txt', 'r') as f:
        whitelist = [code_type for code_type in f.read().split('\n')]
        
        return whitelist


def get_whitelist() -> List:
    '''Получение whitelist'''

    with open('FindRepo/common/whitelist/code_whitelist.txt', 'r') as f:
        whitelist_code = [code_type for code_type in f.read().split('\n')]
    
    with open('FindRepo/common/whitelist/text_whitelist.txt', 'r') as f:
        whitelist_text = [text_type for text_type in f.read().split('\n')]
    
    return whitelist_code + whitelist_text
