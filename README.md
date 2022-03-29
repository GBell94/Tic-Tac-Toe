# Tic Tac Toe

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

Welcome to the game:

![welcome screenshot](/images/Game-welcome-screenshot.png)

User validation:

![user validation screenshot](/images/user-input-validation-screenshot.png)

End of game:

![exit screenshot](/images/exit-user-input-screenshot.png)

## Future Features

- Allow user to choose 'X' or 'O'.
- Allow a random choice of who takes the first turn.
- To develop the computer's game strategy. The computer's preferred moves change slightly depending on whether it takes the first turn or goes second. 
- To investigate the minimax algorithm to decide the computer's move. However, the use of minimax allows the computer to win each time, which may be frustrating for a human user!
- An object oriented approach to the game.

## Testing

The project has been manually tested as follows:

- The code has been passed through a PEP8 linter and this confirmed that there were no problems.
- Invalid input has been provided at the prompt for a move, including a number outside the range 1 to 9, repeating a move already played and entering a string. 
- The game has been run in a local Gitpod terminal and in the Heroku terminal.

## Validator Testing

- PEP8
    No errors were returned from the PEP8 linter [PEP8online.com](http://pep8online.com/)

![PEP8 screenshot](/images/PEP8-screenshot.png)

## Bugs

### Solved Bugs

- The check_row, check_column and check_diagonal functions did not work correctly initially and were rewritten to return the winner.
- The play_again function printed out the request for user information but did not restart or exit in response. This was due to attempting to change a global variable within the function. This was rewritten to return True/False and the global variable changed outside the play_again function.

### Remaining Bugs

No known bugs remain.

## Deployment

This project was deployed using the Code Institute mock terminal for Heroku. After creating an Heroku account:
- Create a new Heroku app.
- Go to Settings tab and select Config Vars.
- Create a _Config Var_ using the provided key and value.
- Again in Settings tab, select Buildpacks.
- Add Python and save, then add node.js and save. Ensure the order is Python first, node.js second.
- Go to the Deployment tab.
- In Deployment Method, select GitHub, then 'Connect to GitHub'. Add the project name and click 'search'. Once the project is found, click 'Connect'. 
- CLick on Automatic Deploy.

## Credits

- Code Institute for the deployment terminal
- The function to print the game board was taken from a suggestion on StackOverflow
- The structure of the function to capture user input was adapted from a 'Tech with Tim' tutorial on YouTube
- The structure of the function to create the computer's move was adapted from Al Sweigart's 'Invent with Python'

### Note

The game code has been copied from my own repository at GBell94/tic-tac-toe-2. Where the code has been taken or adapted from other sources, this is included in the credits section above.