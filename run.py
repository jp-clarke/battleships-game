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



def play_game():
    """
    Starts a new game. Resets scores, runs game setup, initialises
    player and computer boards and runs game to completion.
    """
    score["player"] = 0
    score["computer"] = 0

print("Welcome to Battleships!")
play_game()