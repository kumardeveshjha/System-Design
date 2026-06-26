from abc import ABC, abstractmethod
from sys import exception

#  --> Bad example that violtes Liskov Substitution Principle (LSP)

# Account class that violates the Liskov Substitution Principle (LSP)
class Account(ABC):
     
     def __init__(self,balance: float):
          self.balance = balance
          
     @abstractmethod
     def deposit(self, amount: float):
          pass
          
     @abstractmethod
     def withdraw(self, amount: float):
          pass
     
#  saving account that allows deposits and withdrawals
class SavingsAccount(Account):
     def deposit(self,amount: float):
          self.balance += amount
          print(f"Deposited {amount} to Savings Account. New balance: {self.balance}")
     def withdraw(self, amount: float):
          if self.balance >= amount:
               self.balance -= amount
               print(f"Withdrew {amount} from Savings Account. New balance: {self.balance}")
          else:
               print("Insufficient funds in Savings Account.")


#  fixed deposite account that allows deposits but not withdrawals until maturity
class FixedDepositAccount(Account):
    def __init__(self, balance: float):
        super().__init__(balance)
     

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited {amount} to Fixed Deposit Account. New balance: {self.balance}")

    def withdraw(self, amount: float):
        return exception("Withdrawals are not allowed from Fixed Deposit Account until maturity.")


saving = SavingsAccount(1000)
saving.deposit(500)
saving.withdraw(200)
fixed_deposit = FixedDepositAccount(5000)
fixed_deposit.deposit(1000)
fixed_deposit.withdraw(2000)