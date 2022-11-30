from copy import deepcopy

piece_weights = {
    "king": [
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
        [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
        [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
        [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]
    ],

    "queen": [
        [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
        [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
        [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
        [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
        [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
        [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
        [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
        [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
    ],

    "rook": [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
        [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
        [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
        [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
        [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
        [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
        [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
    ],

    "bishop": [
        [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
        [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
        [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
        [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
        [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
        [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
        [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
        [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
    ],

    "knight": [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
        [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
        [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
        [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
        [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
        [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ],

    "pawn": [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
        [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
        [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
        [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
        [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
        [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ],

}

# get an another team
def get_another_team(team):
    return 'black' if team == 'white' else 'white'

# returns a (curpos,newpos)
def get_move_pos(cur_row: int, cur_col: int, new_row: int, new_col: int):
    cur_pos = str(cur_row + 1) + chr(cur_col + ord('a'))
    new_pos = str(new_row + 1) + chr(new_col + ord('a'))

    return cur_pos + new_pos

# return a position(int, int)
def parse_position(pos: str) -> (int, int):
    row = int(pos[0]) - 1
    col = ord(pos[1]) - ord('a')

    return row, col

# return a table for another player
def get_another_table(tb):
    tb = deepcopy(tb)
    tb.reverse()

    for i in range(len(tb)):
        for j in range(len(tb[i])):
            tb[i][j] = 0 - tb[i][j]

    return tb


# get the value of a piece
def get_piece_val(_piece):
    if _piece == ' ':
        return 0

    return _piece.pts


def in_check(_board, team: str) -> bool:
    # getting the moves of the other team
    moves = _board.get_all_moves(get_another_team(team))

    # getting the king of own team
    team_king = None

    for row in _board.board:
        for _piece in row:
            if _piece != ' ':
                if _piece.name == 'king' and _piece.team == team:
                    team_king = _piece

    if team_king is None:
        for row in _board.board:
            print(row)

        raise Exception("King was None while attempting to check if team " + team + " is in check.")

    # iterating through all moves of the opposite team
    for move in moves:
        _, __, new_row, new_col = get_int_pos(move)

        # if destination of any move matches king's coordinates
        if new_row == team_king.row and new_col == team_king.col:
            return True

    return False

# get the evaluations for a piece at a position according to our piece square tables
def get_piece_wei(_piece):
    if _piece == ' ':
        return 0

    row = _piece.row
    col = _piece.col

    piece_table = piece_weights[_piece.name]

    if _piece.team == 'white':
        return piece_table[row][col]

    # for black, the evaluations have to be reversed (board reversed)
    else:
        piece_table = get_another_table(piece_table)
        return piece_table[row][col]


# get the total value of a board
def get_board_wei(_board):
    val = 0

    for row in _board.board:
        for _piece in row:
            val += get_piece_val(_piece) + get_piece_wei(_piece)

    return val


# analyze a string and return a position(int,int,int,int)
def get_int_pos(move: str) -> (int, int, int, int):
    if len(move) != 4:
        return None, None, None, None

    cur_pos = move[0] + move[1]
    move_pos = move[2] + move[3]

    cur_row = int(cur_pos[0]) - 1
    cur_col = ord(cur_pos[1]) - ord('a')

    new_row = int(move_pos[0]) - 1
    new_col = ord(move_pos[1]) - ord('a')

    return cur_row, cur_col, new_row, new_col

def checkmate_board(_board, team: str):
    # cannot be in checkmate if not in check :)
    if not in_check(_board, team):
        return False

    # obtaining all moves of team
    moves = _board.get_all_moves(team)

    # for every move that a piece in the team can make
    for move in moves:
        temp = deepcopy(_board.board)
        temp_board = deepcopy(_board)
        temp_board.board = deepcopy(temp)

        # temporarily making that move
        res, _ = temp_board.take_move(move, team, False)

        if res:
            # if move does not lead to check, it means checkmate is not possible as there is at least one way out
            if not in_check(temp_board, team):
                return False

    return True


def checkstalemate_board(_board, team: str):
    # cannot be in checkmate for a stalemate to occur
    if checkmate_board(_board, team):
        return False

    moves = _board.get_all_moves(team)

    for move in moves:
        temp = deepcopy(_board.board)
        temp_board = deepcopy(_board)
        temp_board.board = deepcopy(temp)

        # temporarily making that move
        temp_board.take_move(move, team, False)

        # if there is such a move that leads out of check
        if not in_check(temp_board, team):
            return False

    return True