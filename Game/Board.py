# Board.py - Prints the board, showing the numbers of the positions

# positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
class Board:
    board = None
    # Constructor Class --> Set Board to Default
    def __init__(self):
        self.board = [' ', ' ', ' ',
                     ' ', ' ', ' ',
                     ' ', ' ', ' ']

    def setToken(self, pos, token):
        if self.__checkPos(pos):
            self.board[pos-1] = token
            return True
        else:
            return False

    def getToken(self, pos):
        return self.board[pos-1]

    def __checkPos(self, pos):
        if pos == ' ':
            return True

    # Prints the board, showing the current state of X, O, and blanks
    def print_board(self):
    # board[place] = symbol
        print(str(self.board[0]) + " | " + str(self.board[1]) + " | " + str(self.board[2]))
        print("---------")
        print(str(self.board[3]) + " | " + str(self.board[4]) + " | " + str(self.board[5]))
        print("---------")
        print(str(self.board[6]) + " | " + str(self.board[7]) + " | " + str(self.board[8]))