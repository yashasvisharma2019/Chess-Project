from copy import deepcopy
from Engine.Helpers import *

class Piece:
    delta = []

    def __init__(self, name, symbol, team, row, col, pts):
        self.name = name
        self.symbol = symbol
        self.team = team
        self.row = row
        self.col = col
        self.pts = pts
        self.has_moved = False

    def set_pos(self, r, c):
        self.row = r
        self.col = c

    def get_moves(self, _board):
        delta = []

        # go through every move available for this piece
        for move in self.delta:
            row = self.row
            col = self.col

            # potential location to move to
            new_row = row + move[0]
            new_col = col + move[1]

            # check that destination is not out of range
            if _board.check_in_range(new_row, new_col):
                # check that initial location is not empty
                if not _board.check_cell_empty(row, col):
                    # check that the move is possible for that piece
                    if _board.check_move_possible(self, new_row, new_col):
                        # check that there are no team-mates at destination
                        if not _board.check_ally_at_dest(self, new_row, new_col):
                            # check that there are no team-mates blocking the path
                            if not _board.check_piece_in_path(self, new_row, new_col):
                                # form string representation of the move
                                move = get_move_pos(row, col, new_row, new_col)

                                # add to our list
                                if move not in delta:
                                    delta.append(move)

        return delta

    def duplicate(self):
        _dup = deepcopy(self)
        _dup.name = deepcopy(self.name)
        _dup.symbol = deepcopy(self.symbol)
        _dup.team = deepcopy(self.team)
        _dup.row = deepcopy(self.row)
        _dup.col = deepcopy(self.col)
        _dup.pts = deepcopy(self.pts)
        _dup.has_moved = deepcopy(self.has_moved)
        _dup.delta = deepcopy(self.delta)

        return deepcopy(_dup)