import re
import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"] 
currentPlayer = "X" 
winner = None
gameRunning = True


#take player input
def getInput(board):
    boardInp = int(input("Enter Position between 1-9: "))
    if boardInp >= 1 and boardInp <= 9 and board[boardInp - 1] == "-": #checks to see if that spot is empty
        board[boardInp - 1] = currentPlayer
    else:
        print("ERROR! Player in that spot!")
    '''
    if letterInp.isnumeric():
        print("Input Numeric Error")
        getInput()
    else: 
        letterInp = letterInp.lower()
        if re.match("^[sxo]", letterInp):
            return letterInp
        else:
            print("Incorrect Character Error ")
            getInput()
    '''
def checkHorizontal(board):
    global winner 
    if board[0] == board[1] == board[2] and board[0] != "-" :
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-" :
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-": 
        winner = board[6]
        return True


def checkDiagonal(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-" :
        winner = board[0]
        return True
    elif board[2] == board[4] == board[2] and board[2] != "-": 
        winner = board[3]
        return True
    


def checkVertical(board): 
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-" :
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-": 
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-": 
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False 

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    
#printing game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def checkWin():
    global currentPlayer
    global gameRunning
   
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
       print(f"{winner} Won the game")
       gameRunning = False
  

def computer(Board):
    global currentPlayer
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] ="O"
            switchPlayer()

    

#printBoard()



def main():
    while gameRunning == True:
        printBoard(board)
        getInput(board)
        if checkWin():
            printBoard(board)
        else: 
            checkTie(board)

        switchPlayer()
        
            

    



main()


    
#check for win or tie

#check for win or tie again