from Piece import Piece
class Table:
    __tab = []
   

    def __init__(self, rows, cols):
        self.__cols = cols
        self.__rows = rows
        self.__tab = [[' ' for j in range(cols)] for i in range(rows)]
        self.board = []
        self.redLeft = self.blackLeft = 12
        self.redKings = self.blackKings = 0

    def Remove(self, piece):
        if piece.getColor() == "\033[31mR\033[0m":
            self.redLeft -= 1
        if piece.getColor() == "\033[30mB\033[0m":
            self.blackLeft -= 1
        self.__tab[piece.getRow()][piece.getCol()] = '[] '
        if piece in self.board:
            self.board.remove(piece)
    
    def getWinner(self):
        '''Check for tie maybe'''
        return self.redLeft, self.blackLeft
  


    def movePiece(self, Cpiece, newRow, newCol):
        #piece = self.__tab[oldRow][oldCol]
        if Cpiece == '[] ':
            raise ValueError('No piece to move at the given position')
        if self.__tab[newRow][newCol] != str(Cpiece):
            if self.__tab[newRow][newCol] != '[] ':
                print(self.getPiece(newRow, newCol))
                raise ValueError('The destination square is not empty')
        if newRow == self.__rows-1 or newRow == 0:
            Cpiece.makeKing()
            if Cpiece.getColor() == "\033[31mR\033[0m":
                self.redKings += 1
            else:
                self.blackKings += 1
        self.__tab[Cpiece.getRow()][Cpiece.getCol()] = '[] '
        Cpiece.move(newRow, newCol)
        self.__tab[newRow][newCol] = str(Cpiece)
        
        


    def getPosition(self, piece):
        for r in range(self.__rows):
            for c in range(self.__cols):
                if str(piece) == self.__tab[r][c]:
                    return r, c

    def getPiece(self, row, col):
        for piece in self.board:
            if self.__tab[row][col] == str(piece):
                return piece
        return -1    
            

    def addPiece(self, piece):
        self.board.append(piece)
        self.__tab[piece.getRow()][piece.getCol()] = str(piece)
        if piece.getRow() < 0 or piece.getRow() >= self.__rows or piece.getCol() < 0 or piece.getCol() >= self.__cols:
            raise Exception("Invalid entry")
        
    def createBoard(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                if (i + j) % 2 == 0:
                    self.__tab[i][j] = '[] '
                else:
                    self.__tab[i][j] = '[] '

    def listPieces(self, piece):
        self.board.append(piece)

    def getPieces(self):
        return self.board
    
    def validSelection(self, piece):
        print(self.__str__())
        if piece != -1:
            col = piece.getCol()
            row = piece.getRow()
            color = piece.getColor()

            if (color == '\033[30mB\033[0m' and row == (self.__rows-3)) or (color == '\033[31mR\033[0m' and row == (self.__rows-6)):
                return True

        # check for valid selection
            for dr in [-1, 1]:
                for dc in [-1, 1]:
                    rSpace = row + dr
                    cSpace = col + dc
                    if rSpace < 0 or rSpace >= self.__rows or cSpace < 0 or cSpace >= self.__cols:
                        continue
                    pieceInSpace = self.getPiece(rSpace, cSpace)
                    if pieceInSpace == -1:
                        return True
                    if pieceInSpace.getColor() == color:
                        continue
                    if abs(rSpace - row) == 1 and abs(cSpace - col) == 1:
                        return True

        return False
    
    def validMove(self, piece, move):
        print(self.__str__())
        # Get the starting and ending positions of the move
        can = False
        startRow, startCol = move[0]
        endRow, endCol = move[-1]

        # check if new position is occupied
        if self.__tab[endRow][endCol] != '[] ':
            return False
            

        # check if move is diagonal
        if abs(endCol - startCol) != abs(endRow - startRow):
            return False
        
        # if piece is king
        if not piece.isKing():
        # if not then check if move is in correct direction (up for player 1, down for player 2)
            if piece.getColor() == '\033[30mB\033[0m' and endRow - startRow > 0:
                return False
            if piece.getColor() == "\033[31mR\033[0m" and endRow - startRow < 0:
                return False

        # check if move is one or two spaces
        if abs(endCol - startCol) not in [1, 2] or abs(endRow - startRow) not in [1, 2]:
            return False
        
    
        # check if move is a capture move
        if abs(endCol - startCol) == 2:
            midX = (endCol + startCol) // 2
            midY = (endRow + startRow) // 2
            midPiece = self.getPiece(midY, midX)
            if midPiece == -1 or midPiece.getColor() == piece.getColor():
                return False
            else:
                self.Remove(midPiece)
                #self.__tab[midY][midX] = '[] '
                '''Add like a doouble jump somewhere'''
                   # check if a double jump is possible
                can = self.canDoubleJump(piece, endRow, endCol)

    # if all checks pass, move is valid
        # If land in endRow then king
        if endRow == 0 or endRow == self.__rows-1:
            piece.makeKing()
            self.__tab[endRow][endCol] = str(piece)
        return True, can

    
    def canDoubleJump(self, piece, row, col):
        print(self.__str__())

        self.__tab[piece.getRow()][piece.getCol()] = '[] '
        piece.move(row, col)
        self.__tab[row][col] = str(piece)
        
        print(self.__str__())

        if not piece.isKing():
            # check for backwardness
            if piece.getColor() == '\033[30mB\033[0m' and row >= self.__rows-3:
                return False
            if piece.getColor() == '\033[31mR\033[0m' and row <= 2:
                return False
        
        # check all diagonal moves from current position
        for dr in [-1, 1]:
            for dc in [-1, 1]:
                CapPieceRow = row + dr
                CapPieceCol = col + dc
                if CapPieceRow < 0 or CapPieceRow >= self.__rows or CapPieceCol < 0 or CapPieceCol >= self.__cols:
                    continue
                # If the piece we have is the correct piece and the next piece we're trying to capture isn't an open space and is bounds of play and the space diagonally after the capPiece is open then double jump
                if self.__tab[CapPieceRow+dr][CapPieceCol+dc] :
                    print(f"This piece: {self.__tab[row][col]}\nWill skip this piece: {self.__tab[CapPieceRow][CapPieceCol]}\nTo land here: {self.__tab[CapPieceRow+dr][CapPieceCol+dc]}\n")
                    if self.__tab[row][col] == str(piece) and self.__tab[CapPieceRow][CapPieceCol] != '[] ' and CapPieceRow+dr >= 0 and CapPieceRow+dr < self.__rows and CapPieceCol+dc >= 0 and CapPieceCol+dc < self.__cols and self.__tab[CapPieceRow+dr][CapPieceCol+dc] == '[] ':
                        midPiece = self.getPiece(CapPieceRow, CapPieceCol)
                        if midPiece != -1 and midPiece.getColor() != piece.getColor():
                            # Check if the capture piece is behind the current piece and the current piece is not a king
                            if (piece.getColor() == '\033[30mB\033[0m' and (CapPieceRow - row > 0)) or (piece.getColor() == '\033[31mR\033[0m' and (CapPieceRow-row < 0)) and not piece.isKing():
                                continue
                        return True
                        
        return False

    def __str__(self):
        table_str = ""
        for row in self.__tab:
            table_str += " ".join(row) + "\n"
        return table_str