from typing import List
import requests
import functools


@functools.lru_cache(maxsize=10000)
def google_request(object_body: str, site: str):
    results_set = set()

    url = "http://127.0.0.1:6500/google/search"

    params = {
        "text": object_body,
        "limit": 10,
    }

    if site != '':
        params["site"] = site 

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        for site in data:
            results_set.add(site['url'])

    return results_set


@functools.lru_cache(maxsize=10000)
def find_google(object_body: str, is_code=True) -> List[str]:
    print('Поиск: google')
    results_set = set()

    sites: List = ['']

    for site in sites:
        results_set = results_set.union(google_request(object_body=object_body, site=site))

    if len(results_set) != 0:
        print('Google: Найдено!')

    return list(results_set)
