from abc import ABC, abstractmethod

class OrderComponent(ABC):

    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

class BaseOrder(OrderComponent):

    def __init__(self, base_price: float):
        self.base_price = base_price

    def get_cost(self) -> float:
        return self.base_price

    def get_description(self) -> str:
        return f"Base price: {self.base_price}€"

class OrderDecorator(OrderComponent):

    def __init__(self, component: OrderComponent):
        self.component = component

    def get_cost(self) -> float:
        return self.component.get_cost()

    def get_description(self) -> str:
        return self.component.get_description()

class ExpressShippingDecorator(OrderDecorator):

    def get_cost(self) -> float:
        return self.component.get_cost() + 15.0

    def get_description(self) -> str:
        return self.component.get_description() + "\nExpress shipping: +15€"

class ExpressShippingDecorator(OrderDecorator):

    def get_cost(self) -> float:
        return self.component.get_cost() + 15.0

    def get_description(self) -> str:
        return self.component.get_description() + "\nExpress shipping: +15€"

class InsuranceDecorator(OrderDecorator):

    def get_cost(self) -> float:
        return self.component.get_cost() + (self.component.get_cost() * 0.05)

    def get_description(self) -> str:
        return self.component.get_description() + "\nInsurance (5%)"

class GiftWrapDecorator(OrderDecorator):

    def get_cost(self) -> float:
        return self.component.get_cost() + 5.0

    def get_description(self) -> str:
        return self.component.get_description() + "\nGift wrap: +5€"


class DiscountDecorator(OrderDecorator):

    def __init__(self, component: OrderComponent, percent: float):
        super().__init__(component)
        self.percent = percent

    def get_cost(self) -> float:
        cost = self.component.get_cost()
        return cost - (cost * self.percent / 100)

    def get_description(self) -> str:
        return self.component.get_description() + f"\nDiscount: -{self.percent}%"

  class PremiumMemberDecorator(OrderDecorator):

    def get_cost(self) -> float:
        cost = self.component.get_cost()
        return cost - (cost * 0.10)

    def get_description(self) -> str:
        return self.component.get_description() + "\nPremium member: -10%"

    if __name__ == "__main__":
    order = BaseOrder(100.00)

    order = ExpressShippingDecorator(order)
    order = InsuranceDecorator(order)
    order = GiftWrapDecorator(order)
    order = DiscountDecorator(order, percent=15)
    order = PremiumMemberDecorator(order)

    print(order.get_description())
    print(f"\nTOTAL: {order.get_cost()}€")
