from typing import List, Dict

import requests

from common.config.config import config


class LocalSearch:
    def __init__(self):
        pass


    def _save(self, tokens, link):
        database_host: str = config['Database']['service_host']
        database_port: str = config['Database']['service_port']
        
        add_handler: str = config['LocalSearch']['add_handler']


    def _get_similar(self, new_tokens) -> List:
        database_host: str = config['Database']['service_host']
        database_port: str = config['Database']['service_port']
        
        get_handler: str = config['LocalSearch']['add_handler']

        try:
            response = requests.get(f"{database_host}:{database_port}/{get_handler}")
        except:
            return []

        similar: List = list()

        return similar # Jaccard >=0.45


    def find(self, new_tokens: List, link: str) -> List:
        similar: List = self._get_similar(new_tokens)

        self._save(new_tokens, link)

        return similar
