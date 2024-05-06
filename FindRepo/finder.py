from colorama import init
init()
from colorama import Fore, Style

from common.errors.errors import *

from common.argpars.parser import get_args

from common.report.generate_report import generate_report

from global_search.global_finder import global_finder
from local_search.local_finder import local_finder


def main():
    try:
        path, search_type = get_args()
    except ErrorEmptyFile:
        print(Fore.RED + "Не указан путь к файлу или директории (-file)" + Style.RESET_ALL)
        return
    except ErrorEmtpyType:
        print(Fore.RED + "Не указан тип поиска (-type)" + Style.RESET_ALL)
        return

    if search_type == 'global':
        global_finder(path, True)
    elif search_type == 'local':
        local_finder(path)
    else:
        print(Fore.RED + "Не сущетсвующий тип поиска")
        return


if __name__ == "__main__":
    main()
