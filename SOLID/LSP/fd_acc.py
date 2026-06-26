


from my_account import Account
from sys import exception
class FixedDeposite(Account):
     def __init__(self,amount):
          self.balance = amount
          
     def deposit(self, amount):
         self.balance += amount
         print(f"Your current account balance is {self.balance}")
         
     def withdraw(self,amount: float):
          return exception("Withdrawals are not allowed from Fixed Deposit Account until maturity.")