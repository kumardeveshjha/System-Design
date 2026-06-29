#  Restaurant service Page 

from abc import ABC, abstractmethod

class Food:
     @abstractmethod
     def prepare_food(self):
          pass
     

class Biryani:
     def prepare_food(self):
          print("Preparing Biryani")
     
class Dosa:
     def prepare_food(self):
          print("Preparing Doasa")
     
     
# Client facing interface class 

class RestaurantServices:
     
     def ordered_food(self,food_type:str):
          
          if food_type == "Dosa":
               f = Dosa()
          elif food_type == "Biryani":
               f = Biryani()
          else:
               print("Please check the menu properly")
          
          f.prepare_food()
          return f
     
restaurant_order = RestaurantServices()
restaurant_order.ordered_food("Dosa")
               
          
          