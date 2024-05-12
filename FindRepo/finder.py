from colorama import init
init()
from colorama import Fore, Style

from common.errors.errors import *

from typing import Dict

from common.argpars.parser import get_args

from common.report.generate_report import generate_report

from global_search.global_finder import global_finder
from local_search.local_finder import local_finder, save_results


def main():
    try:
        client_args: Dict = get_args()

        path: str = client_args["file"]
        search_type: str = client_args["type"]
        source: str = client_args["source"]
        save: bool = client_args["read_only"]
        need_github: bool = client_args["github"]
        fast: bool = client_args["fast"]
        save_path: str = client_args["save_path"]
    except ErrorEmptyFile:
        print(Fore.RED + "Не указан путь к файлу или директории (-file)" + Style.RESET_ALL)
        return
    except ErrorEmtpyType:
        print(Fore.RED + "Не указан тип поиска (-type)" + Style.RESET_ALL)
        return

    if search_type == 'global':
        result, ok = global_finder(path, need_github, fast)
    elif search_type == 'local':
        result, ok, value_to_save = local_finder(path)
    else:
        print(Fore.RED + "Не сущетсвующий тип поиска" + Style.RESET_ALL)
        return

    if ok:
        generate_report(result_data=result, path=path, search_type=search_type, save_path=save_path)

    if search_type == 'local' and save:
        save_results(path, source, value_to_save)


if __name__ == "__main__":
    main()
