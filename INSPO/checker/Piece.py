import pygame
from checker.constants import RED, GREY, BLUE, SQUARE_SIZE

class Piece:
        PADDING = 15
        OUTBORDER = 2

        def __init__(self, row, col, color):
            self.row = row
            self.col = col
            self.color = color
            self.king = False
            self.x = 0
            self.y = 0
            self.calcPosition()

        def calcPosition(self):
            self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 # (100*1 + 100//2) = 150
            self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 # (100*1 + 100//2) = 150

        def makeKing(self):
            self.king = True

        def drawPiece(self, win):
            radius = SQUARE_SIZE//2 - self.PADDING
            pygame.draw.circle(win, GREY, (self.x, self.y), radius+self.OUTBORDER) #Checker's border
            pygame.draw.circle(win, self.color, (self.x, self.y), radius) #CHecker piece
            if self.king:
                 pass
                 #make king

        def move(self, row, col):
             self.row = row
             self.col = col
             self.calcPosition()

        def __repr__(self):
            '''Representation of the object'''
            return str(self.color)