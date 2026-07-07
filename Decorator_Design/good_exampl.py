
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
          return "Plain Coffeee"
     
     def get_cost(self):
          return 20
     
     
class AddorDecorator(Bevarage):
     def __init__(self,coffee: Coffee):
          self._coffee = coffee
          
     def get_description(self):
          pass
     
     def get_cost(self):
          pass
     

     
class CoffeeWithMilk(AddorDecorator):
     def get_description(self):
          return self._coffee.get_description() + " With Milk"
     def get_cost(self):
          return self._coffee.get_cost() + 20
     
class CoffeeWithMilkAndSugar(AddorDecorator):
     def get_description(self):
          return self._coffee.get_description() + " With Milk and Sugar"
     def get_cost(self):
          return self._coffee.get_cost() + 40
     
     
class CoffeeWithTopCream(AddorDecorator):
     def get_description(self):
          return self._coffee.get_description() + " With Top Cream"
     def get_cost(self):
          return self._coffee.get_cost() + 140
     
     
 
coffee = Coffee()     
milk_coffee = CoffeeWithMilk(coffee)
milk_coffee.get_cost()


