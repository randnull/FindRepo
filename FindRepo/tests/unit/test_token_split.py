import pytest

from local_search.token_split.token_split import TokenSplit
from common.reader.reader import Reader


class TestSplit:
    @pytest.fixture
    def get_split_class(self):
        return TokenSplit(hash_func='md5')


    @pytest.fixture
    def get_reader_class(self):
        return Reader()


    def test_py_shingle_split(self, get_split_class, get_reader_class):
        readed_file = get_reader_class.read("FindRepo/tests/example/example.py")[0][0]

        tokenized_object = get_split_class._tokenize_code(readed_file)

        shingle_object = get_split_class._get_shingles(tokenized_object, 3)

        assert len(tokenized_object) - 4 == len(shingle_object), f"Ожидаемая длина shingle: {len(tokenized_object) - 4}. Получено: {len(shingle_object)}"


    def test_go_shingle_split(self, get_split_class, get_reader_class):
        readed_file = get_reader_class.read("FindRepo/tests/example/example.go")[0][0]

        tokenized_object = get_split_class._tokenize_code(readed_file)

        shingle_object = get_split_class._get_shingles(tokenized_object, 3)

        assert len(tokenized_object) - 2 == len(shingle_object), f"Ожидаемая длина shingle: {len(tokenized_object) - 2}. Получено: {len(shingle_object)}"


    def test_txt_shingle_split(self, get_split_class, get_reader_class):
        readed_file = get_reader_class.read("FindRepo/tests/example/example.txt")[0][0]

        tokenized_object = get_split_class._tokenize_code(readed_file)

        shingle_object = get_split_class._get_shingles(tokenized_object, 3)

        assert len(tokenized_object) - 11 == len(shingle_object), f"Ожидаемая длина shingle: {len(tokenized_object) - 11}. Получено: {len(shingle_object)}"
