
class Pawn:
    def __init__(self,counter,piece_color,i,j):
        self.counter = counter
        self.piece_color = piece_color
        self.row = i
        self.column = j

    def get_moving_possibility(self):

        if self.row == 1 and self.row <= 7:
            return f'the {self.piece_color} Pawn is in Home and possible moves : ({self.row + 1},{self.column}) or ({self.row + 2},{self.column})'
        elif self.row == 6 and self.row >= 0:
            return f'the {self.piece_color} Pawn is in Home and possible moves : ({self.row - 1},{self.column}) or ({self.row - 2},{self.column})'
        else:
            return f'the {self.piece_color} Pawn is not home and possible moves : ({self.row + 1},{self.column})'




class Rook:
    def __init__(self,counter,piece_color,i,j):
        self.counter = counter
        self.piece_color = piece_color
        self.i = i
        self.j = j
        
    def get_moving_possibility(self):

        return f'the {self.piece_color} Rook possible moves : ({self.row + 1},{self.column})'



class Knight:
    def __init__(self,counter,piece_color,i,j):
        self.counter = counter
        self.piece_color = piece_color
        self.i = i
        self.j = j

    def get_moving_possibility(self):
        pass

class Bishop:
    def __init__(self,counter,piece_color,i,j):
        self.counter = counter
        self.piece_color = piece_color
        self.i = i
        self.j = j

    def get_moving_possibility(self):
        pass

class Queen:
    def __init__(self,counter,piece_color,i,j):
        self.counter = counter
        self.piece_color = piece_color
        self.i = i
        self.j = j

    def get_moving_possibility(self):
        pass

class King:
    def __init__(self,counter,piece_color,i,j):
        self.counter = counter
        self.piece_color = piece_color
        self.i = i
        self.j = j

    def get_moving_possibility(self):
        pass




