#  Here  I am using  the builder patter to implement the Laptop Class.

class Laptop:
     processor = None
     ram = None
     storage = None
     color = None
     brand = None
     
class LaptopBuilder:
     def __init__(self):
          self.__laptop = Laptop()
          
     def processor(self,processor:str):
          self.__laptop.processor = processor
          return self
     def ram(self,ram:str):
          self.__laptop.ram = ram
          return self
     def storage(self,storage:str):
          self.__laptop.storage = storage
          return self
     def color(self,color:str):
          self.__laptop.color = color
          return self
     def brand(self,brand:str):
          self.__laptop.brand = brand
          return self
     def build(self):
          return self.__laptop
     
     
l1 = LaptopBuilder().ram("16").storage("512GB").color("Black").brand("Dell")


print(l1.build().ram)