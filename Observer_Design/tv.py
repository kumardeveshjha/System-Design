
from observer import Observer

class TVDisplay(Observer):
     
     def __init__(self):
          self._temp = 0 
     
     def display_Temp(self):
          print(f"The current Temp in TV is {self._temp}")
     
     def update(self,temp):
          self._temp = temp
          print(f"TV temparature updated to {temp}")