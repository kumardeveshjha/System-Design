

import time 
from typing import List

class HighResoImage:
     def __init__(self, image_name):
          self.__image_name = image_name
          self.image_data = None
          
          # loading image form disk which is time consuming process
          self.load_disk_image()
     
     def load_disk_image(self):
          time.sleep(2)
          self.image_data = f"Image data for {self.__image_name}"
          print(f"Loading high resolution image: {self.__image_name} from disk")
          
     def display(self):
          print(f"{self.__image_name} has loaded with the image data{self.image_data}")
          
          
#  Adding  a proxy 

class ProxyImage:
     def __init__(self,file_name):
          self.__file_name = file_name
          self.__real_image = None
          
     def display(self):
          if self.__real_image is None:
              self.__real_image =  HighResoImage(self.__file_name)
          self.__real_image.display()

          
class PhotoGallary:
     def __init__(self):
          self.__image : List[ProxyImage] = []
          
     def add_image(self,image_name):
          proxy_image = ProxyImage(image_name)
          self.__image.append(proxy_image)
          
     def display(self):
          for image in self.__image:
               image.display()
               
     def show_image(self,index:int):
         self.__image[index-1].display()

start_time = time.time()

gallary = PhotoGallary()
gallary.add_image("Image 1")
gallary.add_image("Image 2")
gallary.add_image("Image 3")
gallary.add_image("Image 4")
end_time = time.time()

print(f"{end_time-start_time:.1f}")

print(gallary.show_image(2))