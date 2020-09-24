from Square import Square
from Piece import Pawn
from Piece import Rook
from Piece import Knight
from Piece import Bishop
from Piece import Queen
from Piece import King


class Board:
    color_numbers = {0: "white",1: "black"}

    def __init__(self):
        self.square_dict = {(i, j): Square(color=self.color_numbers[(i+j) % 2], position=(i, j)) for i in range(8) for j in range(8)}
        print('hi')
    def reset_pieces_on_board(self):
        # remove all pieces --------------------------
        for this_square in self.square_dict.values():
            this_square.remove_piece()

        # set white pieces -----------------------------
        for j in range(8):
            self.square_dict[(1, j)].set_piece(Pawn(j, "white", 1, j))

        self.square_dict[(0, 0)].set_piece(Rook(1, "white", 0, 0))
        self.square_dict[(0, 7)].set_piece(Rook(2, "white", 0, 7))
        self.square_dict[(0, 1)].set_piece(Knight(1, "white", 0, 1))
        self.square_dict[(0, 6)].set_piece(Knight(2, "white", 0, 6))
        self.square_dict[(0, 2)].set_piece(Bishop(1, "white", 0, 2))
        self.square_dict[(0, 5)].set_piece(Bishop(2, "white", 0, 5))
        self.square_dict[(0, 3)].set_piece(Queen(1, "white", 0, 3))
        self.square_dict[(0, 4)].set_piece(King(1, "white", 0, 4))

        # set black pieces -----------------------------
        for j in range(8):
            self.square_dict[(6, j)].set_piece(Pawn(j, "Black", 6, j))

        self.square_dict[(7, 0)].set_piece(Rook(1, "black", 7, 0))
        self.square_dict[(7, 7)].set_piece(Rook(2, "black", 7, 7))
        self.square_dict[(7, 1)].set_piece(Knight(1, "black", 7, 1))
        self.square_dict[(7, 6)].set_piece(Knight(2, "black", 7, 6))
        self.square_dict[(7, 2)].set_piece(Bishop(1, "black", 7, 2))
        self.square_dict[(7, 5)].set_piece(Bishop(2, "black", 7, 5))
        self.square_dict[(7, 3)].set_piece(Queen(1, "black", 7, 3))
        self.square_dict[(7, 4)].set_piece(King(1, "black", 7, 4))

        return self.square_dict

    def move_piece(self, old_position, new_position):
        my_piece = self.square_dict[old_position].piece
        print(type(my_piece))
        if my_piece:
            movement_list = my_piece.get_moving_possibility()

            if new_position in movement_list:
                self.square_dict[new_position].set_piece(my_piece)
                my_piece.get_piece_coordinate(new_position[0], new_position[2])
                self.square_dict[old_position].remove_piece()
                return "done"

            else:
                return "error"

        else:
            return "error"

    def show_board(self):
        board = []
        for i in range(8):
            board.append(["", "", "", "", "", "", "", ""])

        for i in range(8):
            for j in range(8):
                pass



my_board = Board()
my_board.reset_pieces_on_board()
print(my_board.move_piece((0,3),(0,2)))
# print(my_board.square_dict[(0, 0)].piece.piece_color)
