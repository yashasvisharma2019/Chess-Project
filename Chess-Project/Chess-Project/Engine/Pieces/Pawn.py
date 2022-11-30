from Engine.Pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, symbol, team, row, col):
        super().__init__('pawn', symbol, team, row, col, 100)

        self.delta = [
            [-1, 0], [-2, 0], [-1, 1], [-1, -1]]

    def remove_two_step_move(self):
        if [2, 0] in self.delta:
            self.delta.remove([2, 0])

        if [-2, 0] in self.delta:
            self.delta.remove([-2, 0])
