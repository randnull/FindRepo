from typing import List


class FormatterPerRequest:
    def __init__(self):
        pass


    @staticmethod
    def delete_forbidden_char(raw_object: str) -> str:
        '''Удаляет запрещенные для запроса символы'''
        github_forbidden_char: List = [".", ",", ":", ";", "/", "\\", "'",
                                    '"', "=", "*", "!", "?", "#", "$", "&"
                                    "+", "^", "|", "~", "<", ">", "(", ")",
                                    "{", "}", "[", "]", "@", '`']

        for ch in github_forbidden_char:
            raw_object = raw_object.replace(ch, '')
        return raw_object


    def _delete_empty_lines(self, raw_object: str) -> str:
        '''Удаляет пустые строки'''

        lines: List = raw_object.split('\n')

        clear_lines: List = list()

        for line in lines:
            if line.strip():
                clear_lines.append(line)

        return '\n'.join(clear_lines)


    def format(self, raw_object: str) -> str:
        '''Стандартизирует объект'''

        new_object: str = self._delete_empty_lines(raw_object)

        return new_object


class FormatterPerHash:
    def __init__(self):
        pass

    #ast
