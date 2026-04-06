from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def validate(self, details: dict) -> bool:
        pass

    @abstractmethod
    def process(self, amount: float, details: dict) -> dict:
        pass

class CreditCardProcessor(PaymentProcessor):

    def validate(self, details: dict) -> bool:
        card_number = details.get("card_number")
        cvv = details.get("cvv")

        return (
            card_number is not None and len(card_number) == 16 and
            cvv is not None and len(cvv) == 3
        )

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid card details"}

        fee = amount * 0.029
        total = amount + fee

        return {
            "success": True,
            "method": "credit_card",
            "amount": total,
            "fee": fee
        }

class BankTransferProcessor(PaymentProcessor):

    def validate(self, details: dict) -> bool:
        iban = details.get("iban")
        return iban is not None and len(iban) >= 15

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid IBAN"}

        fee = 1.50
        total = amount + fee

        return {
            "success": True,
            "method": "bank_transfer",
            "amount": total,
            "fee": fee
        }

class PayPalProcessor(PaymentProcessor):

    def validate(self, details: dict) -> bool:
        email = details.get("email")
        return email is not None and "@" in email

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid email"}

        fee = amount * 0.034 + 0.30
        total = amount + fee

        return {
            "success": True,
            "method": "paypal",
            "amount": total,
            "fee": fee
        }

class PaymentFactory:

    def __init__(self):
        self._processors = {
            "credit_card": CreditCardProcessor,
            "bank_transfer": BankTransferProcessor,
            "paypal": PayPalProcessor
        }

    def get_processor(self, payment_type: str) -> PaymentProcessor:
        processor_class = self._processors.get(payment_type)

        if not processor_class:
            raise ValueError(f"Unknown payment type: {payment_type}")

        return processor_class()

if __name__ == "__main__":
    factory = PaymentFactory()

    processor = factory.get_processor("credit_card")

    result = processor.process(100.0, {
        "card_number": "1234567890123456",
        "cvv": "123"
    })

    print(result)

