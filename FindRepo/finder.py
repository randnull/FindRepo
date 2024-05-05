from global_search.global_finder import global_finder


def finder(link):
    global_finder(link, True)

def main():
    link = input()
    finder(link)


if __name__ == "__main__":
    main()