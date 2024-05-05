from global_search.global_finder import global_finder
from local_search.local_finder import local_finder


def finder(link, search_type: str):
    if search_type == 'global':
        global_finder(link, True)
    if search_type == 'local':
        local_finder(link)


def main():
    link = input()
    search_type = input()
    finder(link, search_type)


if __name__ == "__main__":
    main()
