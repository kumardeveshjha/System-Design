
from typing import List
class File:
     def __init__(self,file_name):
          self.__file_name = file_name
          
     def show_details(self):
          print(f"File : {self.__file_name}")
          
               
#  This is the folder class which can consist file but there is issue with the folder and that is it can not have folder 
#  Also we don't know which method belongs to which one that's why it is a bad practice

class Folder:
     def __init__(self,folder_name):
          self.__folder_name = folder_name
          self.__files: List[File] = []
          
     def add_file(self,file_name:File):
          self.__files.append(file_name)
          
     def show_details(self):
          print(f"Folder : {self.__folder_name}")
          for file in self.__files:
               file.show_details()
               

file_1 = File("File 1")
file_2 = File("File 2")
file_3 = File("File 3")

folder = Folder("My Folder")
folder.add_file(file_1)
folder.add_file(file_2)
folder.add_file(file_3)

folder.show_details()