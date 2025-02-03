
class Payment:
    def process_payment(self, amount):
        print(f"Processing a payment of ${amount}")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing a credit card payment of ${amount}")


class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing a PayPal payment of ${amount}")

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing a Bitcoin payment of ${amount}")


payment1 = CreditCardPayment()
payment1.process_payment(100) 

payment2 = PayPalPayment()
payment2.process_payment(50)   

payment3 = BitcoinPayment()
payment3.process_payment(200)  
