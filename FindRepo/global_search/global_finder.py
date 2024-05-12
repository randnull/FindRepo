from tqdm import tqdm

from random import sample

from common.reader.reader import Reader
from global_search.search.search import Searcher
from global_search.split.split import Split

from colorama import init
init()
from colorama import Fore, Style

from common.config.config import config

from common.errors.errors import *

from typing import List, Dict

from common.whitelist.whitelist import get_whitelist, get_code_whitelist


def global_finder(path: str, github_flag: bool, fast_flag: bool) -> Dict:
    '''Поиск по сторонним источникам'''

    ALLOWED_TYPES: List = get_whitelist()

    CODE_TYPES: List = get_code_whitelist()

    reader: Reader = Reader(types=ALLOWED_TYPES)

    try:
        files: List = reader.read(path)
    except ErrorBadPath:
        print(Fore.RED + f'{path} не является путем до файла или директории' + Style.RESET_ALL)
        return dict(), False
    except ErrorNoFileToSearch:
        print(Fore.RED + f'Путь {path} не содержит ни одного доступного файла' + Style.RESET_ALL)
        return dict(), False

    split_class: Split = Split(hash_func='md5')

    splited: List = list()

    for file, ftype, _ in tqdm(files, desc='Деление объекта'):
        is_code: bool = ftype in CODE_TYPES

        splited += split_class.split(file, ftype, is_code)

    links_dict: Dict = dict()

    if fast_flag:
        fast_sample_size: str = config["GlobalSearch"]["fast_sample_size"]
        if len(splited) > int(fast_sample_size):
            splited: List = sample(splited, int(fast_sample_size))

    searcher_class: Searcher = Searcher(github_flag)

    for part in tqdm(splited, desc='Поиск совпадений'):
        links: List = searcher_class.find(part)

        for link in links:
            links_dict[link] = links_dict.get(link, 0) + 1

    return dict(sorted(links_dict.items(), key=lambda item: -item[1])), True
