import argparse

from common.errors.errors import *


def get_args():
    parser = argparse.ArgumentParser(description='FindRepo - консольное приложение для поиска похожий файлов')

    parser.add_argument(
        '-file',
        type=str,
        default=None,
        help='Путь до объекта'
    )

    parser.add_argument(
        '-type',
        type=str,
        default=None,
        help='Тип поиска (-global: глобальный поиск; -local: локальный поиск)'
    )

    client_args = parser.parse_args()

    if client_args.file is None:
        raise ErrorEmptyFile

    if client_args.type is None:
        raise ErrorEmtpyType

    return (client_args.file, client_args.type)
