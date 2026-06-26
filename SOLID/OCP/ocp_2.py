from abc import ABC, abstractmethod

class PaymentProcess(ABC):
     @abstractmethod
     def pay(self, amount):
          pass
     
     
#  Cash Paument class
class CashPayment(PaymentProcess):
     def __init__(self, tracker=None):
        self.tracker = tracker
        
     def pay(self,amount):
          print(f"Payment of {amount} made using cash.")
          
          if self.tracker:
               self.tracker.track_payment(amount)
          
     

# Credit card paument class 
class CreditCardPayment(PaymentProcess):
     
     def __init__(self, tracker=None):
        self.tracker = tracker
        
     def pay(self,amount):
          print(f"Payment of {amount} made using credit card.")

          if self.tracker:
               self.tracker.track_payment(amount)

#  Debit card payment class 

class DebitCardPayment(PaymentProcess):
     def __init__(self, tracker=None):
        self.tracker = tracker

     def pay(self,amount):
          print(f"Payment of {amount} made using debit card.")
          
          if self.tracker:
               self.tracker.track_payment(amount)

class TotalPayment(PaymentProcess):
     def __init__(self):
          self.total = 0
     
     def pay(self, amount):
          pass
     
     def track_payment(self, amount):
          self.total += amount
     
     def TotalPayment(self):
          print(f"Total payment made: {self.total}")
          
          
total_payment = TotalPayment()    
cash_payment = CashPayment(tracker = total_payment)
credit_card_payment = CreditCardPayment(tracker = total_payment)
debit_card_payment = DebitCardPayment(tracker = total_payment)


cash_payment.pay(100)
credit_card_payment.pay(300)  
debit_card_payment.pay(500)
total_payment.TotalPayment()