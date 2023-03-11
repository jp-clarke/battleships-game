from beautifultable import BeautifulTable
"""
https://beautifultable.readthedocs.io/en/v0.7.0/
"""
from random import randint

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


print("Welcome to Battleships!")
