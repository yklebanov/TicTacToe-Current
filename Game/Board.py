# Board.py - Prints the board, showing the numbers of the positions

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def print_positions():
    print(str(positions[0]) + " | " + str(positions[1]) + " | " + str(positions[2]))
    print("---------")
    print(str(positions[3]) + " | " + str(positions[4]) + " | " + str(positions[5]))
    print("---------")
    print(str(positions[6]) + " | " + str(positions[7]) + " | " + str(positions[8]))

# Prints the board, showing the current state of X, O, and blanks
def print_board(place, symbol):
    board[place] = symbol
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print("---------")
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print("---------")
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))