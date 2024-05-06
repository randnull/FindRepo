from typing import List

from global_search.search.github.github import find_github
from global_search.search.google.google import find_google
# from search.yandex.yandex import find_yandex


class Searcher:
    def __init__(self, is_code):
        self.search_functions: List = [('google', find_google)]
        # self.search_functions = []

        # if is_code:
        #     self.search_functions.append(('github', find_github))


    def _check_hash(self, hash: str): #в БД реп
        return [], False


    def _find_serp(self, find_body: str) -> List:
        '''
        Поиск по части кода в доступных сторонних источниках
        '''

        links = set()

        for function in self.search_functions:
            results = function[1](find_body)
            
            for link in results:
                links.add(link)

        return list(links)


    def find(self, find_object: str) -> List:
        '''
        Поиск по части кода в доступных источниках (БД или сторонние ресурсы)
        '''

        body: str = find_object[0]
        body_hash: str = find_object[1]

        db_result, is_find = self._check_hash(body_hash)

        if is_find:
            return db_result
        
        links: List = self._find_serp(body)

        return links
