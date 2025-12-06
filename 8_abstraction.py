from abc import ABC,abstractclassmethod
class Payment(ABC):
    @abstractclassmethod
    def make_payment(self,amount):
        pass
    def show_receipt(self):
        print("Receipt generated!")

class CreditCardPayment(Payment):
    def make_payment(self,amount):
        print(f"paid {amount} using Credit card")

class UPI(Payment):
    def make_payment(self,amount):
        print(f"paid {amount} using UPI")

payment1=CreditCardPayment()
payment1.make_payment(1000)
payment1.show_receipt()

payment2=UPI()
payment2.make_payment(500)
payment2.show_receipt()



# output
# paid 1000 using Credit card
# Receipt generated!
# paid 500 using UPI
# Receipt generated!