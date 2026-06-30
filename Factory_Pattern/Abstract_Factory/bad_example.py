from abc import ABC, abstractmethod

class Food(ABC):
     @abstractmethod
     def prepare_food(self):
          pass
     
# North Indian Food 
     
class PaneerTikka(Food):
     def prepare_food(self):
          print("Preparing Paneer Tikka")
     
class PalakPaneer(Food):
     def prepare_food(self):
          print("Preparing Palak Paneer")
     
class GulabJamun(Food):
     def prepare_food(self):
          print("Preparing Gulab Jamun")
     

# South Inian

class MedhuVada(Food):
     def prepare_food(self):
          print("Preparing Preparing Medhu Vada")
     
class Dosa(Food):
     def prepare_food(self):
          print("Preparing Dosa")
     
class Payasam(Food):
     def prepare_food(self):
          print("Preparing Payasam")
          
#  Chinese cusine


class SpringRoll(Food):
     def prepare_food(self):
          print("Preparing Preparing Spring Roll")
     
class FriedRice(Food):
     def prepare_food(self):
          print("Preparing Fried Rice")
     
class FortuneCoockie(Food):
     def prepare_food(self):
          print("Preparing Saking Fortuning Cookies")
          
# client side interface 

class RestaurantService:
     
   def prepare_meal(self,meal_type:str):
        
        if meal_type == "North Indian":
             starter = PaneerTikka()
             main_corse = PalakPaneer()
             dessart = GulabJamun()
        elif meal_type == "South Indian":
             starter = MedhuVada()
             main_corse = Dosa()
             dessart = Payasam()
        elif meal_type == "Chinese":
             starter = SpringRoll()
             main_corse = FriedRice()
             dessart = FortuneCoockie()
        else: 
             print('Saste Restaurant mei ja')
             
        starter.prepare_food()
        main_corse.prepare_food()
        dessart.prepare_food()
     
          
  
rest_service = RestaurantService()     
rest_service.prepare_meal('North Indian')   
rest_service.prepare_meal('South Indian')   
rest_service.prepare_meal('Chinese')   
rest_service.prepare_meal('Italian')   
