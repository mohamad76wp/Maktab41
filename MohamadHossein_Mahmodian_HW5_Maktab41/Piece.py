
class Pawn:
    def __init__(self,  counter,  piece_color,  i,  j):
        self.counter = counter
        self.piece_color = piece_color
        self.row = i
        self.column = j

    def get_moving_possibility(self):

        if self.row == 1 and self.row <= 7:
            return f'the {self.piece_color} Pawn is in Home and possible moves : ({self.row + 1}, {self.column}) or ' \
                   f'({self.row + 2}, {self.column})'
        elif self.row == 6 and self.row >= 0:
            return f'the {self.piece_color} Pawn is in Home and possible moves : ({self.row - 1}, {self.column}) or ' \
                   f'({self.row - 2}, {self.column})'
        else:
            return f'the {self.piece_color} Pawn is not home and possible moves : ({self.row + 1}, {self.column})'


class Rook:
    def __init__(self,  counter,  piece_color,  i,  j):
        self.counter = counter
        self.piece_color = piece_color
        self.row = i
        self.column = j
        
    def get_moving_possibility(self):

        dimention_list = list()
        if self.row == 0 and self.column == 0:
            for counter in range(0, 8):
                dimention = (self.row + counter, self.column)
                dimention_list.append(dimention)

            for counter in range(0, 8):
                dimention = (self.row, self.column + counter)
                dimention_list.append(dimention)

            return f'the {self.piece_color} Rook is in home and possible moves : {dimention_list} '

        elif self.row == 7 and self.column == 7:

            for counter in range(0, 8):
                dimention = (self.row - counter, self.column)
                dimention_list.append(dimention)

            for counter in range(0, 8):
                dimention = (self.row, self.column - counter)
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

            for counter in range(self.row, possessive_value_row + 1):
                dimention = (self.row - counter, self.column)
                dimention_list.append(dimention)

            for counter in range(self.column ,  possessive_value_column - 1 ):
                dimention = (self.row, self.column - counter)
                dimention_list.append(dimention)

            return f'the {self.piece_color} Rook is not in home and possible moves : {dimention_list}'



class Knight:
    def __init__(self,  counter,  piece_color,  i,  j):
        self.counter = counter
        self.piece_color = piece_color
        self.row = i
        self.column = j

    def get_moving_possibility(self):
        if self.row == 0 and self.column == 1:
            return f'The {self.piece_color} Knight 1 is in Home and possible moves :({self.row + 2 }, ' \
                   f'{self.column + 1}) or ({self.row + 2}, {self.column - 1}) or ({self.row + 1}, {self.column + 2})'

        elif self.row == 0 and self.column == 6:
            return f'The {self.piece_color} Knight 2 is in Home and possible moves :({self.row + 2}, ' \
                   f'{self.column + 1}) or ({self.row + 2}, {self.column - 1}) or ({self.row + 1}, {self.column - 2})'
        
        elif self.row == 7 and self.column == 1: 
            return f'The {self.piece_color} Knight 1 is in Home and possible moves :({self.row - 2 }, ' \
                   f'{self.column + 1}) or ({self.row - 2}, {self.column - 1}) or ({self.row - 1}, {self.column + 2})'

        elif self.row == 7 and self.column == 6:
            return f'The {self.piece_color} Knight 2 is in Home and possible moves :({self.row - 2}, ' \
                   f'{self.column + 1}) or ({self.row - 2}, {self.column - 1}) or ({self.row - 1}, {self.column - 2})'
              
        else:
            top = f'({self.row + 2}, {self.column + 1}) or ({self.row + 2}, {self.column - 1})'
            right = f'({self.row - 2}, {self.column + 1}) or ({self.row + 2}, {self.column - 1})'
            down =  f'({self.row + 1}, {self.column - 2}) or ({self.row - 1}, {self.column - 2})'
            left = f'({self.row + 1}, {self.column + 2}) or ({self.row - 1}, {self.column + 2})'

            return f'The {self.piece_color} Knight is not in Home and possible moves :' \
                   f'{top} or {right} or {down} or {left}'


