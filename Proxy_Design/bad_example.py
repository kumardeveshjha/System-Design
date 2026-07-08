#  Building a Photo Gallary without proxy design pattern 
#  This method takes time for the image to load from the disk 



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
          
          
class PhotoGallary:
     def __init__(self):
          self.__image : List[HighResoImage] = []
          
     def add_image(self,image_name):
          high_reso_image = HighResoImage(image_name)
          self.__image.append(high_reso_image)
          
     def display(self):
          for image in self.__image:
               image.display()
               

gallary = PhotoGallary()
gallary.add_image("Image 1")
gallary.add_image("Image 2")
gallary.add_image("Image 3")
gallary.add_image("Image 4")

gallary.display()
