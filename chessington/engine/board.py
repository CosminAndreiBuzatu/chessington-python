"""
A module providing a representation of a chess board. The rules of chess are not implemented - 
this is just a "dumb" board that will let you move pieces around as you like.
"""

from collections import namedtuple
from enum import Enum, auto

from chessington.engine.pieces import Pawn, Knight, Bishop, Rook, Queen, King

BOARD_SIZE = 8

class Player(Enum):
    """
    The two players in a game of chess.
    """
    WHITE = auto()
    BLACK = auto()


class Square(namedtuple('Square', 'row col')):
    """
    An immutable pair (row, col) representing the coordinates of a square.
    """

    @staticmethod
    def at(row, col):
        return Square(row=row, col=col)


class Board:
    """
    A representation of the chess board, and the pieces on it.
    """

    def __init__(self):
        self.current_player = Player.WHITE
        self.board = Board._create_starting_board()

    @staticmethod
    def _create_starting_board():

        # Create an empty board
        board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        # Setup the rows of pawns
        board[1] = [Pawn(Player.WHITE) for _ in range(BOARD_SIZE)]
        board[6] = [Pawn(Player.BLACK) for _ in range(BOARD_SIZE)]

        # Setup the rows of pieces
        piece_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        board[0] = list(map(lambda piece: piece(Player.WHITE), piece_row))
        board[7] = list(map(lambda piece: piece(Player.BLACK), piece_row))

        return board

    def set_piece(self, square, piece):
        self.board[square.row][square.col] = piece

    def get_piece(self, square):
        return self.board[square.row][square.col]

    def find_piece(self, piece_to_find):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] is piece_to_find:
                    return Square.at(row, col)
        raise Exception('The supplied piece is not on the board')

    def move_piece(self, from_square, to_square):
        moving_piece = self.get_piece(from_square)
        if moving_piece is not None and moving_piece.player == self.current_player:
            self.set_piece(to_square, moving_piece)
            self.set_piece(from_square, None)
            self.current_player = Player.WHITE if self.current_player == Player.BLACK else Player.WHITE