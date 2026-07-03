#  This is the good example for implementing the chess board using the prototype design pattern

from typing import List
import copy 

class ChessPiece:
     def __init__(self,pieces:str,position:str,color:str):
          self.pieces = pieces
          self.position = position
          self.color = color
          
     def display(self):
          print(f"Pieces: {self.pieces}, Position: {self.position}, Color: {self.color}")
       
     # def clone(self):
     #      return copy.deepcopy(self)   

class ChessBoard:
     def __init__(self):
          self.pieces: List[ChessPiece] = []
          
     def add_pieces(self,piece:ChessPiece):
          self.pieces.append(piece)
          
     def display(self):
          print("Chess Board Positions")
          for piece in self.pieces:
               piece.display()
     
     def clone(self):
          return copy.copy(self)

piece_1 = ChessPiece("Pawn", "A2", "White")
piece_2 = ChessPiece("Knight", "B1", "White")
piece_3 = ChessPiece("Bishop", "C1", "White")     

chess_board = ChessBoard()
chess_board.add_pieces(piece_1)
chess_board.add_pieces(piece_2)    
chess_board.add_pieces(piece_3)

chess_board.display()

print("______________New Board_________________________")

new_chess_board = chess_board.clone()
new_chess_board.display()
new_chess_board.add_pieces(ChessPiece("Queen", "D1", "White"))
chess_board.display()
new_chess_board.display()