from typing import List

from search.github.github import find_github
from search.google.google import find_google
from search.yandex.yandex import find_yandex


class Searcher:
    def __init__(self, is_code):
        #self.search_functions: List = [('google', find_google)]
        self.search_functions = []

        if is_code:
            self.search_functions.append(('github', find_github))


    def _check_hash(self, hash: str) -> (List, bool): #в БД реп
        return [], False


    def _find_serp(self, find_body: str) -> List:
        links = set()
        
        for function in self.search_functions:
            results = function[1](find_body)
            
            for link in links:
                links.add(link)

        return list(links)

    def find(self, find_object: str):
        body: str = find_object[0]
        body_hash: str = find_object[1]

        db_result, is_find = self._check_hash(body_hash)

        if is_find:
            return db_result
        
        links: List = self._find_serp(body)

        print(links)

        #ADD TO DB (body_hash, links)

        return links
