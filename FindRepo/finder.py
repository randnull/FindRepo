# from argpars.parser import parser
from reader.reader import Reader
from search.search import find
from split.split import Split


CODE_TYPES = ['py']


def finder(link: str, fast: bool):   
    reader: Reader = Reader()

    files = reader.read(link)

    split_class: Split = Split('md5')

    for file, ftype in files:
        is_code: bool = ftype in CODE_TYPES

        splited = split_class.split(file, ftype, is_code)

