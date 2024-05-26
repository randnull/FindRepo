from tqdm import tqdm

from colorama import init
init()
from colorama import Fore, Style

from typing import List, Dict

from common.errors.errors import *

from local_search.database_requests.requests import add_local
from common.formatter.formatter import FormatterPerHash

from local_search.token_split.token_split import TokenSplit
from local_search.search.search import LocalSearch

from common.reader.reader import Reader


def local_finder(path: str):
    '''Поиск по базе данных'''

    reader: Reader = Reader()

    try:
        files: List = reader.read(path)
    except ErrorBadPath:
        print(Fore.RED + f'{path} не является путем до файла или директории' + Style.RESET_ALL)
        return dict(), False, dict()
    except ErrorNoFileToSearch:
        print(Fore.RED + f'по пути: {path} не найдены файлы' + Style.RESET_ALL)
        return dict(), False, dict()

    split_class: TokenSplit = TokenSplit(hash_func='md5')

    search_class: LocalSearch = LocalSearch()

    # formatter = FormatterPerHash()

    links_dict: Dict = dict()
    count_dict: Dict = dict()

    for file, _, file_path in tqdm(files, desc='Поиск совпадений'):
        try:
            # file = formatter(file)
            splitted_current_code: List = list(split_class.split(file))
        except ErrorNotTokenize:
            continue
        
        find_links: Dict = search_class.find(splitted_current_code, file_path)

        for link in find_links:
            links_dict[link] = links_dict.get(link, 0) + find_links[link]
            count_dict[link] = count_dict.get(link, 0) + 1

    for link in links_dict:
        links_dict[link] /= count_dict[link]

    value_to_save = search_class.get_value_to_save()

    return dict(sorted(links_dict.items(), key=lambda item: -item[1])), True, value_to_save


def save_results(path: str, source: str, values_to_save: List) -> None:
    if values_to_save is None:
        return

    if source is None:
        source = path

    for value_to_save in values_to_save:
        add_local(value_to_save, source)
