import requests
import json
import toml

import functools

from typing import List


@functools.lru_cache(maxsize=10000)
def find_github(code: str) -> List[str]:
    print('Поиск: Github')
    
    # config = toml.load('authorization.toml')
    # token = config['token_github']['token']

    # headers = {
    #     'Authorization': token
    # }

    # url_with_code = f'https://api.github.com/search/code?q={code}'
    # response = requests.get(url_with_code, headers=headers)
    # try:
    #     response_json = response.json()['items']
    # except:
    #     return []

    # answer_list = list()

    # for answer_index in range(len(response_json)):
    #     answer_list.append(response_json[answer_index]['html_url'])

    # return answer_list
    return []
