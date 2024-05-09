import pytest

from common.reader.reader import Reader


class TestSplit:
    @pytest.fixture
    def get_reader_class(self):
        return Reader()

    
    def test_read_file(self, get_reader_class):
        readed_file = get_reader_class.read("FindRepo/tests/example/example.py")
        expected_type = 'py'

        assert len(readed_file) == 1, f"Ожидался 1 считанный файл. Получено: {len(readed_file[0])}"
        assert readed_file[0][1] == expected_type, f"Ожидался тип: {expected_type}. Получено: {readed_file[0][1]}"

        readed_file = get_reader_class.read("FindRepo/tests/example/example.go")
        expected_type = 'go'

        assert len(readed_file) == 1, f"Ожидался 1 считанный файл. Получено: {len(readed_file[0])}"
        assert readed_file[0][1] == expected_type, f"Ожидался тип: {expected_type}. Получено: {readed_file[0][1]}"


    def test_read_dir(self, get_reader_class):
        readed_dir = get_reader_class.read("FindRepo/tests/example")
        expected_types = ['go', 'py', 'txt', 'cpp']

        assert len(readed_dir) == 6, f"Ожидалось 6 считанных файла. Получено: {len(readed_dir)}"
        for file, ftype, _ in readed_dir:
            assert ftype in expected_types, f"Ожидался один из типов: {expected_types}. Получено: {ftype}"


    def test_read_ipynb(self, get_reader_class):
        readed_file = get_reader_class.read("FindRepo/tests/example/example.ipynb")
        expected_type = 'py'

        assert len(readed_file) == 1, f"Ожидался 1 считанный файл. Получено: {len(readed_file[0])}"
        assert readed_file[0][1] == expected_type, f"Ожидался тип: {expected_type}. Получено: {readed_file[0][1]}"
