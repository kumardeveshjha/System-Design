# Here is the best practices of Abstract Method in Design Pattern 

from abc import ABC,abstractmethod

class Starter(ABC):
     @abstractmethod
     def prepare_food(self):
          pass
     
class MainCourse(ABC):
     @abstractmethod
     def prepare_food(self):
          pass
     
class Dessart(ABC):
     @abstractmethod
     def prepare_food(self):
          pass
     

# North Indian Food 
     
class PaneerTikka(Starter):
     def prepare_food(self):
          print("Preparing Paneer Tikka")
     
class PalakPaneer(MainCourse):
     def prepare_food(self):
          print("Preparing Palak Paneer")
     
class GulabJamun(Dessart):
     def prepare_food(self):
          print("Preparing Gulab Jamun")
     

# South Inian

class MedhuVada(Starter):
     def prepare_food(self):
          print("Preparing Preparing Medhu Vada")
     
class Dosa(MainCourse):
     def prepare_food(self):
          print("Preparing Dosa")
     
class Payasam(Dessart):
     def prepare_food(self):
          print("Preparing Payasam")
          
#  Chinese cusine


class SpringRoll(Starter):
     def prepare_food(self):
          print("Preparing Preparing Spring Roll")
     
class FriedRice(MainCourse):
     def prepare_food(self):
          print("Preparing Fried Rice")
     
class FortuneCoockie(Dessart):
     def prepare_food(self):
          print("Preparing Saking Fortuning Cookies")
          


# Abstarct Factory class this contains the methods that can be directly implemeted for a Restaurant Services 

class CusineFactory(ABC):
     
     @abstractmethod
     def starter(self)->Starter:
          pass
     
     @abstractmethod
     def starter(self)-> MainCourse:
          pass
     
     @abstractmethod
     def starter(self) -> Dessart:
          pass
          
          
class NorthIndian(CusineFactory):
     
     def starter(self)->Starter:
          return PaneerTikka()
     
     def main_course(self)-> MainCourse:
          return PalakPaneer()
     
     def dessart(self) -> Dessart:
          return GulabJamun()
     
     
class RestaurantService:
     def __init__(self,cusine_type: CusineFactory):
          self.__cusine = cusine_type
          
     def prepare_cusine(self):
          starter = self.__cusine.starter()
          main_course = self.__cusine.main_course()
          dessart = self.__cusine.dessart()
          
          starter.prepare_food()
          main_course.prepare_food()
          dessart.prepare_food()
          
north_indian = NorthIndian()

rest_service = RestaurantService(north_indian)
rest_service.prepare_cusine()