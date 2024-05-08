import pytest

from global_search.split.split import Split


class TestSplit:
    @pytest.fixture
    def get_split_class(self):
        return Split(hash_func='md5')


    # def test_python_split(self, get_split_class):
    #     python_sample = '''
    #     def func1():
    #         return 14

    #     def func2(x: int):
    #         return x - 5

    #     print(func1() + func2(4))
    #     '''

    #     splitted = get_split_class.split(python_sample, ftype='py', is_code=True)

    #     assert len(splitted) == 3, f"Ожидалось 3 части. Получено: {len(splitted)}"
    #     assert len(splitted[0]) == 2, f"Ожидалось 2 элемента в каждой части. Получено: {len(splitted[0])}"



    def test_code_split(self, get_split_class):
        code_sample = '''
        package main

        func somefunc(s string) string {
            return s
        }

        func main() {
            somefunc("string")
        }
        '''

        splitted = get_split_class.split(code_sample, ftype='go', is_code=True)

        assert len(splitted) == 3, f"Ожидалось 3 части. Получено: {len(splitted)}"
        assert len(splitted[0]) == 2, f"Ожидалось 2 элемента в каждой части. Получено: {len(splitted[0])}"


    def test_text_split(self, get_split_class):
        text_sample = '''
        Пример текста. Пример текста.
        Пример текста
        '''

        splitted = get_split_class.split(text_sample, ftype='txt', is_code=False)

        assert len(splitted) == 3, f"Ожидалось 3 части. Получено: {len(splitted)}"
        assert len(splitted[0]) == 2, f"Ожидалось 2 элемента в каждой части. Получено: {len(splitted[0])}"
