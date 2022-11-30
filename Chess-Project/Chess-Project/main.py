from termcolor import colored
from Engine.ChessForAI import ChessForAI
from Engine.ChessForPlayers import ChessForPlayers

def start_game():
    print(colored('Welcome to My Chess AI Game', 'cyan'))

    # initialize a result file
    open('./result.txt', 'w')

    while True:
        mode = input(colored('Please select mode(1. Player vs Player, 2. Player vs AI): ', 'magenta'))
        if mode in ['1', '2']:
            break
        
    # in case of Player vs AI
    if mode == '2':
        while True:
            # input a depth of search
            depth_of_search = input(colored('Please input depth of search: ', 'magenta'))

            if depth_of_search.isdigit():
                break

        ChessForAI(int(depth_of_search))
    elif mode == '1':
        ChessForPlayers()

# start a chess game
start_game()