from typing import List

import requests
import json

from common.config.config import config


def add_global(hash, links: List) -> None:
    database_host: str = config['Database']['service_host']
    database_port: str = config['Database']['service_port']

    add_handler: str = config['GlobalSearch']['add_handler']

    request_link = f"http://{database_host}{database_port}{add_handler}"

    json_dict = json.dumps({"hash": hash, "links": links})

    try:
        requests.post(request_link, data=json_dict)
    except:
        pass


def get_global(hash: str) -> List:
    database_host: str = config['Database']['service_host']
    database_port: str = config['Database']['service_port']

    get_handler: str = config['GlobalSearch']['get_handler'] + hash

    request_link = f"http://{database_host}{database_port}{get_handler}"

    try:
        response = requests.get(request_link)

        if response.status_code != 200:
            return []

        json_answer = response.json()

        links: List = json_answer['links']

        return links
    except:
        return []
