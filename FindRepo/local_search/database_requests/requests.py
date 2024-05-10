from typing import List, Dict

import requests
import json

from common.config.config import config


def add_local(hashes: List, link: str) -> None:
    database_host: str = config['Database']['service_host']
    database_port: str = config['Database']['service_port']

    add_handler: str = config['LocalSearch']['add_handler']

    request_link = f"http://{database_host}{database_port}{add_handler}"

    json_dict = json.dumps({"hashes": hashes, "link": link})

    try:
        requests.post(request_link, data=json_dict)
    except:
        pass


def get_local(hashes: List) -> List:
    database_host: str = config['Database']['service_host']
    database_port: str = config['Database']['service_port']

    get_handler: str = config['LocalSearch']['get_handler']

    request_link = f"http://{database_host}{database_port}{get_handler}"

    json_data = json.dumps(hashes)

    try:
        response = requests.post(request_link, data=json_data)

        if response.status_code != 200:
            return []

        response_json = response.json()

        similar: Dict = dict()

        for index, link in enumerate(response_json[0]):
            similar[link['link']] = response_json[1][index]

        return similar
    except:
        return []
