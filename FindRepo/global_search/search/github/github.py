import requests
import json
import toml

import functools

from typing import List

from common.config.config import config

from common.formatter.formatter import FormatterPerRequest


forbidden_char = ['"', '@']


@functools.lru_cache(maxsize=10000)
def find_github(code: str) -> List[str]:
    '''Поиск по github'''

    toml_config = toml.load('FindRepo/auth/authorization.toml')
    token = toml_config['token_github']['token']

    headers = {
        'Authorization': token
    }

    code_to_request = FormatterPerRequest.delete_forbidden_char(code, forbidden_char)
    
    api_link: str = config['GlobalSearch']['github_api_link']

    url_with_code = f'{api_link}={code_to_request}'

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
