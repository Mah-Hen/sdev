from checker.constants import BLACK, RED, WHITE, ROWS, COLS, SQUARE_SIZE #.constants the "." is for importing from same package
from  checker.Piece import Piece
import pygame

'''Checker Board'''
class board:
        def __init__(self):
            self.board = []
            self.redLeft = self.whiteLeft = 12 #red n white piece leftover
            self.redKings = self.whiteKings = 0
            self.createBoard()

        def drawSquares(self, WIN): #win stands for window
            WIN.fill(BLACK)
            for row in range(ROWS):
                for col in range(row%2, COLS, 2):
                    pygame.draw.rect(WIN, RED, (row*SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


        def remove(self, pieces):
            for piece in pieces:
                self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.redLeft -=1
                else:
                    self.whiteLeft -= 1
        
        def winner(self):
            if self.redLeft <= 0:
                return WHITE
            elif self.whiteLeft <= 0:
                return RED
            
            return None

        def move(self, piece, row, col):
            self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col] #swap places, or position in a list
            piece.move(row, col)

            if row == ROWS-1 or row == 0:
                piece.makeKing()
                if piece.color == WHITE:
                    self.whiteKings += 1
                else:
                    self.redKings += 1
            

        def getPiece(self, row, col):
            return self.board[row][col]
        
        def createBoard(self):
            for row in range(ROWS):
                self.board.append([])
                for col in range(COLS):
                    if col % 2 == ((row+1)%2): # if (0%2) is equal to ((0+1)%2) then input the checker
                        if row < 3:
                            self.board[row].append(Piece(row, col, WHITE)) # adding White Checker pieces to board list and board
                        elif row >  4:
                            self.board[row].append(Piece(row, col, RED)) # adding White Checker pieces to board list and board
                        else:
                            self.board[row].append(0) # blank piece
                    else:
                        self.board[row].append(0) # blank piece

        def drawBoard(self, WIN):
            
            self.drawSquares(WIN)
            for row in range(ROWS):
                for col in range(COLS):
                    piece = self.board[row][col]
                    if piece != 0:
                        #pc = piece(row, col, WHITE)
                        piece.drawPiece(WIN)


        
        
        def getValidMove(self, piece):
            '''Checking the validated moves that a piece is able to make'''
            moves = {}
            left = piece.col - 1
            right = piece.col + 1
            row = piece.row

            if piece.color == RED or piece.king:
                moves.update(self.traverseLeft(row-1, max(row-3, -1), -1, piece.color, left)) # start above the current row we're at and going to stop at two current above rows to the last row if need be. I'm going to decrement in the for loop and start at left column. 
                moves.update(self.traverseRight(row-1, max(row-3, -1), -1, piece.color, right))
            if piece.color == WHITE or piece.king:
                moves.update(self.traverseLeft(row+1, min(row+3, ROWS), 1, piece.color, left)) # start above the current row we're at and going to stop at two current above rows to the last row if need be. I'm going to decrement in the for loop and start at left column. 
                moves.update(self.traverseRight(row+1, min(row+3, ROWS), 1, piece.color, right))
            
            return moves
        
        def traverseLeft(self, start, stop, step, color, left, skipped=[]):
            '''If we find an empty square and we skipped we can add the last move and the next move to know where we can move to, if we only skipped and not in the last spot then add move to list of valid moves; if skipped over a piece we are now preparing for a double or triple jump. Now we gotta recalculate the position of our movement, up or down.  , otherwise if it is not and the color looks like our color then we can't move there. If the isn't our color and it is an empy square then we can jump over it.   '''
            moves = {}
            last = []
            for r in range(start, stop, step):
                if left < 0:
                    break
                current = self.board[r][left]
                if current == 0:
                    if skipped and not last:
                        break
                    elif skipped:
                        moves[(r, left)] = last+skipped
                    else:
                        moves[(r, left)] = last
                    
                    if last:
                        if step == -1:
                            row = max(r-3, 0)
                        else:
                            row = min(r+3, ROWS)

                        moves.update(self.traverseLeft(r+step,row, step,  color, left-1, skipped=last))
                        moves.update(self.traverseRight(r+step,row, step,  color, left+1, skipped=last))
                    break
                elif current.color == color:
                    break
                else:
                    last = [current]
                
                    
                left -= 1
            return moves

        def traverseRight(self, start, stop, step, color, right, skipped=[]):
            moves = {}
            last = []
            for r in range(start, stop, step):
                if right >= COLS:
                    break

                current = self.board[r][right]
                if current == 0:
                    if skipped and not last:
                        break
                    elif skipped:
                        moves[(r, right)] = last+skipped
                    else:
                        moves[(r, right)] = last
                    
                    if last:
                        if step == -1:
                            row = max(r-3, 0)
                        else:
                            row = min(r+3, ROWS)

                        moves.update(self.traverseLeft(r+step,row, step,  color, right-1, skipped=last))
                        moves.update(self.traverseRight(r+step,row, step,  color, right+1, skipped=last))
                    break
                elif current.color == color:
                    break
                else:
                    last = [current]
                
                    
                right += 1
            return moves