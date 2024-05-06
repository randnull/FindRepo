from typing import List
import requests
import functools

from colorama import init
init()
from colorama import Fore, Back, Style


@functools.lru_cache(maxsize=10000)
def google_request(object_body: str):
    results_set = set()

    url = "http://127.0.0.1:6500/google/search"

    params = {
        "text": object_body[:31],
        "limit": 5,
    }

    try:
        response = requests.get(url, params=params)
    except:
        # print(Fore.RED + 'Google не доступен!' + Style.RESET_ALL)
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

    #if len(results_set) != 0:
        #print(Fore.GREEN + 'Google: Найдено!' + Style.RESET_ALL)

    return list(results_set)
