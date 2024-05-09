import pytest

import toml

import requests

from common.config.config import config


class TestGithubSearch:
    def test_github_search(self):
        api_link: str = config['GlobalSearch']['github_api_link']

        url_with_code = f'{api_link}={"Test"}'

        toml_config = toml.load('FindRepo/auth/authorization.toml')
        token = toml_config['token_github']['token']

        headers = {
            'Authorization': token
        }

        try:
            response = requests.get(url_with_code, headers=headers)
        except:
            pass

        expected_code = 200
            
        assert response.status_code == expected_code, f"Ожидался код: {expected_code}. Получено: {response.status_code}"
