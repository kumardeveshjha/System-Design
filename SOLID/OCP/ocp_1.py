#  Baa OCP example 

class PaymentMethod:
     
     def __init__(self):
          self.__CashPayments = 0
          self.__CreditCardPaymets = 0
          self.__DebitCardPayments = 0
     
     def CashPayment(self,amount:float):
          self.__CashPayments += amount
          print(f"Payment of {self.__CashPayments} made using cash.")
     
     def CreditCardPayment(self,amount:float):
          self.__CreditCardPaymets += amount
          print(f"Payment of {self.__CreditCardPaymets} made using credit card.")
     
     def DebitCardPayment(self,amount):
          self.__DebitCardPayments += amount
          print(f"Payment of {self.__DebitCardPayments} made using debit card.")
          
     def TotalPayment(self):
          total = self.__CashPayments + self.__CreditCardPaymets + self.__DebitCardPayments
          print(f"Total payment made: {total}")
     
     
     
payment = PaymentMethod()
payment.CashPayment(100)
payment.CreditCardPayment(300)
payment.DebitCardPayment(500)
payment.TotalPayment()

