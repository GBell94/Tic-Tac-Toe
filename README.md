#**Tic Tac Toe**

Tic Tac Toe is a Python terminal game which runs in the Code Institue mock terminal on Heroku.

It's based on the pencil-and-paper game with two players. On paper, the board is drawn as two horizontal and two vertical lines which create nine spaces: one at the centre of the grid, four corners and four sides. One player chooses 'X' and the other is 'O'. Th players take turns to write their chosen letter in one of the empty spaces, with the aim of getting three identical letters in a row, column or diagonal. The game tactics involve not only looking for a win but trying to block the opposing player from making a potentially winning move.

## How to play

This version allows a user to play against the computer. The user is allocated 'X' and the computer 'O', and the user is allowed to take the first turn. The user selects the number of their chosen board position and the computer then makes it's choice. The user and computer continue taking turns until there is a winner (the user or the computer get three letters in a row) or there are no more moves and the game is a tie.

## Features

- User receives a welcome to the game, a brief summary of the rules and how to play.
- The game board is printed with the position numbers for reference.
- Play is against the computer.
- User input is required: users must enter the number corresponding to their move.
- User input is validated: 
    - Users must enter a number between 1 and 9
    - Users cannot choose the same move twice
    - Users cannot enter a string
- Users are given feedback regarding a win or tie.
- There is an opportunity for the user to play again or to quit.

## Future Features

- Allow user to choose 'X' or 'O'.
- Allow a random choice of who takes the first turn.
- To develop the computer's game strategy. The computer's preferred moves change slightly depending on whether it takes the first turn or goes second. 
- To investigate using itertools to check combinations of winning moves for the computer and also the minimax algorithm. However, the use of minimax allows the computer to win each time, which may be frustrating for a human user!
- An object oriented approach to the game.

## Testing

The project has been manually tested as follows:

- The code has been passed through a PEP8 linter and this confirmed that there were no problems.
- Invalid input has been provided at the prompt for a move, including a number outside the range 1 to 9, repeating a move already played and entering a string. 
- The game has been run in a local Gitpod terminal and in the Heroku terminal.

## Bugs




## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

Connect your GitHub repository and deploy as normal.

