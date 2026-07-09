

from typing import List


class User:
     
     def __init__(self):
          self.__user_name = None
          self.__password = None
          
          self.user_id()
     
     def user_login(self,user_name:str,password:str):
          self.__user_name = user_name
          self.__password = password
          print("user Succeessfully Login")
          return {f"Login with {self.__user_name} and password {self.__password}"}
         
     def user_details(self):
         print("User Details .....")
         return {"username":self.__user_name, "password":self.__password}
    
     def user_id(self):
          return f"{self.__user_name} + {self.__password}"
    
    
class Order:
     
     def __init__(self):
          self.__order_id = None
          self.__user_id = None
          self.__orders : List[{self.__order_id,self.__user_id}] = []
     
     def user_order(self,order_id:str,user_id:User):
          self.__order_id = order_id
          self.__user_id  = user_id.user_id()
          order = {"order_id":self.__order_id, "user_id": self.__user_id }
          self.__orders.append(order)
          print(f"Order Placed for the user {self.__user_id}")
          
          return self.__orders

     
class Gateway:
     def __init__(self):
          self.__user_service= User()
          self.__order_service = Order()
          
     def user_login(self,user_name,password):
          self.__user_service.user_login(user_name,password)
          
     def user_details(self):
          self.__user_service.user_details()
          
     def order_service(self,order_id,user_id):
          self.__order_service.user_order(order_id,user_id)
          
     
     


api_gateway = Gateway()
login = api_gateway.user_login("Dev",'12435ghji')
api_gateway.user_details()

api_gateway.order_service("Order-123",login)