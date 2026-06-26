from abc import ABC, abstractmethod


class FileParser(ABC):
     
     def parse_file(self):
          self.open_file()
          self.file_parse()
          self.close_file()
     
     def open_file(self):
          print("Opening the File")
          
     def close_file(self):
          print("Printing the File")
          
     
     @abstractmethod
     def file_parse(self):
          pass
          


class PdfParser(FileParser):
     
     def file_parse(self):
          print("PDF file is being parsed")
     
class CSVParser(FileParser):
     def file_parse(self):
          print("CSV File is being parsed")
          
class HTMLParser(FileParser):
     def file_parse(self):
          print("HTML File is being parsed")
          
          
          
pdf_parser = PdfParser()
csv_parser = CSVParser()
html_parser = HTMLParser()
pdf_parser.parse_file()
csv_parser.parse_file()
html_parser.parse_file()


