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
     