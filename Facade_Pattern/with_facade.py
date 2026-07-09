

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
     
     def user_order(self,order_id:str,users_id:User):
          self.__order_id = order_id
          self.__user_id  = users_id.user_id()
          order = {"order_id":self.__order_id, "user_id": self.__user_id }
          self.__orders.append(order)
          print(f"Order Placed for the user {self.__user_id}")
          
          return self.__orders

     
class Gateway:
     def __init__(self):
          self.__user_service= User()
          self.__order_service = Order()
          
     def user_login(self,user_name,password):
          return self.__user_service.user_login(user_name,password)
          
     def user_details(self):
          return self.__user_service.user_details()
          
     def order_service(self,order_id):
          user_id = self.__user_service
          return self.__order_service.user_order(order_id,user_id)
          
     def total_details(self,user_name,password,order_id):
          print(self.user_login(user_name,password))
          print(self.user_details())
          print(self.order_service(order_id))
     
     
api_gateway = Gateway()
# print(api_gateway.user_login("Dev","dev-123"))
# print(api_gateway.user_details())
# api_gateway.order_service("order-123")

api_gateway.total_details("Devesh_2","Dev_123","Dev_order_123")
api_gateway.total_details("Devesh_3","Dev_1234","Dev_order_1234")
api_gateway.total_details("Devesh_4","Dev_1235","Dev_order_1235")
api_gateway.total_details("Devesh_5","Dev_1236","Dev_order_1236")



