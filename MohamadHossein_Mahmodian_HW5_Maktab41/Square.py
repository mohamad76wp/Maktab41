class Square:
    def __init__(self, color, position, piece=None):
        self.color = color
        self.piece = piece
        self.position = position

        # print('color',self.color)
        # print('piece',self.piece)
        # print('position',self.position)

    def set_piece(self, piece):
        self.piece = piece
        # print('f',self.piece)

    def remove_piece(self):
        self.piece = None
