import pytest
import warnings

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

            if response.status_code == 401:
                warnings.warn(UserWarning("Токен для авторизации Github не работает. Поиск по нему недоступен"))
            elif response.status_code != 200:
                warnings.warn(UserWarning(f"Код ответа github: {response.status_code}. Поиск по нему недоступен"))
        except:
            warnings.warn(UserWarning("Github не отвечает. Поиск по нему недоступен"))
