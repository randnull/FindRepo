from typing import List, Dict

import requests
import json

from local_search.database_requests.requests import get_local, add_local

from common.config.config import config


class LocalSearch:
    def __init__(self) -> None:
        pass


    def _save(self, tokens: List, link: str) -> None:
        add_local(tokens, link)


    def _get_similar(self, new_tokens: List) -> List:
        return get_local(new_tokens)


    def find(self, new_tokens: List, link: str) -> List:
        similar: List = self._get_similar(new_tokens)

        self._save(new_tokens, link)

        return similar
