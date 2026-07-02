#  This is a bad example of builder design pattern because it does not separate the construction of a complex object from its representation. 
# Instead, it directly constructs the object in the builder class, which can lead to tight coupling and reduced flexibility.

class Laptop:
     def __init__(self,
                  cpu:str,
                  ram:str,
                  storage : str= None,
                  color: str = None,
                  brand:str = None
                  ):
           self.cpu = cpu
           self.ram = ram
           self.storage = storage 
           self.color = color
           self.brand = brand
           
     def my_laptop(self):
          if self.cpu:
               print(f"My laptop has cpu = {self.cpu}")     
          if self.ram:
               print(f"My laptop has ram = {self.ram}")     
          if self.storage:
               print(f"My laptop has storage = {self.storage}")     
          if self.color:
               print(f"My laptop has color = {self.color}")     
          if self.brand:
               print(f"My laptop has brand = {self.brand}")     
           

l1 = Laptop("i7","18gb",None,"black",None)
l1.my_laptop()