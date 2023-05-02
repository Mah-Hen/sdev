import pygame
from checker.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED   
from checker.Board import board
from checker.game import Game


FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # Window
pygame.display.set_caption('Checkers') # name of game

def getROWCOL(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col

def main():
    run = True
    clock = pygame.time.Clock() # FPS
    Board = board() 
    game = Game(WINDOW)

    
    

    
    
    while run:
        
        
        
        clock.tick(FPS)
        if Board.winner() != None:
            print(Board.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If quit exit game loop and exit 
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = getROWCOL(position)
                game.select(row, col)

                

        game.update()
        
            
            
    pygame.quit()

main()
