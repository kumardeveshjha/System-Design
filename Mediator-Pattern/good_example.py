
from abc import ABC, abstractmethod
from typing import List


class AirTrafficController(ABC):
     
     @abstractmethod 
     def register_plane(self):
          pass
     
     @abstractmethod
     def send_mesage(self):
          pass
  
     
class ControlTower(AirTrafficController):
     
     def __init__(self):
          self.__airplanes: List["Airplane"] = []
     def register_plane(self,new_airplane:"Airplane"):
          self.__airplanes.append(new_airplane) 
     
     def send_mesage(self,msg:str,sender:"Airplane"):
          for flight in self.__airplanes:
               if flight != sender:
                    flight.receive_message(msg,sender)
               
     
class Airplane:
     
     def __init__(self,flight_number:str,tower:"ControlTower"):
          self.__flight_number = flight_number
          self.__tower = tower
          self.__tower.register_plane(self)
          
     def send_message(self,msg:str):
          self.__tower.send_mesage(msg,self)
          
     def get_flight(self) -> str:
          return self.__flight_number
     
     def receive_message(self,msg:str,send_by:"Airplane"):
          print(f"Flight {self.__flight_number} recieve {msg} from {send_by.get_flight()}")
          
control_tower = ControlTower()
jet_air = Airplane("JET-1234",control_tower)
indigo = Airplane("IND-12234",control_tower)
air_india = Airplane("AIR-4455",control_tower)
air_dev = Airplane("DEV-12345",control_tower)
air_india.send_message("This is time to do bomb blast")
