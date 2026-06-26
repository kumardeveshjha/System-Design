from enum import Enum

class TransportMode(Enum):
         WALKING = "walking"
         BIKE = "bike"
         CAR = "car"
          
class TransportService():
     
     def __init__(self,transport_mode:TransportMode):
          self.__transport_mode: TransportMode = transport_mode          
     
     def set_mode(self, new_transport_mode):
          self.__transport_mode: TransportMode = new_transport_mode
          
     def eta(self):
          if self.__transport_mode == TransportMode.WALKING:
               print("Travelling through walking, take 20 minutes")
          
          if self.__transport_mode == TransportMode.BIKE:
               print("Travelling through walking, take 15 minute")
          
          if self.__transport_mode == TransportMode.CAR:
               print("Travelling through CAR, take 10 minute")
          
     
transport_service = TransportService(TransportMode.WALKING)
transport_service.eta()
