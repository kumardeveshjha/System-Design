
class Logger:
     
     def __init__(self,file_name:str):
          self.file_name = file_name
          self.log_count = 0
          
          
     def log(self,accesed_by: str,msg:str):
          print(f"The file {self.file_name} is opened by {accesed_by} with {msg}" )
          self.log_count += 1
          
     
user = Logger("File.txt")
user.log("User", "I want to login")
print(user.log_count)
print(id(user))

#  Staff 

staff_memeber = Logger("File.txt")
staff_memeber.log("Staff", "Access Denied")
print(staff_memeber.log_count)
print(id(staff_memeber))
