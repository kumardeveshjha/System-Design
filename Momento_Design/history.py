

from text_momento import TextMomento
from text_editor import  TextEditor
from typing import List

     
class History:
     
     def __init__(self):
          self.__momento_list: List[TextMomento] = []
          self.__current_index = -1
         
          
     def addMomento(self, momento: TextMomento):
          self.__momento_list.append(momento)
          
     
     def getHistory(self):
          for i in range(len(self.__momento_list)):
               print(f"{i} : {self.__momento_list[i].getSaveText()}")
            
     def undo(self) -> TextMomento:
          if len(self.__momento_list) > 0:
               self.__momento_list.pop()
               if len(self.__momento_list) == 0:
                    return TextMomento("")
               return self.__momento_list[-1]
          else:
               return None
          

          
     