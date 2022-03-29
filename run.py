import random

"""
Set up game board and set current player to 'X', which will be the user
User will have first turn
"""
board = ['-' for x in range(9)]

current_player = 'X'

game_running = True


def print_board(board):
    """
    Take board list and display in a 2D row-column format
    """
    print("""
    {0} | {1} | {2}
    ---------
    {3} | {4} | {5}
    ---------
    {6} | {7} | {8}""".format(board[0], board[1], board[2], board[3], board[4],
                              board[5], board[6], board[7], board[8]))
    print()


def welcome():
    """
    Print out an example board in the welcome message with the spaces numbered
    for reference
    """
    board = [x for x in range(1, 10)]
    print("""
    {0} | {1} | {2}
    ---------
    {3} | {4} | {5}
    ---------
    {6} | {7} | {8}""".format(board[0], board[1], board[2], board[3], board[4],
                              board[5], board[6], board[7], board[8]))
    print()


def player_input(board):
    """
    Get input from the player who enters their move. Validate the input -
    needs to be a number between 1 and 9 and not already chosen. Loop continues
    until input is valid.
    """
    run = True
    while run:
        response = input('Please choose your move (1 - 9): ')
        try:
            move = int(response) - 1
            if move >= 0 and move <= 9:
                if board[move] == '-':
                    run = False
                    board[move] = current_player
                else:
                    print('This space has already been used. Please choose '
                          'again.')
            else:
                print('Your move should be in the range 1 to 9')
        except:
            print('Your move needs to be a number, please try again.')


def check_row(board):
    """
    Check if any row contains three identical letters and return the letter
    if there is a win
    """
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return winner
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return winner
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return winner
    else:
        return False


def check_column(board):
    """
    Check if any column contains three identical letters and return the letter
    if there is a win
    """
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return winner
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return winner
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return winner
    else:
        return False


def check_diagonal(board):
    """
    Check if either diagonal contains three identical letters and return the
    letter if there is a win
    """
    if board[0] == board[4] == board[6] and board[0] != '-':
        winner = board[0]
        return winner
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return winner
    else:
        return False


def check_win(board):
    """
    If there is a winner, let the user know who won
    """
    if ((check_row(board) is not False) or (check_column(board) is not False) or 
       (check_diagonal(board) is not False)):
        print_board(board)
        if ((check_row(board) == 'X') or (check_column(board) == 'X') or 
        (check_diagonal(board) == 'X')):
            print('You win!')
        else:
            print('Computer wins')
        return False


def check_tie(board):
    """
    Check if there are no more moves available and let user know this is a tie
    """
    if '-' not in board:
        print_board(board)
        print("It's a tie")
        return False


def switch_player(current_player):
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def play_again():
    """
    Get input from user to play another game or quit
    """
    exit = input('Do you want to play again? (Y or N) ')
    if exit.lower() == 'y':
        return True
    else:
        print('Thanks for playing!')
        return False


def winner(board, letter):
    """
    Returns if there is a winner - used in working out the computer move
    """
    return ((board[0] == board[1] == board[2] == letter) or
            (board[3] == board[4] == board[5] == letter) or
            (board[6] == board[7] == board[8] == letter) or
            (board[0] == board[3] == board[6] == letter) or
            (board[1] == board[4] == board[7] == letter) or
            (board[2] == board[5] == board[8] == letter) or
            (board[0] == board[4] == board[8] == letter) or
            (board[2] == board[1] == board[6] == letter))


def computer(board):
    """
    Work out the computer move.
    Create a list of possible moves. Create a copy of the current board and
    check if it's possible to make a winning move. If not, try to block a
    player win. Take the centre position as a first preference, the try a
    corner and finally a side position.
    """
    possible_moves = []
    for i in range(0, 9):
        if board[i] == '-':
            possible_moves.append(i)

    move = 0

    for letter in ['X', 'O']:
        for i in possible_moves:
            copy_board = board[:]
            copy_board[i] = letter
            if winner(copy_board, letter):
                return i

    if 4 in possible_moves:
        return 4

    corners = []
    for i in possible_moves:
        if i in [0, 2, 6, 8]:
            corners.append(i)
    if len(corners) > 0:
        return random.choice(corners)

    sides = []
    for i in possible_moves:
        if i in [1, 3, 5, 7]:
            sides.append(i)
    if len(sides) > 0:
        return random.choice(sides)


print('WELCOME to TIC TAC TOE! \n\nYou are X, the computer is O. \nYou go '
      'first - choose your move by selecting your space on the board.\nGet '
      'a straight line of Xs (row, column, diagonal) to win.')
welcome()

while game_running:

    print_board(board)
    player_input(board)
    if (check_win(board) is False) or (check_tie(board) is False):
        game_running = False
    switch_player(current_player)
    computer_move = computer(board)
    if computer_move is not None:
        board[computer_move] = 'O'
    if (check_win(board) is False) or (check_tie(board) is False):
        game_running = False
    switch_player(current_player)
    if game_running is False:
        if play_again() is False:
            game_running = False
        else:
            game_running = True
            board = ['-' for x in range(9)]
