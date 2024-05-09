import pytest
import warnings

from local_search.local_finder import local_finder


class TestLocalSearch:
    def test_local_search(self):
        path = "FindRepo/tests/example/example.py"

        result = local_finder(path)

        assert result[1], "Поиск не выполнен"

        if len(result[0]) == 0:
            warnings.warn(UserWarning("Локальный поиск не дал результатов"))
