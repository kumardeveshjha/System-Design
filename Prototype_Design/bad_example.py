#  Making a a chess board for the next step board Positions 

from typing import List

class ChessPiece:
     def __init__(self, pieces: str,position:str, color:str):
         self.pieces = pieces
         self.position = position
         self.color = color
         
     def display(self):
          print(f"Pieces: {self.pieces}, Position: {self.position}, Color: {self.color}")
          
          
class ChessBoard:
     def __init__(self):
          self.pieces : List[ChessPiece] = []
          
     def add_pieces(self,pieces:ChessPiece):
          self.pieces.append(pieces)
     
     def display(self):
          print("\n Current Board State")
          for piece in self.pieces:
               piece.display()
               
          

piece_1 = ChessPiece("Pawn", "A2", "White")
piece_2 = ChessPiece("Knight", "B1", "White")
piece_3 = ChessPiece("Bishop", "C1", "White")     
piece_4 = ChessPiece("Rook", "A1", "White")


chess_board = ChessBoard()
chess_board.add_pieces(piece_1)
chess_board.add_pieces(piece_2)
chess_board.add_pieces(piece_3)
chess_board.add_pieces(piece_4)

chess_board.display()

print("______________New Board_________________________")

new_chess_board = ChessBoard()
for p in chess_board.pieces:
     new_chess_board.add_pieces(p)
    
new_chess_board.display()
      
new_chess_board.add_pieces(ChessPiece("Queen", "D1", "White"))

new_chess_board.display()
chess_board.display()