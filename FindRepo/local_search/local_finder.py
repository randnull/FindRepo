from tqdm import tqdm

from colorama import init
init()
from colorama import Fore, Style

from typing import List, Dict

from common.errors.errors import *

from common.whitelist.whitelist import get_whitelist
from local_search.split.split import TokenSplit
from local_search.search.search import LocalSearch

from common.reader.reader import Reader


def local_finder(link: str):
    reader: Reader = Reader()

    try:
        files: List = reader.read(link)
    except Exception as ErrorBadPath:
        print(Fore.RED + f'{link} не является путем до файла или директории' + Style.RESET_ALL)
        return

    split_class: TokenSplit = TokenSplit(hash_func='md5')
    search_class: LocalSearch = LocalSearch()

    # links_dict: Dict = dict()

    for file, _ in tqdm(files, desc='Поиск совпадений'):
        try:
            splitted_current_code: str = split_class.split(file)
        except ErrorNotTokenize:
            continue

        result: List = search_class.find(splitted_current_code)