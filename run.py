# Generate random numbers for placing ships and generating targets on board.
from random import randint

# Creates time delay between functions to improve user experience.
# https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/
from time import sleep

# Prints visually appealing game board to terminal
# https://beautifultable.readthedocs.io/en/v0.7.0/
from beautifultable import BeautifulTable


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
    while True:
        player_name = input("Enter your name:\n")

        if validate_name(player_name):
            break

    while True:
        board_size = input("Enter board size (3-6)\n")

        if validate_size(board_size):
            print(f"\nBoard size: {board_size}x{board_size}")
            break

    ship_number = round(1.3*int(board_size))
    print(f"You have {ship_number} ships.\n")
    sleep(1)
    print(f"\u0394 - {player_name}'s ships")
    print("X - Hit")
    print("O - Miss")

    return player_name, board_size, ship_number


def validate_name(value):
    """
    Validates player name input.
    """
    try:
        if 0 < len(value) <= 50:
            return True
        print("Name must be from 1 to 50 characters")
        return False
    except TypeError:
        print("Name must be from 1 to 50 characters")
        return False


def validate_size(value):
    """
    Validates player input for board size.
    """
    try:
        if 2 < int(value) < 7:
            return True
        print("Please enter a number between 3 and 6")
        return False
    except ValueError:
        print("Please enter a number between 3 and 6")
        return False


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
    Loops through player and computer guesses until all ships
    have been destroyed on either board.
    """
    sleep(1)
    print(f"\nYou have {player_board.ship_number} ships left")
    print(f"Computer has {computer_board.ship_number} ships left")

    while player_board.ship_number != 0 and computer_board.ship_number != 0:
        player_guess(computer_board)
        sleep(1.5)
        computer_guess(player_board)

        sleep(1.5)
        update_board(player_board)
        sleep(1.5)
        update_board(computer_board)


def player_guess(board):
    """
    Receives a target from player and returns a hit or miss on computer board.
    """
    # print(board.ship_positions)

    while True:
        target = input("\nChoose a target. eg. 'A1'\n")
        target = list(target)

        if validate_target(board, target):
            target[0] = target[0].upper()
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
        if len(value) == 0:
            print("Please enter a valid coordinate")
            return False

        value[0] = value[0].upper()
        if (len(value) == 2 and
            value[0] in board.rows_header and
                value[1] in board.columns_header):
            return True
        else:
            print("Please enter a valid coordinate")
            return False
    except ValueError:
        print("Please enter a valid coordinate")
        return False


def computer_guess(board):
    """
    Generates a target from computer and returns a hit or miss on player board.
    """
    while True:
        row = randint(0, int(board.board_size)-1)
        column = randint(0, int(board.board_size)-1)
        target = [row, column]
        coordinates = str(chr(target[0] + 65) + str(target[1] + 1))

        if target not in board.guesses:
            board.guesses.append(target)
            break

    print(f"Computer chose {coordinates}")
    if target in board.ship_positions:
        board.ship_number -= 1
        print(
            f"Computer scores a hit! "
            f"Player ships remaining: {board.ship_number}"
        )
    else:
        print(f"Computer misses. Player ships remaining: {board.ship_number}")


def update_board(board):
    """
    Updates player and computer boards between
    rounds by adding hits and misses.
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
    sleep(1)
    if player_board.ship_number == 0 and computer_board.ship_number == 0:
        print(f"\n{player_board.player_name} has no ships left")
        sleep(1)
        print("Computer has no ships left\n")
        sleep(1)
        print("Game drawn")
    elif player_board.ship_number == 1 and computer_board.ship_number == 0:
        print(f"\n{player_board.player_name} has 1 ship left")
        sleep(1)
        print("Computer has no ships left\n")
        sleep(1)
        print(f"{player_board.player_name} wins the game!")
    elif player_board.ship_number > 1 and computer_board.ship_number == 0:
        print(
            f"\n{player_board.player_name} has "
            f"{player_board.ship_number} ships left"
        )
        sleep(1)
        print("Computer has no ships left\n")
        sleep(1)
        print(f"{player_board.player_name} wins the game!")
    elif player_board.ship_number == 0 and computer_board.ship_number == 1:
        print(f"{player_board.player_name} has no ships left")
        sleep(1)
        print("Computer has 1 ship left\n")
        sleep(1)
        print("Computer wins the game!")
    elif player_board.ship_number == 0 and computer_board.ship_number > 1:
        print(f"\n{player_board.player_name} has no ships left")
        sleep(1)
        print(f"Computer has {computer_board.ship_number} ships left")
        sleep(1)
        print("\nComputer wins the game!")

    sleep(1)
    input("\nPress Enter to continue...\n")
    play_game()


def play_game():
    """
    Starts a new game. Resets scores, runs game setup, initialises
    player and computer boards and runs game to completion.
    """
    print("\nWelcome to Battleships!\n")

    sleep(1)
    setup_data = game_setup()
    player_name = setup_data[0]
    board_size = setup_data[1]
    ship_number = setup_data[2]

    player_board = Board(board_size, ship_number, player_name, "human")
    computer_board = Board(board_size, ship_number, "Computer", "computer")

    populate_board(player_board)
    populate_board(computer_board)

    sleep(1)
    game_board(player_board)
    sleep(1)
    game_board(computer_board)

    game_loop(player_board, computer_board)

    end_game(player_board, computer_board)


play_game()
