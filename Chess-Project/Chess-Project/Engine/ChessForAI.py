from Engine.AIEngine import AIEngine
from Engine.Board import *

# represent a chess class that implements a main game loop
class ChessForAI:
    def __init__(self, depth_of_search):
        # create an AI player
        self.player_ai = AIEngine('black', depth_of_search)

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
        while True:
            # take user input
            cur_piece = input("\nPlease enter the position of piece to move (ex: 1a, 7b, ...):  ")
            target = input("Please enter the target position of current piece (ex: 3b, 7c, ...): ")

            result, name = self.board.take_move(cur_piece + target, self.my_team, True)

            if not result:
                print("\nFailed to move a current piece. Please try again")

            else:
                print("Man: {}({}) moved to {}".format(name, cur_piece, target))
                self.board.show_board()

                # check if a user wins
                if checkmate_board(self.board, self.player_ai.team):
                    print("\nCheckmate! You win!!!!!\n")
                    break
                
                # check if a game is in draw
                if checkstalemate_board(self.board, self.player_ai.team):
                    print("Stalemate. Draw !!!")
                    break

                # move by AI
                self.player_ai.move(self.board)

                self.board.show_board()

                # check if AI wins
                if checkmate_board(self.board, self.my_team):
                    print("Checkmate! AI wins!!!!!\n")
                    break

                if checkstalemate_board(self.board, self.my_team):
                    print("Stalemate. Draw !!!")
                    break
