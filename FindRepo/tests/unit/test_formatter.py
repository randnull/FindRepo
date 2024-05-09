import pytest

from common.formatter.formatter import FormatterPerHash, FormatterPerRequest


class TestFormater:
    @pytest.fixture
    def get_formatter_per_hash_class(self):
        return FormatterPerHash()

    
    @pytest.fixture
    def get_formatter_per_request_class(self):
        return FormatterPerRequest()


    def test_formatter_per_request(self, get_formatter_per_request_class):
        code_sample = '''

        def func():
            return 1

        print(func())


        '''

        formatted_code = get_formatter_per_request_class.format(code_sample)

        for line in formatted_code.split('\n'):
            assert line.strip(), "Код имеет пустые строки"


    def test_delete_forbidden_char(self, get_formatter_per_request_class):
        code_sample = '''
        def func():
            """описание@"""

            return 1

        print(func())
        '''

        formatted_code = FormatterPerRequest.delete_forbidden_char(code_sample)

        char_count = formatted_code.count('"') + formatted_code.count('@')

        assert char_count == 0, "В коде остались удаленные символы"
