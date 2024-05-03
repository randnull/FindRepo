from typing import List


class FormatterPerRequest:
    def __init__(self):
        pass


    @staticmethod
    def _delete_forbidden_char(raw_object: str, forbidden_char: List) -> str:
        for ch in forbidden_char:
            raw_object = raw_object.replace(ch, '')
        return raw_object


    def _delete_whitespaces(self, raw_object: str) -> str:
        lines: List = raw_object.split('\n')

        clear_lines: List = list()

        for line in lines:
            if line.strip():
                clear_lines.append(line)

        return '\n'.join(clear_lines)


    def format(self, raw_object: str) -> str:
        new_object: str = self._delete_spaces(raw_object)

        return new_object


class FormatterPerHash:
    def __init__(self):
        pass

    #ast