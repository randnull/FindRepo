import pytest

from global_search.search.google.google import find_google


class TestGoogleSearch:
    def test_google_request(self):
        result = find_google("Example")

        assert len(result) != 0, "Нет результатов поиска"
