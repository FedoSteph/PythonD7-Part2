from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def payment(self, amount):
        # Subclasses must implement this method
        pass


class PaymentBalance(PaymentProcessor):

    def __init__(self, balance: float):
        self.balance = balance

    def payment(self, amount):
        if amount > self.balance:
            return "Insufficient balance"

        self.balance -= amount
        return f"Payment successful. Remaining balance: {self.balance}"


class PayCreditCard(PaymentProcessor):

    def __init__(self, balance: float):
        self.balance = balance

    def payment(self, amount):
        self.balance -= amount
        return f"Credit card payment successful. Remaining balance: {self.balance}"


# Creating objects
balance = PaymentBalance(1000)
print(balance.payment(100))

credit_card = PayCreditCard(1200)
print(credit_card.payment(100))