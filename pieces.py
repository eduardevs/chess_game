from enum import Enum
from pydantic import BaseModel

# idea color negative, or positive
class PIECES_COLORS(Enum):
    WHITE = 'white'
    BLACK = 'black'

class PIECES_VALUES(Enum):
    PAWN = 1
    KNIGHT = 3
    BISHOP = 3
    ROOK = 5
    QUEEN = 9
    KING = 10


class ChessPiece(BaseModel):
    color:PIECES_COLORS = None
    # moves ? here ?

class Pawn(ChessPiece):
    move: 'step'
    # moves one step forward
    def makeMove():
        pass




class Knigth(ChessPiece):
    # moves in L
    move: 'L'
    pass

class Bishop(ChessPiece):
    # moves vertical
    pass

class Rook(ChessPiece):
    # moves horizontal
    pass

class Queen(ChessPiece):
    pass

class King(ChessPiece):
    pass

# class ChessBoard(:
#     pass



