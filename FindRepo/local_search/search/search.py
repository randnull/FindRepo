from typing import List, Dict


class LocalSearch:
    def __init__(self):
        pass


    def _get_all_tokens(self):
        return set() #БД


    def _get_similar(self, new_tokens) -> List:
        all_tokens = self._get_all_tokens()

        # results: Dict = dict()

        # for token in all_tokens:
        #     len_intersect_tokens: int = len(token.intersection(new_tokens))
        #     len_union_tokens: int = len(token.union(new_tokens))

        #     results

        similar: List = list()

        return similar # Добавление при Jaccard >=0.45


    def find(self, new_tokens: List) -> List:
        return self._get_similar(new_tokens)
