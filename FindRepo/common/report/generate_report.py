from typing import Dict

import json
import os
from datetime import datetime

from colorama import init
init()
from colorama import Fore, Style

from common.reader.reader import Reader

from common.config.config import config


def generate_report(result_data: Dict, path: str, search_type: str, save=True) -> None:
    '''Генерирует и сохраняет отчет о проверке в формате json'''

    dir_name: str = config['Report']['dir_name']

    os.makedirs(dir_name, exist_ok=True)

    report: Dict = {"Report": {
        "path": path,
        "search_type": search_type
    }}

    if result_data is None or len(result_data) == 0:
        report["Report"].update({
            "result": "No one match"
        })
    else:
        report["Report"].update({
            "result": "Founded"
        })
        for result_number, link in enumerate(result_data):
            report["Report"][f"result_{result_number + 1}"] = {
                "link": link,
                "match": result_data[link]
            }

    report_json = json.dumps(report, indent=4)

    file_path: str = os.getcwd() + f"/{dir_name}"
    current_datetime = datetime.now().strftime("%y-%m-%d-%h-%m-%s")

    if save:
        Reader.write(report_json, f'{dir_name}/global_report{current_datetime}.json')
        print(Fore.GREEN + f"Файл с отчетом успешно сохранен по пути {file_path}")
