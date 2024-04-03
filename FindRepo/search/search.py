from search.github.github import find_github
from search.google.google import find_google
from search.yandex.yandex import find_yandex


def find(text: str, is_code=True):
    search_functions = [('google', find_google)]

    if is_code:
        search_functions.append(('github', find_github))

    answer_list = list()

    for function in search_functions:
        results = function[1](text)
        answer_list += results


    return list(set(answer_list))


        