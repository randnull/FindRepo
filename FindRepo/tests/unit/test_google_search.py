import pytest

import requests

from common.config.config import config


class TestGoogleSearch:
    def test_google_search(self):
        google_host: str = config['GlobalSearch']['google_host']
        google_port: str = config['GlobalSearch']['google_port']

        url = f"http://{google_host}:{google_port}/google/search"

        text_to_search = "TestTest1"

        params = {
            "text": text_to_search,
            "limit": 10,
        }

        expected_code = 200

        try:
            response = requests.get(url, params=params)
        except:
            assert 1 == 0, "Сервер по поиску в Google не отвечает"

        assert response.status_code == expected_code, f"Ожидался код: {expected_code}. Получено: {response.status_code}"
