from Engine.Pieces.Piece import Piece

class King(Piece):

    def __init__(self, symbol, team, row, col):
        super().__init__('king', symbol, team, row, col, 1e6)

        self.delta = [
            [0, 1], [1, 0], [0, -1], [-1, 0],
            [-1, -1], [1, 1], [-1, 1], [-1, -1]
        ]