import argparse
import os

from FindRepo.github.github import find_github_code
from FindRepo.gitlab.gitlab import find_gitlab_code


forbidden_char = ['"', '@']


def filter_code(code: str) -> str:
    for ch in forbidden_char:
        code = code.replace(ch, '')
    return code


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-file',
        type=str,
        default=""
    )
    parser.add_argument(
        '-max_count',
        type=str,
        default=""
    )

    client_args = parser.parse_args()

    file = open(client_args.file, 'r')
    _, file_name = os.path.split(client_args.file)    
    file_name = file_name.split('.')[0]

    code = filter_code(file.read())
    count = int(client_args.max_count)

    result_github = find_github_code(code, count)
    result_gitlab = find_gitlab_code(file_name, count)

    print('github result: ', end="")
    print(*result_github)
    
    print('gitlab result: ', end="")
    print(*result_gitlab)
