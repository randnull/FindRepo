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

    parser.add_argument(
        '-fast',
        action='store_true',
        help='Ускоренный поиск'
    )

    parser.add_argument(
        '-source',
        type=str,
        default=None,
        help='Источник кода для локального поиска'
    )

    parser.add_argument(
        '-read_only',
        action='store_false',
        help='Сохранить результаты в базе. Если -source не указан, то сохранение по пути.'
    )

    parser.add_argument(
        '-github',
        action='store_true',
        help='Нужно ли использовать поиск по github (обязателен токен)'
    )

    parser.add_argument(
        '-save_path',
        type=str,
        default="reports",
        help='Путь для сохранения результата'
    )

    client_args = parser.parse_args()

    if client_args.file is None:
        raise ErrorEmptyFile

    if client_args.type is None:
        raise ErrorEmtpyType

    client_agrs = {
        "file": client_args.file,
        "type": client_args.type,
        "source": client_args.source,
        "read_only": client_args.read_only,
        "github": client_args.github,
        "save_path": client_args.save_path,
        "fast": client_args.fast
    }

    return client_agrs
