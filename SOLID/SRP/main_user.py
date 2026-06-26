#  User main file 

from LLD.SOLID.SRP.user import User 
from LLD.SOLID.SRP.user_DB_repo import UserDB

# Creating the User Object 
user1 = User("Devesh",25,"myloda@gmail.com")

#  Creating a Database Object
user_db = UserDB("localhost","root","password")

# Passing values to the user Object and calling the method
print(user1.get_user_info())
print(user1.is_adult())

# Paasing the user 1 reference to the database class to save the user in the datbase 
print(user_db.save_user(user1))