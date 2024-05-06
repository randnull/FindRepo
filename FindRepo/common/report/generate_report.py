from typing import Dict

import json

from common.reader.reader import Reader


def generate_report(result_data) -> None:
    report: Dict = {"Report": {}}

    for result_number, link in enumerate(result_data.values()):
        report["Report"][f"result_{result_number}"] = {
            "link": link
        }


    report_json = json.dumps(report, indent=4)

    Reader.write(report_json, 'report.json')
