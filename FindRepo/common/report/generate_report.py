from typing import Dict

import json
import os
from datetime import datetime

from colorama import init
init()
from colorama import Fore, Style

from common.reader.reader import Reader

from common.config.config import config


def generate_global_report(result_data, path, save=True) -> None:
    os.makedirs('reports', exist_ok=True)

    report: Dict = {"Report": {
        "path": path
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
    
    file_path: str = os.getcwd() + "/reports"
    current_datetime = datetime.now().strftime("%y-%m-%d-%h-%m-%s")

    if save:
        Reader.write(report_json, f'reports/global_report{current_datetime}.json')
        print(Fore.GREEN + f"Файл с отчетом успешно сохранен по пути {file_path}")
