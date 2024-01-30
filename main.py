import argparse
import os

import ast
import astunparse

from FindRepo.github.github import find_github_code
from FindRepo.gitlab.gitlab import find_gitlab_code


forbidden_char = ['"', '@']


def sep_to_func(code: str):
    tree = ast.parse(code)

    parts = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            parts.append(astunparse.unparse(node).strip())
    
    tree.body = [node for node in tree.body if not isinstance(node, ast.FunctionDef)]

    parts.append(astunparse.unparse(tree).strip())

    return parts


def filter_code(code: str) -> str:
    for ch in forbidden_char:
        code = code.replace(ch, ' ')
    return code


def main():
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
    count = client_args.max_count

    if not count.isdigit():
        raise RuntimeError('Count must be int!')
    
    count = int(count)
    
    code_for_checking = sep_to_func(code)
    
    result_github = []

    for part in code_for_checking:
        result = find_github_code(part, 1)
        
        if result != []:
            result_github.append(*result)

    print('github result: ', end="")
    print(*result_github)


if __name__ == "__main__":
    main()
