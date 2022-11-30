from Engine.Pieces.Piece import Piece

class Knight(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('knight', symbol, team, row, col, 300)

        self.delta = [
            [-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]