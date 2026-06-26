
# This is a bad exanple of tamplate method 

class FileParser:
     
     def parser(self):
          self.open_file()
          print("Reading the file")
          self.close_file()
     
     def open_file(self):
          print("Opening the file")
          
     def close_file(self):
          print("Closing the file")
          

parser = FileParser()

parser.parser()