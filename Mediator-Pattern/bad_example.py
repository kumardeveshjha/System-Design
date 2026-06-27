
class Airoplane:
     def __init__(self,flight_name:str,flight_num:str):
          self.__flight_number = flight_num
          self.__flight_name = flight_name
          
     
     def send_message(self,message:str,airoplane:"Airoplane"):
          self.message = message
          print(f"The flight {self.__flight_name}-{self.__flight_number} is sending {self.message} to {airoplane.get_flight}")
          
     def get_flight(self):
          return self.__flight_number
     
     
     
indigo = Airoplane("Indigo","IND12345")
air_india = Airoplane("AIR-INDIA","AIR-34334")

indigo.send_message("Flight is taking off",air_india)