class Bishop:
    def __init__(self,  counter,  piece_color,  i,  j):
        self.counter = counter
        self.piece_color = piece_color
        self.row = i
        self.column = j

    def get_moving_possibility(self):
        if self.row == 0 and self.column == 2 or self.column == 5:
            return f'The {self.piece_color} Bshop is in home and possible moves :({self.row + 1}, {self.column + 1}) or ({self.row + 1}, {self.column - 1})'

        elif self.row == 7 and self.column == 2 or self.column == 5:
            return f'The {self.piece_color} Bshop is in home and possible moves :({self.row - 1}, {self.column + 1}) or ({self.row - 1}, {self.column - 1})'
        
        else:
            top = f'({self.row + 1}, {self.column + 1}) or ({self.row + 1}, {self.column - 1})'
            right = f'({self.row + 1}, {self.column + 1}) or ({self.row - 1}, {self.column + 1})'
            down = f'({self.row - 1}, {self.column + 1}) or ({self.row - 1}, {self.column - 1})'
            left = f'({self.row + 1}, {self.column - 1}) or ({self.row - 1}, {self.column - 1})'

            return f'The {self.piece_color} Bishop is not in Home and possible moves :{top} or {right} or {down} or {left}'

class Queen:
    def __init__(self,  counter,  piece_color,  i,  j):
        self.counter = counter
        self.piece_color = piece_color
        self.row = i
        self.column = j

    def get_moving_possibility(self):
        if self.row == 0 and self.column == 3:
            return f'The {self.piece_color} Queen is in home ann possible moves: ({self.row + 1}, {self.column}) or ({self.row + 1}, {self.column + 1}) or ({self.row + 1}, {self.column - 1}) or ({self.row}, {self.column + 1}) or ({self.row}, {self.column - 1})'

        elif self.row == 7 and self.column == 3:
            return f'The {self.piece_color} Queen is in home ann possible moves: ({self.row - 1}, {self.column}) or ({self.row - 1}, {self.column + 1}) or ({self.row - 1}, {self.column - 1}) or ({self.row}, {self.column + 1}) or ({self.row}, {self.column - 1})'

        else:
            rowPlus = self.row
            columnPlus = self.column

            rowMines= self.row
            columnMines = self.column

            while columnPlus < 8 > columnPlus:
                rowPlus = self.row + 1
                columnPlus = self.column + 1

                top = (rowPlus, self.column)
                right = (self.row, columnPlus)
                upOrib = (rowPlus, columnPlus)
                downOrib = (rowMines, columnPlus)

            moves1 = [top, right, upOrib, downOrib]
            while rowMines < 8 > columnMines:

                rowMines= self.row - 1
                columnMines = self.column - 1

                down = (rowMines, self.column)
                left = (self.row, columnMines)
                upXOrib = (rowPlus, columnMines)
                downXOrib = (rowMines, columnMines)
            moves2 = [down, left, upXOrib, downXOrib]
            
            return [moves1, moves2]



class King:
    def __init__(self,  counter,  piece_color,  i,  j):
        self.counter = counter
        self.piece_color = piece_color
        self.row = i
        self.column = j

    def get_moving_possibility(self):
        if self.row == 0 and self.column == 3:
            return f'The {self.piece_color} King is in home ann possible moves: ({self.row + 1}, {self.column}) or ' \
                   f'({self.row + 1}, {self.column + 1}) or ({self.row + 1}, {self.column - 1}) or ({self.row}, ' \
                   f'{self.column + 1}) or ({self.row}, {self.column - 1})'

        elif self.row == 7 and self.column == 3:
            return f'The {self.piece_color} king is in home ann possible moves: ({self.row - 1}, {self.column}) or ' \
                   f'({self.row - 1}, {self.column + 1}) or ({self.row - 1}, {self.column - 1}) or ({self.row}, ' \
                   f'{self.column + 1}) or ({self.row}, {self.column - 1})'

        else:
            rowPlus = self.row
            columnPlus = self.column

            rowMines= self.row
            columnMines = self.column

            while columnPlus < 8 > columnPlus:
                rowPlus = self.row + 1
                columnPlus = self.column + 1

                top = (rowPlus, self.column)
                right = (self.row, columnPlus)
                upOrib = (rowPlus, columnPlus)
                downOrib = (rowMines, columnPlus)

                moves1 = [top, right, upOrib, downOrib]
            while rowMines < 8 > columnMines:

                rowMines= self.row - 1
                columnMines = self.column - 1

                down = (rowMines, self.column)
                left = (self.row, columnMines)
                upXOrib = (rowPlus, columnMines)
                downXOrib = (rowMines, columnMines)
                moves2 = [down, left, upXOrib, downXOrib]
            
            return [moves1, moves2]





