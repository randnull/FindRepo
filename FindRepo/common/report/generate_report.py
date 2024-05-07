from typing import Dict

import json

from common.reader.reader import Reader


def generate_report(result_data, save=True) -> None:
    report: Dict = {"Report": {}}

    for result_number, link in enumerate(result_data):
        report["Report"][f"result_{result_number}"] = {
            "link": link
        }

    report_json = json.dumps(report, indent=4)
    
    if save:
        Reader.write(report_json, 'report.json')
