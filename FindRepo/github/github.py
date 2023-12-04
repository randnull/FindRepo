import requests
import json
import toml

from typing import List

def find_github_code(code: str, count: int) -> List[str]:
    if count <= 0:
        count = 1
        raise RuntimeWarning('Count less than zero!')

    config = toml.load('authorization.toml')
    token = config['token_github']['token']

    headers = {
        'Authorization': token
    }

    url_with_code = f'https://api.github.com/search/code?q={code}'

    response = requests.get(url_with_code, headers=headers)
    response_json = response.json()['items']

    answer_list = list()

    for answer_index in range(min(len(response_json), count)):
        answer_list.append(response_json[answer_index]['html_url'])

    return answer_list
