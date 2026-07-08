#  This is the good example for a Composite Pattern 
from abc import ABC, abstractmethod
from typing import List

# Making an Interface for the files and Folders to implement the features required 
# This will make sure that there will not need to specify the type whether it is a fileor folder 
# A dditionally it also helps in maintaing the structure of the folder 


class FileSystemComponent(ABC):
     
     @abstractmethod
     def show_details(self):
          pass


class File(FileSystemComponent):
     def __init__(self,file_name):
          self.__file_name = file_name
          
     def show_details(self):
          print(f"File : {self.__file_name}")
          
               

class Folder(FileSystemComponent):
     def __init__(self,folder_name):
          self.__folder_name = folder_name
          self.__components: List[FileSystemComponent] = []
          
     def add_file(self,component:FileSystemComponent):
          self.__components.append(component)
          
     def show_details(self):
          print(f"Folder : {self.__folder_name}")
          for component in self.__components:
               component.show_details()
               

file_1 = File("File 1")
file_2 = File("File 2")
file_3 = File("File 3")

sub_folder = Folder("Sub Folder")
sub_folder.add_file(file_1)
sub_folder.add_file(file_2)
sub_folder.add_file(file_3)

video_file = File('Video.mkv')
audio_file = File('Audio.mkv')

main_folder = Folder("Main Folder")
main_folder.add_file(video_file)
main_folder.add_file(audio_file)
main_folder.add_file(sub_folder)

main_folder.show_details()