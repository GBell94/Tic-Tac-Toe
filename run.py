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




print('Welcome to Tic Tac Toe! \nYou are X, the computer is O. \nYou go first - choose your move by selecting your space on the board.\nGet a straight line of Xs (row, column, diagonal) to win.')
welcome()