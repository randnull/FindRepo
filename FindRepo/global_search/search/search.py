from typing import List

from global_search.search.github.github import find_github
from global_search.search.google.google import find_google

from common.formatter.formatter import FormatterPerRequest

from global_search.database_requests.requests import add_global, get_global


class Searcher:
    def __init__(self, is_code = True):
        self.formatter_class = FormatterPerRequest()

        self.search_functions: List = [('google', find_google)]

        if is_code:
            self.search_functions.append(('github', find_github))


    def _check_hash(self, hash: str):
        return get_global(hash)


    def _save_hash(self, hash: str, links: List):
        add_global(hash, links)


    def _find_serp(self, find_body: str) -> List:
        '''
        Поиск по части кода в доступных сторонних источниках
        '''

        formatted_body: str = self.formatter_class.format(find_body)

        links = set()

        for function in self.search_functions:
            results = function[1](formatted_body)
            
            for link in results:
                links.add(link)

        return list(links)


    def find(self, find_object: str) -> List:
        '''
        Поиск по части кода в доступных источниках (БД или сторонние ресурсы)
        '''

        body: str = find_object[0]
        body_hash: str = find_object[1]

        db_result = self._check_hash(body_hash)

        if db_result != []:
            return db_result
        
        links: List = self._find_serp(body)

        if links != []:
            self._save_hash(body_hash, links)

        return links
