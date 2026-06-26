from transport_mode import TransportMode

class TransportService(TransportMode):
     
     def __init__(self,transport_mode: TransportMode):
          self.__transport_mode: TransportMode = transport_mode
          
     def set_mode(self,new_transport_mode):
          self.__transport_mode = new_transport_mode
          
     def eta(self):
          self.__transport_mode.eta()
          
     def directions(self):
          self.__transport_mode.directions()
          
     