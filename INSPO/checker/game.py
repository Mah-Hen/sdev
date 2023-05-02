import pygame
from checker.constants import RED, WHITE, BLUE, SQUARE_SIZE
from checker.Board import board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.Board.drawBoard(self.win)
        self.drawvalidMoves(self.validMoves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.Board = board()
        self.turn = RED
        self.validMoves = {}


    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.Board.getPiece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.validMoves = self.Board.getValidMove(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.Board.getPiece(row, col)
        if self.selected and piece == 0 and (row, col) in self.validMoves:
            self.Board.move(self.selected, row, col)
            skipped = self.validMoves[(row, col)]
            if skipped:
                self.Board.remove(skipped)
            self.changeTurn()
        else:
            return False

        return True

    def drawvalidMoves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def changeTurn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED