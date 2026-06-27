

class Logger:
     __instance = None
     
     def __new__(cls,file_name: str):
           if cls.__instance == None:
                cls.__instance = super().__new__(cls)
                cls.__instance.file_name = file_name
                cls.__instance.log_count = 0
                return cls.__instance
           else:
                return cls.__instance
           
     def log(self,msg:str):
          print(f"{msg} is opening the file")
          self.log_count += 1 
          
     def get_log_count(self):
          return self.log_count
          
          
          
instance_1 = Logger("Same.txt")  
instance_1.log("I am the instance 1")
print(f" instance_1 = {id(instance_1)}")

instance_2 = Logger("Same.txt")
instance_2.log("Instance_2")
print(f" instance_2 = {id(instance_2)}")

instance_3 = Logger("Same.txt")
instance_3.log("instance 3")
print(f" Intance 3 = {id(instance_3)}")
print(instance_1.get_log_count())
print(instance_2.get_log_count())
print(instance_3.get_log_count())