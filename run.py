import random

"""
Set up game board and set current player to 'X', which will be the user
User will have first turn
"""
board = ['-' for x in range(9)]

current_player = 'X'

def print_board(board):
    print("""
    {0} | {1} | {2}
    ---------
    {3} | {4} | {5}
    ---------
    {6} | {7} | {8}""".format(board[0],board[1],board[2],board[3],board[4],board[5],
    board[6],board[7],board[8]))
    print()


def welcome():
    board = [x for x in range(1, 10)]
    print("""
    {0} | {1} | {2}
    ---------
    {3} | {4} | {5}
    ---------
    {6} | {7} | {8}""".format(board[0],board[1],board[2],board[3],board[4],board[5],
    board[6],board[7],board[8]))
    print()


def player_input(board):

    run = True
    while run:
        response = input('Please choose your move (1 - 9): ')
        try:
            move = int(response) - 1
            if move >=0 and move <=9:
                if board[move] == '-':
                    run = False
                    board[move] = current_player  
                else:
                    print('This space has already been used. Please choose again.')  
            else:
                print('Your move should be in the range 1 to 9')
        except:
            print('Your move needs to be a number, please try again.')


def check_row(board):
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
    if board[0] == board[4] == board[6] and board[0] != '-':
        winner = board[0]
        return winner
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return winner
    else:
        return False


def check_win(board):
    if check_row(board) != False:
        print_board(board)
        if check_row(board) == 'X':
            print('You win!')
        else:
            print('Computer wins')  
        return False
    elif check_column(board) !=False:
        print_board(board)
        if check_row(board) == 'X':
            print('You win!')
        else:
            print('Computer wins')  
        return False
    elif check_diagonal(board) != False:
        print_board(board)
        if check_row(board) == 'X':
            print('You win!')
        else:
            print('Computer wins')
        return False


def check_tie(board):
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
    exit = input('Do you want to play again? (Y or N) ')
    if exit.lower() == 'y':
        return True
    else:
        print('Thanks for playing!') 
        return False  


def winner(board, letter):
    return ((board[0] == board[1] == board[2] == letter) or
        (board[3] == board[4] == board[5] == letter) or
        (board[6] == board[7] == board[8] == letter) or
        (board[0] == board[3] == board[6] == letter) or
        (board[1] == board[4] == board[7] == letter) or
        (board[2] == board[5] == board[8] == letter) or
        (board[0] == board[4] == board[8] == letter) or
        (board[2] == board[1] == board[6] == letter))  


def computer(board):
    possible_moves = []
    for i in range(0,9):
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


print('Welcome to Tic Tac Toe! \nYou are X, the computer is O. \nYou go first - choose your move by selecting your space on the board.\nGet a straight line of Xs (row, column, diagonal) to win.')
welcome()


print_board(board)
player_input(board)