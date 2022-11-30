from Engine.Board import Board
import Engine.Helpers as Helpers
from copy import deepcopy
from Engine.Helpers import *

# This class performs min-max algorithm
class AIEngine:

    def __init__(self, team: str, depth: int):
        self.team = team
        self.depth = depth

    # get max_value on current depth
    # team: black and white
    # alpha: alpha for alpha-beta pruning of minimax algorithm
    # beta: beta for alpha-beta pruning of minimax algorithm
    # returns best move
    def max_value(self, _board: Board, depth: int, team: str, alpha: int, beta: int) -> (float, str):
        # finish search and return the weight of board
        if depth == 0:
            return get_board_wei(_board), None

        value = -1e6
        best_move = None

        # get all available moves
        moves = _board.get_all_moves(team)

        # find the best move
        for move in moves:
            temp = _board.duplicate()
            temp_board = Board(True)
            temp_board.board = deepcopy(temp)

            # make a move
            if temp_board.take_move(move, team, False):
                val, _ = self.min_value(temp_board, depth - 1, get_another_team(team), alpha, beta)

                # update if the move is better than best_move
                if val > value:
                    value = val
                    best_move = move

                # update alpha
                alpha = max(alpha, value)

                if beta <= alpha:
                    return value, best_move

        return value, best_move

    # get min_value on current depth
    # team: black and white
    # alpha: alpha for alpha-beta pruning of minimax algorithm
    # beta: beta for alpha-beta pruning of minimax algorithm
    # returns best move
    def min_value(self, _board: Board, depth: int, team: str, alpha: int, beta: int) -> (float, str):
        # finish search and return the weight of board
        if depth == 0:
            return get_board_wei(_board), None

        value = 1e6
        best_move = None

        moves = _board.get_all_moves(team)

        # find the best move
        for move in moves:
            temp = _board.duplicate()
            new_board = Board(True)
            new_board.board = deepcopy(temp)

            # make a move
            if new_board.take_move(move, team, False):
                val, _ = self.max_value(new_board, depth - 1, get_another_team(team), alpha, beta)

                # update if the move is better than best_move
                if val < value:
                    value = val
                    best_move = move

                # update beta
                beta = min(beta, value)

                if beta <= alpha:
                    return value, best_move

        return value, best_move

    # perfrom minimax algorithm
    def minimax(self, _board: Board) -> str:
        alpha = -1e6
        beta = 1e6

        if self.team == 'black':
            _, best_move = self.min_value(_board, self.depth, 'black', alpha, beta)

        elif self.team == 'white':
            _, best_move = self.max_value(_board, self.depth, 'black', alpha, beta)

        return best_move

    def move(self, _board: Board) -> bool:
        best_move = self.minimax(_board)

        if best_move is not None:
            name = _board.get_piece_name(best_move)
            _board.take_move(best_move, self.team, False)
            print("\nAI: {}({}) moved to {}".format(name, best_move[0:2], best_move[2:4]))

            return True

        return False
