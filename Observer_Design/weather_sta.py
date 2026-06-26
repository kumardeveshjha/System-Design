
from observer import Observer
from typing import List

class WeatherStation(Observer):
     
     def __init__(self):
          self.__temprature = 0
          self._observer : List[Observer] = []
          
     def new_observer(self, new_observer: Observer):
          self._observer.append(new_observer)
     
     def remove_observer(self,ob: Observer):
          self._observer.remove(ob)
          
     def update_Temp(self,new_temp):
          self.__temprature = new_temp
          self.notify_observer()
     
     def display_temp(self,ob:Observer):
         obj = ob(self.__temprature)
         return obj
                   
     def notify_observer(self):
          for observer in self._observer:
               observer.update(self.__temprature)