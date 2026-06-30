from food_type import Starter, MainCourse,Dessart
from cusine_factory import CusineFactory



class MedhuVada(Starter):
     def prepare_food(self):
          print("Preparing Preparing Medhu Vada")
     
class Dosa(MainCourse):
     def prepare_food(self):
          print("Preparing Dosa")
     
class Payasam(Dessart):
     def prepare_food(self):
          print("Preparing Payasam")
          