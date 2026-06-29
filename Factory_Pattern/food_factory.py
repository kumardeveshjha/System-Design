#  This is a part of good code practice using the factory pattern 

from abc import ABC, abstractmethod

class Food:
     @abstractmethod
     def prepare_food(self):
          pass
     
     
class Biryani(Food):
     def prepare_food(self):
          print("Preparing Biryani")
     
class Dosa(Food):
     def prepare_food(self):
          print("Preparing Doasa")
          
class Pasta(Food):
     def prepare_food(self):
          print("Preparing pasta")
          
          
class FoodFactroy:
     
     @staticmethod
     def prepare_food(food_type:str):
          if food_type == "dosa":
               d = Dosa()
               return d.prepare_food()
          elif food_type == "biryani":
               b = Biryani()
               return b.prepare_food()
          elif food_type == "pasta":
               b = Pasta()
               return b.prepare_food()
          else:
               return None
          



     