from random import randint

from beautifultable import BeautifulTable
"""
https://beautifultable.readthedocs.io/en/v0.7.0/
"""


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
        self.columns_header = []
        self.rows_header = []
        self.grid = BeautifulTable()


def game_setup():
    """
    Player enters name, sets board size. Ship number based on board size.
    """
    player_name = input("Enter your name:\n")

    while True:
        board_size = input("Enter board size (4-6)\n") 

        if validate_size(board_size):
            print(f"\nBoard size: {board_size}x{board_size}")
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
    grid = board.grid

    for squares in range(int(board.board_size)):
        board.rows_header.append(chr(squares + 65))
        board.columns_header.append(str(squares + 1))

    grid.columns.header = board.columns_header
    grid.rows.header = board.rows_header

    if board.type == "human":
        ships = len(board.ship_positions)
        for i in range(ships):
            position = board.ship_positions[i]
            row = position[0]
            column = position[1]
            grid.rows[row][column] = "\u0394"

    print(f"\n{board.player_name}'s Board:")
    print(grid)


def game_loop(player_board, computer_board):
    """
    Loops through player and computer guesses until all ships destroyed on either board.
    """
    print(f"\nYou have {player_board.ship_number} ships left")
    print(f"Computer has {computer_board.ship_number} ships left")

    while player_board.ship_number != 0 and computer_board.ship_number != 0:
        player_guess(computer_board)
        computer_guess(player_board)

        update_board(player_board)
        update_board(computer_board)

    # print("game over")


def player_guess(board):
    """
    Receives a target from player and returns a hit or miss on computer board.
    """
    print(board.ship_positions)

    while True:
        target = input("\nChoose a target. eg. 'A1'\n")
        target = list(target)
        target[0] = target[0].upper()

        if validate_target(board, target):
            # https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python
            target[0] = ord(target[0]) - 65
            target[1] = int(target[1]) - 1

            if target in board.guesses:
                print("Coordinate has already been selected. Please try again")
            else:
                board.guesses.append(target)
                break

    if target in board.ship_positions:
        board.ship_number -= 1
        print(f"Hit! Computer ships remaining: {board.ship_number}")
    else:
        print(f"Miss! Computer ships remaining: {board.ship_number}")


def validate_target(board, value):
    """
    Validates player's input coordinates to target computer board.
    """
    try:
        if len(value) == 2 and value[0] in board.rows_header and value[1] in board.columns_header:
            return True
        else:
            print("Please enter a valid coordinate")
            return False
    except ValueError:
        print("Please enter a valid coordinate")


def computer_guess(board):
    """
    Generates a target from computer and returns a hit or miss on player board.
    """
    while True:
        row = randint(0, int(board.board_size)-1)
        column = randint(0, int(board.board_size)-1)
        target = [row, column]
        coordinates = str(chr(target[0] + 65) + str(target[1] + 1))

        # print(target)

        if target not in board.guesses:
            board.guesses.append(target)
            break
        else:
            continue

    # print(board.guesses)

    print(f"Computer chose {coordinates}")
    if target in board.ship_positions:
        board.ship_number -= 1
        print(f"Computer scores a hit! Player ships remaining: {board.ship_number}")
    else:
        print(f"Computer misses. Player ships remaining: {board.ship_number}")


def update_board(board):
    """
    Updates player and computer boards between rounds by adding hits and misses.
    """
    grid = board.grid
    guesses = len(board.guesses)
    for i in range(guesses):
        position = board.guesses[i]
        row = position[0]
        column = position[1]

        if position in board.ship_positions:
            grid.rows[row][column] = "X"
        else:
            grid.rows[row][column] = "O"

    print(f"\n{board.player_name}'s Board:")
    print(grid)


def end_game(player_board, computer_board):
    """
    Finishes game and declares winner.
    """
    if player_board.ship_number == 0 and computer_board.ship_number == 0:
        print(f"{player_board.player_name} has no ships left")
        print("Computer has no ships left")
        print("Game drawn")
    elif player_board.ship_number == 1 and computer_board.ship_number == 0:
        print(f"{player_board.player_name} has 1 ship left")
        print("Computer has no ships left")
        print(f"{player_board.player_name} wins the game")
    elif player_board.ship_number > 1 and computer_board.ship_number == 0:
        print(f"{player_board.player_name} has {player_board.ship_number} ships left")
        print("Computer has no ships left")
        print(f"{player_board.player_name} wins the game")
    elif player_board.ship_number == 0 and computer_board.ship_number == 1:
        print(f"{player_board.player_name} has no ships left")
        print("Computer has 1 ship left")
        print()
    elif player_board.ship_number == 0 and computer_board.ship_number > 1:
        print(f"{player_board.player_name} has no ships left")
        print(f"Computer has {computer_board.ship_number} ships left")
        print("Computer wins the game")

    input("Press Enter to continue...")
    play_game()


def play_game():
    """
    Starts a new game. Resets scores, runs game setup, initialises
    player and computer boards and runs game to completion.
    """
    print("\nWelcome to Battleships!\n")

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

    game_loop(player_board, computer_board)

    end_game(player_board, computer_board)


play_game()
