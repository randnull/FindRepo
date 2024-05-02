from tqdm import tqdm
# from progress.bar import IncrementalBar

# from argpars.parser import parser
from reader.reader import Reader
from search.search import Searcher
from split.split import Split
from colorama import init
init()
from colorama import Fore, Style
from errors.errors import *
from typing import List, Dict
from whitelist.whitelist import get_whitelist


def finder(link: str, fast: bool):
    CODE_TYPES: List = get_whitelist()

    reader: Reader = Reader(types=CODE_TYPES)

    try:
        files: List = reader.read(link)
    except Exception as ErrorBadPath:
        print(Fore.RED + f'{link} не является путем до файла или директории' + Style.RESET_ALL)
        return

    split_class: Split = Split(hash_func='md5')

    splited: List = list()

    for file, ftype in tqdm(files, desc='Деление объекта'):
        is_code: bool = ftype in CODE_TYPES

        splited += split_class.split(file, ftype, is_code)

    links_dict: Dict = dict()

    for part in tqdm(splited, desc='Поиск совпадений'):
        searcher_class: Searcher = Searcher(is_code=is_code)

        links: List = searcher_class.find(part)

        for link in links:
            links_dict[link] = links_dict.get(link, 0) + 1

    for link in dict(sorted(links_dict.items(), key=lambda item: -item[1])):
        print(Fore.GREEN + f'Результат: {link}. Количество совпадений: {links_dict[link]}' + Style.RESET_ALL)
    

def main():
    link = input()
    finder(link, True)


if __name__ == "__main__":
    main()
