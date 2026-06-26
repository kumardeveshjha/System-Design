
from typing import List

class Song:
     def __init__(self,title:str):
          self.__title:str = title
          
     def get_title(self):
          return self.__title 

class Playlist:
     def __init__(self):
          self.__playlist:List[Song] = []
               
     def add_song(self,song:Song):
          self.__playlist.append(song)
          
     def get_playlist(self):
          return self.__playlist
     
playlist = Playlist()

playlist.add_song(Song("This is rockstar Devesh Kumar"))
playlist.add_song(Song("This is rockstar Devendra Kumar"))
playlist.add_song(Song("This is rockstar Dev Kumar"))


for i in range(len(playlist.get_playlist())):
     print(playlist.get_playlist()[i].get_title())     
          
          