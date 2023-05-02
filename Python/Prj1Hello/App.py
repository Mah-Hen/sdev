from Table import Table
from Piece import Piece
import os
import time 

class App:
    def __init__(self, color, win=False):
        self.turn = color
        self.win = win
    
    def getMove(self, table):
        row = 0
        print("Collums traverse left (1) to right (8)")
        col = input("Please enter the column: ").strip()
        if len(col) == 0:
            print("Error!")
            time.sleep(1.5)
            clearScreen()
            print(table)
            row, col = self.getMove(table)
            
        if type(col) != int:
            if not col.isnumeric():
                if not col.isspace():
                    col = col.lower()
                    if col == "quit":
                        return (-1, -1)
                    else:
                        print("Error!")
                        time.sleep(1.5)
                        clearScreen()
                        print(table)
                        row, col = self.getMove(table)
                else:
                    print("Error!")
                    time.sleep(1.5)
                    clearScreen()
                    print(table)
                    row, col = self.getMove(table)
            
            else:
                col = int(col)  
                if col < 1 or col >=9:
                    print("Error!")
                    time.sleep(1.5)
                    clearScreen()
                    print(table)
                    row, col = self.getMove(table)
                    
                col = col-1

            time.sleep(1.5)
            clearScreen()

            print(table)
            print("Rows descends top (1) to bottom (8)")
            row = input("Please enter the row: ").strip()
            if row.isspace():
                row, col = self.getMove(table)
                
            if type(row) != int:
                if not row.isnumeric():
                    if not row.isspace():
                        row = row.lower()
                        if row == "quit":
                            return (-1, -1)
                        else:
                            print("Error!")
                            time.sleep(1.5)
                            clearScreen()
                            print(table)
                            row, col = self.getMove(table)
                    else:
                        print("Error!")
                        time.sleep(1.5)
                        clearScreen()
                        print(table)
                        row, col = self.getMove(table)            
                    
                else:
                    row = int(row)  
                    if row < 1 or row >= 9:
                        print("Error!")
                        time.sleep(1.5)
                        clearScreen()
                        print(table)
                        row, col  = self.getMove(table)
                        
                    row = row - 1

        return row, col
    
    def changeTurn(self):
        if self.turn == "\033[31mR\033[0m":
            self.turn = "\033[30mB\033[0m"
        else:
            self.turn = "\033[31mR\033[0m"
    
    def getTurn(self):
        return self.turn



R1 = Piece("\033[31mR\033[0m", "\033[31m1 \033[0m", 0, 1)
R2 = Piece("\033[31mR\033[0m", "\033[31m2 \033[0m", 0, 3)
R3 = Piece("\033[31mR\033[0m", "\033[31m3 \033[0m", 0, 5)
R4 = Piece("\033[31mR\033[0m", "\033[31m4 \033[0m", 0, 7)
R5 = Piece("\033[31mR\033[0m", "\033[31m5 \033[0m", 1, 0)
R6 = Piece("\033[31mR\033[0m", "\033[31m6 \033[0m", 1, 2)
R7 = Piece("\033[31mR\033[0m", "\033[31m7 \033[0m", 1, 4)
R8 = Piece("\033[31mR\033[0m", "\033[31m8 \033[0m", 1, 6)
R9 = Piece("\033[31mR\033[0m", "\033[31m9 \033[0m", 2, 1)
R10 = Piece("\033[31mR\033[0m", "\033[31m10\033[0m", 2, 3)
R11 = Piece("\033[31mR\033[0m", "\033[31m11\033[0m", 2, 5)
R12 = Piece("\033[31mR\033[0m", "\033[31m12\033[0m", 2, 7)

B1 = Piece("\033[30mB\033[0m", "\033[30m1 \033[0m", 7, 0)
B2 = Piece("\033[30mB\033[0m", "\033[30m2 \033[0m", 7, 2)
B3 = Piece("\033[30mB\033[0m", "\033[30m3 \033[0m", 7, 4)
B4 = Piece("\033[30mB\033[0m", "\033[30m4 \033[0m", 7, 6)
B5 = Piece("\033[30mB\033[0m", "\033[30m5 \033[0m", 6, 1)
B6 = Piece("\033[30mB\033[0m",  "\033[30m6 \033[0m", 6, 3)
B7 = Piece("\033[30mB\033[0m",  "\033[30m7 \033[0m", 6, 5)
B8 = Piece("\033[30mB\033[0m",  "\033[30m8 \033[0m",6, 7)
B9 = Piece("\033[30mB\033[0m", "\033[30m9 \033[0m", 5, 0)
B10 = Piece("\033[30mB\033[0m", "\033[30m10\033[0m", 5, 2)
B11 = Piece("\033[30mB\033[0m","\033[30m11\033[0m", 5, 4)
B12 = Piece("\033[30mB\033[0m", "\033[30m12\033[0m", 5, 6)


