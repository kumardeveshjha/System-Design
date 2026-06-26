#  Single responsibility Primnciple (SRP) --> Bad Example

class User:
     def __init__(self,name,age,email):
          self.name = name
          self.age = age
          self.email = email
     
     def get_user_info(self):
          return f"MY name is {self.name} and I am {self.age} years old. You can contact me at {self.email}"
      
     def is_adult(self) -> bool:
          return self.age > 18    
     
     def save_to_DB(self):
          pass
     
     def delete_from_DB(self):
          pass
     
          
          
          
     