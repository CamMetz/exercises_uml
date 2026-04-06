from abc import ABC, abstractmethod
import time


class DataPipeline(ABC):

    def __init__(self, source):
        self.source = source
        self.data = None

    def run(self):
        self.connect()
        self.extract()
        self.transform()
        self.validate()
        self.load()
        self.cleanup()

        return f"{self.__class__.__name__} finished"

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    def validate(self):
        print("Validating data...")
        for record in self.data:
            if not isinstance(record, dict):
                raise ValueError("Invalid record structure")
        print("Validation passed")

    def load(self):
        print("Loading data to destination...")
        time.sleep(0.5)
        print(f"Loaded {len(self.data)} records successfully")

    def cleanup(self):
        print("Cleaning up resources...")
        self.data = None
        print("Cleanup complete")

class CSVPipeline(DataPipeline):

    def connect(self):
        print(f"Connecting to CSV file: {self.source}")
        time.sleep(0.5)
        print("CSV connection established")

    def extract(self):
        print("Extracting CSV data...")
        self.data = [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25}
        ]

    def transform(self):
        print("Transforming CSV data...")
        for record in self.data:
            record["age"] = int(record["age"])
            record["name"] = record["name"].upper()

class APIPipeline(DataPipeline):

    def connect(self):
        print(f"Connecting to API: {self.source}")
        time.sleep(0.5)
        print("API connection established")

    def extract(self):
        print("Extracting API data...")
        self.data = [
            {"user_id": 101, "username": "charlie", "score": 85},
            {"user_id": 102, "username": "diana", "score": 92}
        ]

    def transform(self):
        print("Transforming API data...")
        for record in self.data:
            record["score"] = int(record["score"])
            record["username"] = record["username"].lower()
            record["grade"] = "A" if record["score"] >= 90 else "B"

class DatabasePipeline(DataPipeline):

    def connect(self):
        print(f"Connecting to database: {self.source}")
        time.sleep(0.5)
        print("Database connection established")

    def extract(self):
        print("Extracting DB data...")
        self.data = [
            {"product_id": 501, "product_name": "Laptop", "price": 1200},
            {"product_id": 502, "product_name": "Mouse", "price": 25}
        ]

    def transform(self):
        print("Transforming DB data...")
        for record in self.data:
            record["price"] = float(record["price"])
            record["product_name"] = record["product_name"].title()
            record["tax"] = record["price"] * 0.2

class XMLPipeline(DataPipeline):

    def connect(self):
        print(f"Connecting to XML file: {self.source}")
        time.sleep(0.5)
        print("XML connection established")

    def extract(self):
        print("Extracting XML data...")
        self.data = [
            {"order_id": 1, "amount": "100"},
            {"order_id": 2, "amount": "200"}
        ]

    def transform(self):
        print("Transforming XML data...")
        for record in self.data:
            record["amount"] = float(record["amount"])

if __name__ == "__main__":

    print("CSV PIPELINE")
    csv_pipeline = CSVPipeline("data/users.csv")
    print(csv_pipeline.run())

    print("\n" + "="*50)

    print("API PIPELINE")
    api_pipeline = APIPipeline("https://api.com")
    print(api_pipeline.run())

    print("\n" + "="*50)

    print("DB PIPELINE")
    db_pipeline = DatabasePipeline("postgresql://localhost/db")
    print(db_pipeline.run())

    print("\n" + "="*50)

    print("XML PIPELINE (NEW)")
    xml_pipeline = XMLPipeline("data/orders.xml")
    print(xml_pipeline.run())
