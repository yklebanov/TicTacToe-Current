# Board.py - Prints the board, showing the numbers of the positions

class Board:
    board = None
    # Constructor Class --> Set Board to Default
    def __init__(self):
        self.board = [' ', ' ', ' ',
                     ' ', ' ', ' ',
                     ' ', ' ', ' ']

    def setToken(self, pos, token):
        if self.__checkPos(self.getToken(pos)):
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
    def print_board(self, numbered=False):
        if not(numbered):
            # board[place] = symbol
            print(str(self.getToken(1)) + " | " + str(self.getToken(2)) + " | " + str(self.getToken(3)))
            print("---------")
            print(str(self.getToken(4)) + " | " + str(self.getToken(5)) + " | " + str(self.getToken(6)))
            print("---------")
            print(str(self.getToken(7)) + " | " + str(self.getToken(8)) + " | " + str(self.getToken(9)))
        else:
            temp = ""
            count = 1
            for x in self.board:
                if self.__checkPos(x):
                    temp = temp + str(count)
                else:
                    temp = temp + str(x)
                count = count + 1
                
                if count % 3 == 1:
                    if not(count == 10):
                        temp = temp + "\n------\n"
                else:
                    temp = temp + "|"

            print(str(temp))