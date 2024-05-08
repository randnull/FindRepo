from typing import List
import requests
import functools

from colorama import init
init()
from colorama import Fore, Back, Style

from common.config.config import config


@functools.lru_cache(maxsize=10000)
def google_request(object_body: str):
    results_set = set()

    google_host: str = config['GlobalSearch']['google_host']
    google_port: str = config['GlobalSearch']['google_port']

    url = f"http://{google_host}:{google_port}/google/search"

    google_limit = int(config['GlobalSearch']['google_limit'])
    google_max_len = int(config['GlobalSearch']['google_max_len'])

    params = {
        "text": object_body[:google_max_len],
        "limit": google_limit,
    }

    try:
        response = requests.get(url, params=params)
    except:
        return set()

    if response.status_code == 200:
        data = response.json()
        
        for site in data:
            results_set.add(site['url'])

    return results_set


@functools.lru_cache(maxsize=10000)
def find_google(object_body: str, is_code=True) -> List[str]:
    results_set = set()

    results_set = google_request(object_body=object_body)

    return list(results_set)
