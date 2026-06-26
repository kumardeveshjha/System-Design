#  This is the users database reposoitory, which is responsible for handling all database operations related to users.

from LLD.SOLID.SRP.user import User
class UserDB:
     def __init__(self,db,user,password):
          self.db = db
          self.user = user
          self.password = password 
          
     def save_user(self,user:"User"):
          return f"Saving {user.name} to the database"
          