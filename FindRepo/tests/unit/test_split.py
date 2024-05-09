import pytest

from global_search.split.split import Split
from common.reader.reader import Reader


class TestSplit:
    @pytest.fixture
    def get_split_class(self):
        return Split(hash_func='md5')


    @pytest.fixture
    def get_reader_class(self):
        return Reader()


    def test_python_split(self, get_split_class, get_reader_class):
        readed_file = get_reader_class.read("FindRepo/tests/example/example.py")

        python_sample = readed_file[0][0]
        ftype = readed_file[0][1]

        splitted = get_split_class.split(python_sample, ftype=ftype, is_code=True)

        assert len(splitted) == 3, f"Ожидалось 3 части. Получено: {len(splitted)}"
        assert len(splitted[0]) == 2, f"Ожидалось 2 элемента в каждой части. Получено: {len(splitted[0])}"


    def test_code_split(self, get_split_class, get_reader_class):
        readed_file = get_reader_class.read("FindRepo/tests/example/example.go")

        code_sample = readed_file[0][0]
        ftype = readed_file[0][1]

        splitted = get_split_class.split(code_sample, ftype=ftype, is_code=True)

        assert len(splitted) == 3, f"Ожидалось 3 части. Получено: {len(splitted)}"
        assert len(splitted[0]) == 2, f"Ожидалось 2 элемента в каждой части. Получено: {len(splitted[0])}"


    def test_text_split(self, get_split_class, get_reader_class):
        readed_file = get_reader_class.read("FindRepo/tests/example/example.txt")

        text_sample = readed_file[0][0]
        ftype = readed_file[0][1]

        splitted = get_split_class.split(text_sample, ftype=ftype, is_code=False)

        assert len(splitted) == 4, f"Ожидалось 4 части. Получено: {len(splitted)}"
        assert len(splitted[0]) == 2, f"Ожидалось 2 элемента в каждой части. Получено: {len(splitted[0])}"
