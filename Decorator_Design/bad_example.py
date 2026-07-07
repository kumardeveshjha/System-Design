#  

from abc import ABC, abstractmethod
class Bevarage(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_cost(self):
        pass
   
   
class Coffee(Bevarage):
     def get_description(self):
          return "Coffee"
     
     def get_cost(self):
          return 20
     
     
class CoffeeWithMilk(Bevarage):
     def get_description(self):
          return "Coffee with milk"
     def get_cost(self):
          return 30
     
class CoffeeWithMilkAndSugar(Bevarage):
     def get_description(self):
          return "Coffee with milk and sugar"
     def get_cost(self):
          return 40
     

simple_coffee = Coffee()

print(simple_coffee.get_description())
print(simple_coffee.get_cost())


