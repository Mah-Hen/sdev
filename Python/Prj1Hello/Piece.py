class Piece:
    __color = None
    __num = None

    def __init__(self, color, num, row=0, col=0, king=False):
        self.__color = color
        self.king = king
        self.__num = num
        self.col = col
        self.row = row


    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col
    
    def getNum(self):
        return self.__num
    
    def setNum(self, num):
        self.__num = num
    
    def getPosition(self):
       return self.row, self.col
    
    def setPosition(self, row, col):
        self.col = col
        self.row = row


    def getColor(self):
        return self.__color
    

    def makeKing(self):
        self.king = True
        if self.__color == '\033[31mR\033[0m':
            self.setNum('\033[31mK \033[0m')
        if self.__color == '\033[30mB\033[0m':
            self.setNum('\033[30mK \033[0m')


    def isKing(self):
        return self.king
    
    def move(self, row, col):
        self.row = row
        self.col = col

    def toPiece(self, str):
        return self.fromStr(str)
        

    @classmethod
    def fromStr(cls, pieceString):
        color = pieceString[0]
        num = int(pieceString[1:])
        return cls(color, num)


    def __str__(self):
        return f"{self.__color}{self.__num}"
    


    

