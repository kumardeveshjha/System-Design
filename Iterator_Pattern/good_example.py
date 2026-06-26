from abc import ABC, abstractmethod
from typing import List

class Song:
     def __init__(self,title:str):
          self.__title = title
          
     def get_title(self):
          return self.__title
     
     
class Iterator(ABC):
     
     @abstractmethod
     def has_next(self) -> bool:
          pass
     
     def next(self):
          pass
     
class PlaylistIterator(Iterator):
     def __init__(self,song_list:List[Song]):
          self.__playlist = song_list
          self.__position:int = 0
          
     def has_next(self):
          if self.__position<len(self.__playlist):
               return True
          else:
               return False
          
     def next(self)-> Song|None:
          while self.has_next() ==True:
               song = self.__playlist[self.__position]
               self.__position +=1 
               return song
          else:
               None

class Playlist:
     def __init__(self):
          self.__playlist:List[Song] = []
          
     def add_song(self,song:Song):
          self.__playlist.append(song)
     
     def create_iterator(self) -> PlaylistIterator:
          return PlaylistIterator(self.__playlist)
               
               
playlist = Playlist()
playlist.add_song(Song("Hi i am dev jackson"))
playlist.add_song(Song("Hey call me dev jackson"))
playlist.add_song(Song("Hello this is dev jackson"))

iterator = playlist.create_iterator()

while iterator.has_next():
     print(iterator.next().get_title())