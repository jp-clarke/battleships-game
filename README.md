# Battleships

Battleships is a Python based variation of the classic pencil and paper game (and later board game). This particular version runs in Code Institute's mock terminal on Heroku. Users will play against a computer opponent and try to guess the position of the computer's ships before their own ships are destroyed.

Link to the live version is as follows:

https://battleships-jclarke.herokuapp.com/

## How to Play

In this version of the game, rather than turns being alternate, both player and computer turns occur in a single round, thereby eliminating first turn advantage.

To begin, the player is asked to enter their name.

The player is then asked to set the size of the board, from a minimum of 3x3 up to a 6x6 grid. The number of ships per board depends on this selection.

Both player's and computer's boards are then displayed in the terminal. The player's ships are displayed on the board as a delta sign ( &#916; ). The computer's ships remain invisible.

The player is asked to choose a target on the board, after which the computer will choose a target on the player's board. Hits are marked with an "X", whereas misses are marked with a "O".

After each round, the number of ships remaining for both player and computer is updated.

The winner is the first to sink all of the opponent's ships. If both players lose their final ships in a single round, the game will be declared a draw.

## Design



## Features



## Data Model



## Testing



### Bugs



## Deployment



## Credits