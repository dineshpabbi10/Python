import os
class tictac:

    def __init__(self):
        self.board = [['1','2','3'],['4','5','6'],['7','8','9']]
        self.player = 'X'
        self.position = list()
        self.abs = {"1" : [0,0] , "2" : [0,1] , "3":[0,2] , "4":[1,0],"5":[1,1],"6":[1,2],"7":[2,0],"8":[2,1],"9":[2,2]}
        self.display()
        self.mark()

    def win(self,mark):
        self.board
        if(mark == self.board[0][0] == self.board[0][1] == self.board[0][2] or mark == self.board[0][0] == self.board[1][1] == self.board[2][2] or mark == self.board[1][0] == self.board[1][1] == self.board[1][2] or mark == self.board[2][0] == self.board[2][1] == self.board[2][2] or mark == self.board[0][0] == self.board[1][0] == self.board[2][0] or mark == self.board[0][1] == self.board[1][1] == self.board[2][1] or mark == self.board[0][2] == self.board[1][2] == self.board[2][2] or mark == self.board[0][2] == self.board[1][1] == self.board[2][0]):
            return True
    def draw(self):
        for x in self.board:
            for y in x:
                if(y == "X" or y == "0"):
                    pass
                else:
                    return False
        return True


    def inPos(self):
        pos = input("Enter the position from 1 to 9\n")
        self.position = self.abs[pos]
        if (self.board[self.position[0]][self.position[1]] != pos):
            print("This position is already filled,Enter a new position")
            self.inPos()


    def mark(self):
        self.inPos()
        self.board[self.position[0]][self.position[1]] = self.player
        self.display()
        if(self.win(self.player) == True):
            print(self.player + " has won the game!")
            self.board = [['1','2','3'],['4','5','6'],['7','8','9']]
            self.player = "X"
            p = input("Enter Y if you want to play the game again \n")
            if(p == "Y" or p == "y"):
                self.display()
                self.mark()
            else:
                print("See ya later !")

        if (self.draw() == True):
            print("The result is a draw !")
            self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            self.player = "X"
            p = input("Enter Y if you want to play the game again \n")
            if (p == "Y" or p == "y"):
                self.display()
                self.mark()
            else:
                print("See ya later !")

        else:
            if(self.player == "X"):
                self.player = "0"
            else:
                self.player = "X"
            self.mark()



    def display(self):
        os.system("cls")
        print("---------")
        for x in self.board:
            for y in x:
                print("|"+y+"|",end="")
            print("\n---------")


obj = tictac()