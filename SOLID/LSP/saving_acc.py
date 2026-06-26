
from my_account import Account

class SavingsAccount(Account):
     def deposit(self, amount: float):
          self.balance += amount
          print(f"Deposited {amount} to Savings Account. New balance: {self.balance}")
          
     def withdraw(self, amount: float):
          if self.balance >= amount:
               self.balance -= amount
               print(f"Withdrew {amount} from Savings Account. New balance: {self.balance}")
          else:
               print("Insufficient funds in Savings Account.")


saving = SavingsAccount(1000)

 