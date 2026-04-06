from abc import ABC, abstractmethod
import json

class ReportGeneratorInterface(ABC):

    @abstractmethod
    def generate(self, data: dict) -> str:
        """Return JSON string"""
        pass

class LegacyReportGenerator:

    def generate_report(self, data: dict) -> str:
        xml = "<report>\n"
        for key, value in data.items():
            xml += f"  <{key}>{value}</{key}>\n"
        xml += "</report>"
        return xml

import json
import re

class LegacyReportAdapter(ReportGeneratorInterface):

    def __init__(self, legacy: LegacyReportGenerator):
        self.legacy = legacy

    def generate(self, data: dict) -> str:
        # 1. récupérer XML du legacy
        xml = self.legacy.generate_report(data)

        # 2. convertir XML → dict → JSON
        json_data = self._xml_to_json(xml)

        return json_data

    def _xml_to_json(self, xml: str) -> str:
        """
        Conversion simple XML -> JSON (basique pour l'exo)
        """
        data = {}

        # regex simple pour extraire les balises
        matches = re.findall(r"<(\w+)>(.*?)</\1>", xml)

        for key, value in matches:
            if key != "report":
                # tentative conversion nombre
                try:
                    value = float(value) if "." in value else int(value)
                except:
                    pass
                data[key] = value

        return json.dumps(data)

class AnalyticsDashboard:

    def display(self, json_data: str):
        data = json.loads(json_data)

        print("=== Analytics Dashboard ===")
        for key, value in data.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    legacy = LegacyReportGenerator()
    adapter = LegacyReportAdapter(legacy)
    dashboard = AnalyticsDashboard()

    report_data = {
        "total_sales": 150000,
        "orders": 1234
    }

    json_report = adapter.generate(report_data)

    dashboard.display(json_report)
