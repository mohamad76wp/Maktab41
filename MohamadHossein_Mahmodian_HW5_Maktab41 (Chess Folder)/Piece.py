
class Pawn:
    def __init__(self, counter, piece_color, i, j):
        self.counter = counter
        self.piece_color = piece_color
        self.row = i
        self.column = j

    def get_moving_possibility(self):

        if self.row == 1 and self.row <= 7:
            return f'the {self.piece_color} Pawn is in Home and possible moves : ({self.row + 1},{self.column}) or ' \
                   f'({self.row + 2},{self.column})'
        elif self.row == 6 and self.row >= 0:
            return f'the {self.piece_color} Pawn is in Home and possible moves : ({self.row - 1},{self.column}) or ' \
                   f'({self.row - 2},{self.column})'
        else:
            return f'the {self.piece_color} Pawn is not home and possible moves : ({self.row + 1},{self.column})'


class Rook:
    def __init__(self, counter, piece_color, i, j):
        self.counter = counter
        self.piece_color = piece_color
        self.row = i
        self.column = j
        
    def get_moving_possibility(self):

        dimention_list = list()
        if self.row == 0 and self.column == 0:
            for counter in range(0,8):
                dimention = (self.row + counter,self.column)
                dimention_list.append(dimention)

            for counter in range(0,8):
                dimention = (self.row,self.column + counter)
                dimention_list.append(dimention)

            return f'the {self.piece_color} Rook is in home and possible moves : {dimention_list} '

        elif self.row == 7 and self.column == 7:

            for counter in range(0,8):
                dimention = (self.row - counter,self.column)
                dimention_list.append(dimention)

            for counter in range(0,8):
                dimention = (self.row,self.column - counter)
                dimention_list.append(dimention)


            return f'the {self.piece_color} Rook is in home and possible moves : {dimention_list} '

        else: # This part is not reachable becuse the rook is not out of home
            possessive_value_row = self.row - 7
            possessive_value_column = self.column - 7
            print(possessive_value_row)
            print(possessive_value_column)

            negative_value_row = self.row - 0
            negative_value_column = self.column - 0
            print(negative_value_row)
            print(negative_value_column)

            for counter in range(self.row,possessive_value_row + 1):
                dimention = (self.row - counter,self.column)
                dimention_list.append(dimention)

            for counter in range(self.column , possessive_value_column - 1 ):
                dimention = (self.row,self.column - counter)
                dimention_list.append(dimention)

            return f'the {self.piece_color} ook is not in home and possible moves : {dimention_list}'



class Knight:
    def __init__(self, counter, piece_color, i, j):
        self.counter = counter
        self.piece_color = piece_color
        self.i = i
        self.j = j

    def get_moving_possibility(self):
        pass


class Bishop:
    def __init__(self, counter, piece_color, i, j):
        self.counter = counter
        self.piece_color = piece_color
        self.i = i
        self.j = j

    def get_moving_possibility(self):
        pass


class Queen:
    def __init__(self, counter, piece_color, i, j):
        self.counter = counter
        self.piece_color = piece_color
        self.i = i
        self.j = j

    def get_moving_possibility(self):
        pass


class King:
    def __init__(self, counter, piece_color, i, j):
        self.counter = counter
        self.piece_color = piece_color
        self.i = i
        self.j = j

    def get_moving_possibility(self):
        pass




