from random import randint

from beautifultable import BeautifulTable
"""
https://beautifultable.readthedocs.io/en/v0.7.0/
"""

score = {"player": 0, "computer": 0}

columns_header = []
rows_header = []

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
            print(f"\nBoard size: {board_size}x{board_size}\n")
            break

    ship_number = round(1.3*int(board_size))
    print(f"You have {ship_number} ships.\n")

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
        row = randint(0, int(board.board_size)-1)
        column = randint(0, int(board.board_size)-1)

        if [row, column] not in board.ship_positions:
            board.ship_positions.append([row, column])
            i += 1


def game_board(board):
    """
    Displays game board to player.
    https://stackoverflow.com/questions/18544419/how-to-convert-numbers-to-alphabet
    """

    grid = BeautifulTable()
    
    # Reset row and column header lists
    global columns_header
    columns_header = []
    global rows_header
    rows_header = []

    for squares in range(int(board.board_size)):
        rows_header.append(chr(squares + 65))
        columns_header.append(str(squares + 1))    

    grid.columns.header = columns_header
    grid.rows.header = rows_header

    if board.type == "human":
        ships = len(board.ship_positions)
        for i in range(ships):
            position = board.ship_positions[i]
            row = position[0]
            column = position[1]
            grid.rows[row][column] = "\u0394"

        print(f"{board.player_name}'s Board:")
        print(grid)

    if board.type == "computer":
        print(f"\n{board.player_name}'s Board:")
        print(grid)


def player_guess(player_board, computer_board):
    """
    Receives a target from player and returns a hit or miss on computer board.
    """
    print(f"\nYou have {player_board.ship_number} ships left")
    print(f"Computer has {computer_board.ship_number} ships left\n")

    while True:
        target = input("Choose a target. eg. 'A1'\n")
        target = list(target)
        target[0] = target[0].upper()
        validate_target(target)

        # https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python
        target[0] = ord(target[0]) - 65
        target[1] = int(target[1]) - 1

        if target not in computer_board.guesses:
            break
        else:
            return True
    
    computer_board.guesses.append(target)
    print(computer_board.guesses)
    print(player_board.ship_positions)
    print(computer_board.ship_positions)
    # if target in computer_board.ship_positions:


def validate_target(value):
    """
    Validates player's input coordinates to target computer board.
    """
    



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

    game_board(player_board)
    game_board(computer_board)

    player_guess(player_board, computer_board)


print("\nWelcome to Battleships!\n")
play_game()