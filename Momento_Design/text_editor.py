
from text_momento import TextMomento

class TextEditor:
     
     def __init__(self):
          self.__text = ""
          
     def write(self, text):
          self.__text += text
          
     def getText(self):
          return self.__text
     
     def saveText(self) -> TextMomento:
          momento = TextMomento(self.__text)
          return momento
     
     def restore(self, momento:TextMomento):
          self.__text = momento.getSaveText()