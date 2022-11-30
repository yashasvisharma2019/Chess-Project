import random
import sys
from Engine.Pieces.Piece import Piece
from Engine.Pieces.Rook import Rook
from Engine.Pieces.Bishop import Bishop
from Engine.Pieces.King import King
from Engine.Pieces.Knight import Knight
from Engine.Pieces.Pawn import Pawn
from Engine.Pieces.Queen import Queen
from Engine.Helpers import *
from copy import deepcopy
from termcolor import colored

# chess board class
class Board:
    black_pieces = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜', '♟']
    white_pieces = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖', '♙']
    castling_left = False
    castling_right = False
    board = []
    board_size = 8

    def __init__(self, b_skip):
        if not b_skip:
            for i in range(self.board_size):
                col = []
                for j in range(self.board_size):
                    col.append(' ')

                self.board.append(col)

    # initialize actual board
    def put_pieces(self):
        # initialize black pieces
        self.board[0][0] = Rook('♜', 'black', 0, 0)
        self.board[0][1] = Knight('♞', 'black', 0, 1)
        self.board[0][2] = Bishop('♝', 'black', 0, 2)
        self.board[0][3] = Queen('♛', 'black', 0, 3)
        self.board[0][4] = King('♚', 'black', 0, 4)
        self.board[0][5] = Bishop('♝', 'black', 0, 5)
        self.board[0][6] = Knight('♞', 'black', 0, 6)
        self.board[0][7] = Rook('♜', 'black', 0, 7)

        for i in range(self.board_size):
            p = Pawn('♟', 'black', 1, i)
            self.board[1][i] = deepcopy(p)

        # initialize white pieces
        self.board[self.board_size - 1][0] = Rook('♖', 'white', self.board_size - 1, 0)
        self.board[self.board_size - 1][1] = Knight('♘', 'white', self.board_size - 1, 1)
        self.board[self.board_size - 1][2] = Bishop('♗', 'white', self.board_size - 1, 2)
        self.board[self.board_size - 1][3] = Queen('♕', 'white', self.board_size - 1, 3)
        self.board[self.board_size - 1][4] = King('♔', 'white', self.board_size - 1, 4)
        self.board[self.board_size - 1][5] = Bishop('♗', 'white', self.board_size - 1, 5)
        self.board[self.board_size - 1][6] = Knight('♘', 'white', self.board_size - 1, 6)
        self.board[self.board_size - 1][7] = Rook('♖', 'white', self.board_size - 1, 7)

        for i in range(self.board_size):
            p = Pawn('♙', 'white', self.board_size - 2, i)
            self.board[self.board_size - 2][i] = deepcopy(p)

    # calc points of a piece depending on its team
    def calc_points(self):
        for row in self.board:
            for _piece in row:
                if _piece != ' ':
                    _piece.pts = -1 * _piece.pts if _piece.team == 'black' else _piece.pts

    # take a move
    def take_moves(self):
        for row in self.board:
            for _piece in row:
                if _piece != ' ':
                    for move in _piece.delta:
                        for i in range(len(move)):
                            if _piece.team == 'black':
                                move[i] = 0 - move[i]

    # duplicate board
    def duplicate(self):
        b = []

        for i in range(self.board_size):
            col = []
            for j in range(self.board_size):
                col.append(' ')

            b.append(col)

        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    b[row][col] = deepcopy(self.board[row][col].duplicate())

        return deepcopy(b)

    # show an entire board with pieces
    def show_board(self):
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        rows = ['1', '2', '3', '4', '5', '6', '7', '8']

        print()

        print(' ', end=' ')

        for letter in cols:
            print('', letter, sep=' ', end=' ')
        print()

        for i in range(self.board_size):
            print(rows[i], end=' ')

            for j in range(self.board_size):
                team = -1
                if self.board[i][j] == ' ':
                    p = '■'
                else:
                    p = self.board[i][j].symbol
                    if p in self.black_pieces:
                        team = 'black'
                    else:
                        team = 'white'

                if team == -1:
                    print('', p, sep=' ', end=' ')
                elif team == 'black':
                    print('', colored(p, 'red'), sep=' ', end=' ')
                else:
                    print('', colored(p, 'yellow'), sep=' ', end=' ')

            print(' ' + rows[i])
            
        print(' ', end=' ')

        for letter in cols:
            print('', letter, sep=' ', end=' ')
        print()

        self.write_board_to_file()

    def write_board_to_file(self):
        sys.stdout = open('./result.txt', 'a', encoding='utf-8')
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        rows = ['1', '2', '3', '4', '5', '6', '7', '8']

        print()

        print(' ', end=' ')

        for letter in cols:
            print('', letter, sep=' ', end=' ')
        print()

        for i in range(self.board_size):
            print(rows[i], end=' ')

            for j in range(self.board_size):
                team = -1
                if self.board[i][j] == ' ':
                    p = '■'
                else:
                    p = self.board[i][j].symbol
                    if p in self.black_pieces:
                        team = 'black'
                    else:
                        team = 'white'

                if team == -1:
                    print('', p, sep=' ', end=' ')
                elif team == 'black':
                    print('', p, sep=' ', end=' ')
                else:
                    print('', p, sep=' ', end=' ')

            print(' ' + rows[i])
            
        print(' ', end=' ')

        for letter in cols:
            print('', letter, sep=' ', end=' ')
        print()

        sys.stdout.close()
        sys.stdout = sys.__stdout__

    # check if poistion is valid on the board
    def check_in_range(self, row: int, col: int):
        if 0 <= row < self.board_size and 0 <= col < self.board_size:
            return True
        return False

    # check if a selected cell is empty
    def check_cell_empty(self, row: int, col: int):
        if self.board[row][col] == ' ':
            return True
        return False

    # check if piece at dest is an ally
    def check_ally_at_dest(self, _piece: Piece, row: int, col: int) -> bool:
        if self.check_cell_empty(row, col):
            return False

        if self.get_piece(row, col).team == _piece.team:
            return True

        return False

    # check if piece at dest is an enemy
    def check_enemy_at_dest(self, _piece: Piece, row: int, col: int):
        if self.check_cell_empty(row, col):
            return False

        if self.get_piece(row, col).team != _piece.team:
            return True

        return False

    # get a piece at a cell
    def get_piece(self, row: int, col: int):
        return self.board[row][col]

    # get the team of the piece at specified coordinates
    def get_team(self, row: int, col: int):
        if self.check_cell_empty(row, col):
            return None

        return self.board[row][col].team

    # get the name of a piece at specified string coordinates
    def get_piece_name(self, pos):
        row, col = parse_position(pos)
        return self.board[row][col].name

    # get available moves on the board
    def get_all_moves(self, team: str):
        moves = []
        for row in self.board:
            for _piece in row:
                if _piece != ' ':
                    if _piece.team == team:
                        moves += _piece.get_moves(self)

        return moves

    # get all positions of pieces for a team
    def get_team_positions(self, team: str):
        positions = []

        for row in self.board:
            for _piece in row:
                if _piece != ' ':
                    if _piece.team == team:
                        pos = (_piece.row, _piece.col)
                        positions.append(pos)

        return positions

    # set an empty cell
    def set_empty(self, row: int, col: int):
        self.board[row][col] = ' '

    # set a piece at a given cell
    def set_piece(self, _piece, row: int, col: int):
        self.board[row][col] = _piece

    # perform the castle move
    def castle(self, king):
        # in case of moving to right
        if self.castling_right:
            self.castling_right = False

            rook = self.get_piece(king.row, king.col + 3)

            self.set_empty(king.row, king.col)
            self.set_empty(rook.row, rook.col)

            self.set_piece(king, king.row, king.col + 2)
            self.set_piece(rook, rook.row, rook.col - 2)

            king.col = king.col + 2
            rook.col = rook.col - 2

        # in case of moving to left
        elif self.castling_left:
            self.castling_left = False

            rook = self.get_piece(king.row, king.col - 4)

            self.set_empty(king.row, king.col)
            self.set_empty(rook.row, rook.col)

            self.set_piece(king, king.row, king.col - 2)
            self.set_piece(rook, rook.row, rook.col + 3)

            king.col = king.col - 2
            rook.col = rook.col + 3

    # upgrade a pawn to some other piece
    def upgrade_pawn(self, pawn, is_human):

        upgradable_pieces = ['knight', 'bishop', 'rook', 'queen']
        name = ""

        if is_human:
            print("\nYou can upgrade your pawn!", end=' ')

            while name not in upgradable_pieces:
                name = input("Please choose one of pieces (knight, bishop, rook, queen): ")

        else:
            # AI pawn will be upgraded to a random piece
            idx = random.randint(0, len(upgradable_pieces) - 1)
            name = upgradable_pieces[idx]

        row = pawn.row
        col = pawn.col
        team = pawn.team

        if team == 'white':
            symbol = '♕'
        else:
            symbol = '♛'

        if name == 'knight':
            self.board[row][col] = Knight(symbol, team, row, col)

        elif name == 'bishop':
            self.board[row][col] = Bishop(symbol, team, row, col)

        elif name == 'rook':
            self.board[row][col] = Rook(symbol, team, row, col)

        elif name == 'queen':
            self.board[row][col] = Queen(symbol, team, row, col)

        else:
            pass

    # check if pawn can be upgraded
    def check_upgrade_transform(self, _piece) -> bool:
        if _piece.name == 'pawn':

            if _piece.team == 'white':
                if _piece.row == 0:
                    return True

            elif _piece.team == 'black':
                if _piece.row == self.board_size - 1:
                    return False

    # check if a move is possible for a specified piece
    def check_move_possible(self, _piece: Piece, new_row: int, new_col: int):
        diff_row = new_row - _piece.row
        diff_col = new_col - _piece.col

        if _piece.name == 'pawn':
            # pawn can only move diagonally if there is an enemy there
            if [diff_row, diff_col] in [[-1, 1], [-1, -1], [1, -1], [1, 1]]:
                if not self.check_enemy_at_dest(_piece, new_row, new_col):
                    return False

            # pawn cannot move forward if there is a piece at the destination
            if [diff_row, diff_col] in [[1, 0], [-1, 0], [2, 0], [-2, 0]]:
                if [diff_row, diff_col] in [[2, 0], [-2, 0]] and _piece.has_moved:
                    return False
                if not self.check_cell_empty(new_row, new_col):
                    return False

        if _piece.name == 'king':
            king_row = _piece.row
            king_col = _piece.col

            # king attempting castling
            if [diff_row, diff_col] in [[0, 2], [0, -2]]:

                # castling not possible if king has already moved
                if _piece.has_moved:
                    return False

                # right castle
                if diff_col == 2:
                    # cells between king and rook should be empty
                    if not self.check_cell_empty(king_row, king_col + 1) or not self.check_cell_empty(king_row, king_col + 2):
                        return False

                    # where the rook should be
                    rook_place = self.get_piece(king_row, self.board_size - 1)

                    # no rook at the supposed position
                    if rook_place == ' ' or rook_place.name != 'rook':
                        return False

                    # cannot castle if rook has moved
                    if rook_place.has_moved:
                        return False

                    self.castling_right = True
                    return True

                # left castle
                elif diff_col == -2:
                    # cells between king and rook should be empty
                    if not self.check_cell_empty(king_row, king_col - 1) or not self.check_cell_empty(king_row,
                                                                                                king_col - 2) or not self.check_cell_empty(
                            king_row, king_col - 3):
                        return False

                    # where the rook should be
                    rook_place = self.get_piece(king_row, king_col - 4)

                    # no rook at the supposed position
                    if rook_place == ' ' or rook_place.name != 'rook':
                        return False

                    # cannot castle if rook has moved
                    if rook_place.has_moved:
                        return False

                    self.castling_left = True
                    return True

        if [diff_row, diff_col] in _piece.delta:
            return True
        else:
            return False

    # check if there is a piece on path
    def check_piece_in_path(self, _piece: Piece, new_row: int, new_col: int):

        # knight can jump over any pieces in path
        if _piece.name == 'knight':
            return False

        diff_row = new_row - _piece.row
        diff_col = new_col - _piece.col

        # getting the ratio
        row_step = diff_row / abs(diff_row) if diff_row != 0 else 0
        row_step = int(row_step)
        col_step = diff_col / abs(diff_col) if diff_col != 0 else 0
        col_step = int(col_step)

        curr_row = deepcopy(_piece.row)
        curr_col = deepcopy(_piece.col)

        curr_row += row_step
        curr_col += col_step

        # if destination is at immediate next step and there is a piece there of the same team
        if curr_row == new_row and curr_col == new_col:
            if _piece.team == self.get_team(curr_row, curr_col):
                return True

        # incrementing so we can go through the whole path to destination, step by step
        while curr_row != new_row or curr_col != new_col:

            if not self.check_cell_empty(curr_row, curr_col):
                return True

            curr_row += row_step
            curr_col += col_step

        return False

    # move a piece from one cell to another
    def take_move(self, move: str, team: str, is_human: bool):
        row, col, new_row, new_col = get_int_pos(move)

        # creating a temporary board
        temp = self.duplicate()
        new_board = Board(True)
        new_board.board = deepcopy(temp)

        _piece = new_board.board[row][col]

        if (row, col) in self.get_team_positions(get_another_team(team)):
            if is_human:
                print("\nCannot move a piece of the opposite team.")
            return False, None

        if row is None or col is None or new_row is None or new_col is None:
            if is_human:
                print("\nError parsing input.")
            return False, None

        if not self.check_in_range(new_row, new_col):
            if is_human:
                print("\nDestination out of range.")
            return False, None

        if self.check_cell_empty(row, col):
            if is_human:
                print("\nThere is no piece to move at the selected cell.")
            return False, None

        if not self.check_move_possible(_piece, new_row, new_col):
            if is_human:
                print("\nPiece at selected cell cannot move to the specified location.")
            return False, None

        if self.check_ally_at_dest(_piece, new_row, new_col):
            if is_human:
                print("\nIllegal move. There is a friendly piece at the destination.")
            return False, None

        if self.check_piece_in_path(_piece, new_row, new_col):
            if is_human:
                print("\nIllegal Move. There is a friendly piece in the path.")
            return False, None

        # trying left castling on temp board
        if self.castling_left:
            new_board.castling_left = True
            new_board.castle(_piece)

        # trying right castling on temp board
        if self.castling_right:
            new_board.castling_right = True
            new_board.castle(_piece)

        # trying any other move on temp board
        else:
            new_board.set_empty(row, col)
            new_board.set_piece(_piece, new_row, new_col)
            new_board.board[new_row][new_col].set_pos(new_row, new_col)

        # if the movement leads to check
        if in_check(new_board, team):
            # if this player was already in check
            if in_check(self, team):
                if is_human:
                    print("\nYou cannot make a move that keeps your King in check.")
            else:
                if is_human:
                    print("\nYou cannot make a move that puts your King into check.")
            return False, None

        # mark piece as moves
        if not _piece.has_moved:
            _piece.has_moved = True

            # once pawn has moved, it should no longer be allowed to do two step move
            if _piece.name == 'pawn':
                _piece.remove_two_step_move()

        # update actual board
        _piece = self.board[row][col]

        # castle left
        if self.castling_left:
            self.castle(_piece)

        # castle right
        elif self.castling_right:
            self.castle(_piece)

        # perform any other move
        else:
            self.set_empty(row, col)
            self.set_piece(_piece, new_row, new_col)

            # update the piece attributes
            _piece.set_pos(new_row, new_col)
            _piece.has_moved = True

        # check if pawn should be transformed to another piece (if it reaches end of board)
        if self.check_upgrade_transform(_piece):
            self.upgrade_pawn(_piece, is_human)

        return True, _piece.name
