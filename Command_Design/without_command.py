#  here is the example for Low Level Design Of command Pattern

class Chef:
     
     def cook_burger():
          print("Chef is making Burger")
     
     def cook_pizza():
          print("Chef is making pizza")
          
          
class Waiter:
     
     def __init__(self, order: str): 
          self.__order = order
          
     
     def order(self,order):
        if self.__order == "Burger":
             return Chef.cook_burger()
        elif self.__order == "Pizza":
             return Chef.cook_pizza()    
     
     
chef = Chef()
waiter = Waiter("Burger")

waiter.order("Burger")