def setTable(table):
    table.addPiece(R1)
    table.addPiece(R2)
    table.addPiece(R3)
    table.addPiece(R4)
    table.addPiece(R5)
    table.addPiece(R6)
    table.addPiece(R7)
    table.addPiece(R8)
    table.addPiece(R9)
    table.addPiece(R10)
    table.addPiece(R11)
    table.addPiece(R12)

    table.addPiece(B1)
    table.addPiece(B2)
    table.addPiece(B3)
    table.addPiece(B4)
    table.addPiece(B5)
    table.addPiece(B6)
    table.addPiece(B7)
    table.addPiece(B8)
    table.addPiece(B9)
    table.addPiece(B10)
    table.addPiece(B11)
    table.addPiece(B12)

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear') 


def doubleMove(can, game, table, piece):
    clearScreen()
    while can:
        print(table)
        # Recursion incoming
        print("Double Jump")
        print(f"RETRIEVE SPACE for {piece}")
        dRow, dCol = game.getMove(table) # type: ignore
        if dRow == -1 or dCol == -1:
            print("Quiting...")
            time.sleep(1.5)
            clearScreen()
            can = False
            quit()
        elif table.validMove(piece, ((piece.getRow(), piece.getCol()),(dRow, dCol))):
            table.movePiece(piece, dRow, dCol)
            can = table.canDoubleJump(piece, dRow, dCol)
        else:
            '''FIX THIS ELSE STATEMENT, make it more efficient'''
            clearScreen()
            print(f"Retrieved {table.getPiece(piece.getRow(), piece.getCol())}. Where do you want to put it?")
            continue
    
    if not can:
        game.changeTurn()

        time.sleep(1)
        clearScreen()


def Winner(table):
    red, black = table.getWinner()

    if red == 0:
        time.sleep(1.5)
        clearScreen()
        print("Black Wins!")
        return False
    elif black == 0:
        time.sleep(1.5)
        clearScreen()
        print("Red Wins!")
        return False
    else: 
        return True
        

def main():

    running = True
    table = Table(8,8)
    game = App(B1.getColor())
    table.createBoard()
    setTable(table)


    
    
    while running:
        try:
            print(table)    
            print(f"RETRIEVE {game.getTurn()} PIECE")
            pRow, pCol = game.getMove(table) 
            if pRow == -1 or pCol == -1:
                print("Quiting...")
                time.sleep(1.5)
                clearScreen()
                running = False
                quit()

            piece = table.getPiece(pRow, pCol)
            if not table.validSelection(piece): #Flag
                time.sleep(1.5)
                clearScreen()
                continue
            elif piece.getColor() == game.getTurn():  # type: ignore

        

                print(table)

                print(f"RETRIEVE SPACE for {piece}")
                dRow, dCol = game.getMove(table) # type: ignore
                if dRow == -1 or dCol == -1:
                    print("Quiting...")
                    time.sleep(1.5)
                    clearScreen()
                    running = False
                    quit()

                time.sleep(1)
                clearScreen()
                valid, can = table.validMove(piece, ((pRow, pCol),(dRow, dCol))) # type: ignore
                if  valid: # type: ignore
                    if not can:
                        game.changeTurn()
                        table.movePiece(piece, dRow, dCol)
                    else:
                        doubleMove(can, game, table, piece)

                else:
                    '''FIX THIS ELSE STATEMENT, make it more efficient'''
                    clearScreen()
                    print(f"Retrieved {table.getPiece(pRow, pCol)}. Where do you want to put it?")
                    continue
                    
            else:
                clearScreen()
                print("")
                continue
        except ValueError:
            clearScreen()
            print("")
            continue
        except TypeError:
            clearScreen()
            print("")
        except IndexError:
            clearScreen()
            print("")
            game.changeTurn()   
        clearScreen()
        running = Winner(table)


    
    


main()
