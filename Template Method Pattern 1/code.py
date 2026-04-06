from abc import ABC, abstractmethod
import json

class FormatStrategy(ABC):

    @abstractmethod
    def generate(self, data: list) -> str:
        pass

    @abstractmethod
    def get_extension(self) -> str:
        pass

class PDFFormatStrategy(FormatStrategy):

    def generate(self, data):
        report = "PDF REPORT\n"
        report += "=" * 50 + "\n"
        for item in data:
            report += f"| {item['name']:20} | {item['value']:10} |\n"
        report += "=" * 50 + "\n"
        report += "End of PDF Report"
        return report

    def get_extension(self):
        return "pdf"

class CSVFormatStrategy(FormatStrategy):

    def generate(self, data):
        report = "name,value\n"
        for item in data:
            report += f"{item['name']},{item['value']}\n"
        return report

    def get_extension(self):
        return "csv"

class JSONFormatStrategy(FormatStrategy):

    def generate(self, data):
        return json.dumps(data, indent=2)

    def get_extension(self):
        return "json"

class ExcelFormatStrategy(FormatStrategy):

    def generate(self, data):
        report = "EXCEL REPORT\n"
        report += "-" * 50 + "\n"
        report += "Name\tValue\n"
        for item in data:
            report += f"{item['name']}\t{item['value']}\n"
        report += "-" * 50 + "\n"
        return report

    def get_extension(self):
        return "xlsx"

class HTMLFormatStrategy(FormatStrategy):

    def generate(self, data):
        report = "<html><body><h1>Report</h1><ul>"
        for item in data:
            report += f"<li>{item['name']}: {item['value']}</li>"
        report += "</ul></body></html>"
        return report

    def get_extension(self):
        return "html"

class ReportGenerator:

    def __init__(self, data):
        self.data = data
        self.strategy = None

    def set_strategy(self, strategy: FormatStrategy):
        self.strategy = strategy

    def generate_report(self):
        if not self.strategy:
            raise ValueError("Strategy not set")
        return self.strategy.generate(self.data)

    def save_report(self, filename):
        if not self.strategy:
            raise ValueError("Strategy not set")

        content = self.generate_report()
        extension = self.strategy.get_extension()

        with open(f"{filename}.{extension}", "w") as f:
            f.write(content)

data = [
    {"name": "Sales Q1", "value": 15000},
    {"name": "Sales Q2", "value": 18000},
]

generator = ReportGenerator(data)

print("=== PDF ===")
generator.set_strategy(PDFFormatStrategy())
print(generator.generate_report())

print("\n=== CSV ===")
generator.set_strategy(CSVFormatStrategy())
print(generator.generate_report())

print("\n=== JSON ===")
generator.set_strategy(JSONFormatStrategy())
print(generator.generate_report())

print("\n=== HTML (NEW) ===")
generator.set_strategy(HTMLFormatStrategy())
print(generator.generate_report())

generator.set_strategy(CSVFormatStrategy())
generator.save_report("report")
