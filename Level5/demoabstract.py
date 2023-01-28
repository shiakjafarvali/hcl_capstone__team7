from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def payment(selfself,amt):
        pass
    def gen_slip(selfself,amt):
        print(amt)
class CreditPayment(Payment):
    def payment(selfself,amt):
        print("Paid Amount Using Credit Card",amt)
    def gen_slip(selfself,amt):
        print(amt)

class DebitCard(Payment):
    def payment(selfself,amt):
        print("Paid amount using Debit card",amt)
    def gen_slip(selfself,amt):
        print(amt)
obj1=CreditPayment()
obj1.payment(350)
obj1.gen_slip(350)
obj2=DebitCard()
obj2.payment(350)
obj2.gen_slip(350)