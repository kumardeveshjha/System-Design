# Creating the main account class
from abc import ABC, abstractmethod

class Account(ABC):
     def __init__(self, balance: float):
          self.balance = balance
     
     @abstractmethod
     def deposit(self, amount: float):
          pass
     

