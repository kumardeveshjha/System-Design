from food_type import Starter, MainCourse,Dessart
from cusine_factory import CusineFactory


class SpringRoll(Starter):
     def prepare_food(self):
          print("Preparing Preparing Spring Roll")
     
class FriedRice(MainCourse):
     def prepare_food(self):
          print("Preparing Fried Rice")
     
class FortuneCoockie(Dessart):
     def prepare_food(self):
          print("Preparing Saking Fortuning Cookies")
          