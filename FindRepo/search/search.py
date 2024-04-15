from search.github.github import find_github
from search.google.google import find_google
from search.yandex.yandex import find_yandex


class Searcher:
    def __init__(self):
        pass

    def _check_hash(self, hash: str):
        pass

    def _find_serp(self, object: str):
        pass
        # search_functions = [('google', find_google)]

        # if is_code:
        #     search_functions.append(('github', find_github))

        # answer_list = list()

        # for function in search_functions:
        #     results = function[1](text)
        #     answer_list += results


        # return list(set(answer_list))

    def find(self, text: str, is_code=True):
        pass
