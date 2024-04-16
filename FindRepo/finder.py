# from argpars.parser import parser
from reader.reader import Reader
from search.search import Searcher
from split.split import Split


CODE_TYPES = ['py']


def finder(link: str, fast: bool):   
    reader: Reader = Reader()

    files = reader.read(link)

    split_class: Split = Split('md5')

    links_dict = dict()

    for file, ftype in files:
        is_code: bool = ftype in CODE_TYPES

        if is_code:
            searcher_class: Searcher = Searcher(is_code=is_code)

            splited = split_class.split(file, ftype, is_code)

            for part in splited:
                links = searcher_class.find(part)

                for link in links:
                    links_dict[link] = links_dict.get(link, 0) + 1
            
    for link in dict(sorted(links_dict.items(), key=lambda item: -item[1])):
        if links_dict[link] > 1:
            print(f'Результат: {link}. Количество совпадений: {links_dict[link]}')
    

def main():
    link = input()
    finder(link, True)


if __name__ == "__main__":
    main()
