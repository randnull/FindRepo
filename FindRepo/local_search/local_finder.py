from tqdm import tqdm

from colorama import init
init()
from colorama import Fore, Style

from typing import List, Dict

from common.errors.errors import *

from local_search.token_split.token_split import TokenSplit
from local_search.search.search import LocalSearch

from common.reader.reader import Reader


def local_finder(path: str) -> Dict:
    '''Поиск по базе данных'''

    reader: Reader = Reader()

    try:
        files: List = reader.read(path)
    except Exception as ErrorBadPath:
        print(Fore.RED + f'{path} не является путем до файла или директории' + Style.RESET_ALL)
        return dict(), False

    split_class: TokenSplit = TokenSplit(hash_func='md5')

    search_class: LocalSearch = LocalSearch()

    links_dict: Dict = dict()

    for file, _, file_path in tqdm(files, desc='Поиск совпадений'):
        try:
            splitted_current_code = list(split_class.split(file))
        except ErrorNotTokenize:
            continue

        find_links: List = search_class.find(splitted_current_code, file_path)

        for link in find_links:
            links_dict[link] = links_dict.get(link, 0) + 1

    return dict(sorted(links_dict.items(), key=lambda item: -item[1])), True
