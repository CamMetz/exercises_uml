import json

class ConfigManager:
    _instance = None

    def __init__(self):
        if ConfigManager._instance is not None:
            raise Exception("This class is a singleton!")

        self._config = {}
        self._load_config()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ConfigManager()
        return cls._instance

    def _load_config(self):
        with open("config.json", "r") as f:
            self._config = json.load(f)

    def get(self, key: str):
        keys = key.split(".")
        value = self._config

        for k in keys:
            value = value.get(k)
            if value is None:
                return None

        return value

    def reload(self):
        """Reload config from file"""
        self._load_config()

class DatabaseService:

    def connect(self):
        config = ConfigManager.get_instance()

        db_host = config.get("database.host")
        db_port = config.get("database.port")

        print(f"Connecting to database at {db_host}:{db_port}")

class EmailService:

    def send_email(self, to: str, subject: str):
        config = ConfigManager.get_instance()

        smtp_host = config.get("email.smtp_host")
        sender = config.get("email.sender")

        print(f"Sending email from {sender} via {smtp_host} to {to}")

class EmailService:

    def send_email(self, to: str, subject: str):
        config = ConfigManager.get_instance()

        smtp_host = config.get("email.smtp_host")
        sender = config.get("email.sender")

        print(f"Sending email from {sender} via {smtp_host} to {to}")

if __name__ == "__main__":
    db_service = DatabaseService()
    email_service = EmailService()
    payment_service = PaymentService()

    db_service.connect()
    email_service.send_email("user@test.com", "Welcome")
    payment_service.process_payment(99.99)

