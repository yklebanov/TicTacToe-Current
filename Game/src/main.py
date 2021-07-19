# Project Name: Tic-Tac-Toe
# Author: Yasha Klebanov

from Board import Board


currentBoard = Board()
# Validates user's input
def valid_input(input):
    if input.isdigit() and (1 <= int(input) < 10):
        return True
    else:
        return False

# Main game Loop
game_over = False
while game_over == False:
    currentBoard.print_board(numbered=True)
    # Player X's Turn
    player = "X"
    user_input = 0
    flag = True
    while flag:
        user_input = input("Where do you want to move? ")
        if valid_input(user_input):
            flag = False
    user_input = int(user_input)
    currentBoard.setToken(user_input, player)
    currentBoard.print_board(numbered=False)
    #board[user_input-1] = player
    #print_board()

    # Player O's Turn
    player = "O"
    user_input = 0
    flag = True
    while flag:
        user_input = input("Where do you want to move? ")
        if valid_input(user_input):
            flag = False
    user_input = int(user_input)
    currentBoard.setToken(user_input, player)
    currentBoard.print_board(numbered=False)
    #board[user_input - 1] = player
    #print_board()
