
Final Chess project:
Implementing a Chess program, with a game tree-based AI

===============================================================================================================================================================
Project Structure
main.py -- entry of this project result.txt -- result of output Engine\AIEngine -- a class that implements minimax algorithm using alpha-beta pruning
Engine\Board -- a class that implements all available moves on the board
Engine\ChessForAI -- a class that simulate a game between a player and AI Engine\ChessForPlayers -- a class that simulate a game between two players
Engine\Helpers -- group of functions and variables containing information about chess game and piece weight
Engine\Pieces\Piece -- base class of piece containing available all basic information about a piece
Engine\Pieces\King
Engine\Pieces\Queen Engine\Pieces\Rook Engine\Pieces\Bishop -- containing available positions and weight about each piece Engine\Pieces\Knight Engine\Pieces\Pawn

===================================================================================================================================================================
Each piece has a weight for its importance
Please refer: https://www.chessprogramming.org/Point_Value

King => Infinity (1000000 in this problem) Queen => 1000 Rook => 550 Bishop => 350 Knight => 300 Pawn => 100 (Max Euwe and Hans Kramer's basic values)

=====================================================================================================================================================================
Play Mode:
Player vs Player
Player vs AI

======================================================================================================================================================================
Implemented Methods

The main file is Main.py and we used termcolor for the color formating in terminal.
Code is written in python
Made by : Yashasvi Sharma and Rishabh Rai
