import requests
import json
import toml

import functools

from typing import List


forbidden_char = ['"', '@']


def filter_code(code: str) -> str:
    for ch in forbidden_char:
        code = code.replace(ch, '')
    return code


@functools.lru_cache(maxsize=10000)
def find_github(code: str) -> List[str]:
    config = toml.load('authorization.toml')
    token = config['token_github']['token']

    headers = {
        'Authorization': token
    }
    # forbidden_char = ['"', '@']
    code_to_request = filter_code(code)

    url_with_code = f'https://api.github.com/search/code?q={code_to_request}'

    try:
        response = requests.get(url_with_code, headers=headers)
    except:
        return list()

    try:
        response_json = response.json()['items']
    except Exception as ex:
        return []

    answer_list = list()

    for answer_index in range(len(response_json)):
        answer_list.append(response_json[answer_index]['html_url'])

    return answer_list
