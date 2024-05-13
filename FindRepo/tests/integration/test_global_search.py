import pytest
import warnings

from global_search.global_finder import global_finder


class TestGlobalSearch:
    def test_global_search(self):
        path = "FindRepo/tests/example/example.py"

        result = global_finder(path, False, False)

        assert result[1], "Поиск не выполнен"

        if len(result[0]) == 0:
            warnings.warn(UserWarning("Глобальный поиск не дал результатов"))
