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

The class Board was used as the data model. Instances of the Board class are created for both the player's and the computer's data. The data stored includes the following:
- board size
- number of ships remaining on the board
- player name
- type (human or computer)
- opponent's guesses on the board
- ship positions on the board
- table data
    - row and column headers
    - BeautifulTable()

## Testing




### Bugs



## Deployment


- Ensure that \n is added to end of all input strings
- Update requirements.txt to ensure Heroku installs beautiful table  (pip3 freeze > requirements.txt)
- Save and push changes to github
- Login to Heroku
- Create new app
- Name app (must be unique)
- Choose region (Europe)
- Create app
- Go to Settings tab
- Config Vars
    - The key is PORT and the value is 8000
- Add Buildpacks (ensure correct order)
    - python
    - nodejs
- Go to Deploy tab
- Select GitHub and connect
- Search for GitHub repository, select and connect
- Deploy branch

##  Credits