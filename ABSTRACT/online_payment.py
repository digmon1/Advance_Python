from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Rs.{amount} paid using Credit Card.")

    def refund(self, amount):
        print(f"Rs.{amount} refunded to Credit Card.")


class DebitCard(Payment):

    def pay(self, amount):
        print(f"Rs.{amount} paid using Debit Card.")

    def refund(self, amount):
        print(f"Rs.{amount} refunded to Debit Card.")


class UPI(Payment):

    def pay(self, amount):
        print(f"Rs.{amount} paid using UPI.")

    def refund(self, amount):
        print(f"Rs.{amount} refunded to UPI.")


credit = CreditCard()
debit = DebitCard()
upi = UPI()

credit.pay(5000)
credit.refund(1000)

print()

debit.pay(2500)
debit.refund(500)

print()

upi.pay(1500)
upi.refund(300)