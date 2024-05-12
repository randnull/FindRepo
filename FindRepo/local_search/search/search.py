from typing import List, Dict

from local_search.database_requests.requests import get_local

from common.config.config import config


class LocalSearch:
    def __init__(self) -> None:
        self.max_jaccard_score = float(config['LocalSearch']['jaccard_score'])

        self.__value_to_save: List = list()


    def _get_similar(self, new_tokens: List) -> List:
        return get_local(new_tokens)

    
    def get_value_to_save(self):
        return self.__value_to_save


    def find(self, new_tokens: List, link: str) -> Dict:
        similar: Dict = self._get_similar(new_tokens)

        if ((len(similar) == 0) or (max(similar.values()) < self.max_jaccard_score)):
            self.__value_to_save.append(new_tokens)

        return similar
