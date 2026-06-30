
from abc import ABC,abstractmethod
from food_type import Starter, MainCourse,Dessart

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