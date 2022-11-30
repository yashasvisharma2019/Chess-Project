from Engine.Board import *

# represent a chess class that implements a main game loop
class ChessForPlayers:
    def __init__(self):
        # set default white to user team
        self.my_team = 'white'

        # init board
        self.init_board()

        # start processing game
        self.game_loop()

    def init_board(self):
        # create an initial board and put pieces
        self.board = Board(False)
        self.board.put_pieces()
        self.board.calc_points()
        self.board.take_moves()
        self.board.show_board()

    def game_loop(self):
        cur_team = self.my_team
        ano_team = 'black' if cur_team == 'white' else 'white'

        while True:
            # take user input
            cur_index = 1 if cur_team == 'white' else 2
            cur_piece = input("Player {}\nPlease enter the position of piece to move (ex: 1a, 7b, ...):  ".format(cur_index))
            target = input("Please enter the target position of current piece (ex: 3b, 7c, ...): ")

            result, name = self.board.take_move(cur_piece + target, cur_team, True)

            if not result:
                print("\nFailed to move a current piece. Please try again")

            else:
                print("Player {}: {}({}) moved to {}".format(cur_index, name, cur_piece, target))
                self.board.show_board()

                # check if a user wins
                if checkmate_board(self.board, ano_team):
                    print("\nCheckmate! Player {} win!!!!!\n".format(cur_index))
                    break
                
                # check if a game is in draw
                if checkstalemate_board(self.board, ano_team):
                    print("Stalemate. Draw !!!")
                    break

            cur_team, ano_team = ano_team, cur_team
