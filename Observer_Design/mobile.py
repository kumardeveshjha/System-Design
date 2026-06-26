
from observer import Observer

class MobileDisplay(Observer):
     
     def __init__(self):
          self._temp = 0 
     
     def display_Temp(self):
          print(f"The current Temp in mobile is {self._temp}")
     
     def update(self,temp):
          self._temp = temp
          print(f" Mobile display temparature updated to {temp}")