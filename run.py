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

        if validate_size(board_size): #function to be added
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




def play_game():
    """
    Starts a new game. Resets scores, runs game setup, initialises
    player and computer boards and runs game to completion.
    """
    score["player"] = 0
    score["computer"] = 0
    game_setup()


print("Welcome to Battleships!")
play_game()