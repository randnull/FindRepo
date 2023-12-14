import requests
import json
import toml

from typing import List

def find_gitlab_code(code: str, count: int = 5) -> List[str]:
    if count <= 0:
        raise RuntimeError('Count less than zero!')

    config = toml.load('authorization.toml')
    token = config['token_gitlab']['token']

    headers = {
        "PRIVATE-TOKEN": token
     }

    url_with_code = f'https://gitlab.com/api/v4/search?scope=projects&search={code}'
    response = requests.get(url_with_code, headers=headers)
    response_json = response.json()

    answer_list = list()

    for answer_index in range(min(len(response_json), count)):
        answer_list.append(response_json[answer_index]['web_url'])

    return answer_list
