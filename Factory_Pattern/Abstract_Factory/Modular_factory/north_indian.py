
from food_type import Starter, MainCourse,Dessart
from cusine_factory import CusineFactory


class PaneerTikka(Starter):
     def prepare_food(self):
          print("Preparing Paneer Tikka")
     
class PalakPaneer(MainCourse):
     def prepare_food(self):
          print("Preparing Palak Paneer")
     
class GulabJamun(Dessart):
     def prepare_food(self):
          print("Preparing Gulab Jamun")
     
     
class NorthIndian(CusineFactory):
     
     def starter(self)->Starter:
          return PaneerTikka()
     
     def main_course(self)-> MainCourse:
          return PalakPaneer()
     
     def dessart(self) -> Dessart:
          return GulabJamun()
     