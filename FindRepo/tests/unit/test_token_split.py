import pytest

from local_search.token_split.token_split import TokenSplit


class TestSplit:
    @pytest.fixture
    def get_split_class(self):
        return TokenSplit(hash_func='md5')


    def test_shingle_split(self, get_split_class):
        pass


    def test_token_split(self, get_split_class):
        pass
