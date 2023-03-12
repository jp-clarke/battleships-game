from beautifultable import BeautifulTable
"""
https://beautifultable.readthedocs.io/en/v0.7.0/
"""

from random import randint

score = {"player": 0, "computer": 0}


class Board:
    """
    Board class. Determines size of board, number of ships, name of player
    and board type.
    """
    def __init__(self, board_size, ship_number, player_name, type):
        self.board_size = board_size
        self.ship_number = ship_number
        self.player_name = player_name
        self.type = type
        self.guesses = []
        self.ship_positions = []


def game_setup():
    """
    Player enters name, sets board size. Ship number based on board size.
    """
    player_name = input("Enter your name:\n")

    while True:        
        board_size = input("Enter board size (4-6)\n") 

        if validate_size(board_size):
            print(f"Board size: {board_size}x{board_size}")
            break

    ship_number = round(1.3*int(board_size))
    print(f"You have {ship_number} ships.")

    return player_name, board_size, ship_number


def validate_size(value):
    """
    Validates player input for board size.
    """
    try:
        if 3 < int(value) < 7:
            return True
        else:
            print("Please enter a number between 4 and 6")
            return False
    except ValueError:
            print("Please enter a number between 4 and 6")


def populate_board(board):
    """
    Positions ships on board for player and computer.
    """

    i = 1
    while i <= board.ship_number:
        x = randint(0, int(board.board_size)-1)
        y = randint(0, int(board.board_size)-1)        
    
        if [x, y] not in board.ship_positions:
            board.ship_positions.append([x, y])
            i += 1


def play_game():
    """
    Starts a new game. Resets scores, runs game setup, initialises
    player and computer boards and runs game to completion.
    """
    score["player"] = 0
    score["computer"] = 0
    
    setup_data = game_setup()
    player_name = setup_data[0]
    board_size = setup_data[1]
    ship_number = setup_data[2]

    player_board = Board(board_size, ship_number, player_name, "human")
    computer_board = Board(board_size, ship_number, "Computer", "computer")

    populate_board(player_board)
    populate_board(computer_board)

    print(player_board.ship_positions)
    print(computer_board.ship_positions)


print("Welcome to Battleships!")
play_game()