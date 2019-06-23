import pygame
from instances import win
from background import squares
from vars import *

# pygame.init()

def hover():
    pos = pygame.mouse.get_pos()
    x, y  = pos[0], pos[1]

    for square in squares:
        # tests if cursor is on the square
        if x >= (square.x) and x <= (square.x2) and y >= square.y and y <= square.y2:
            # square is surrounded with grey rectangle
            pygame.draw.rect(win, (square.x, square.y, squarewidth, squarewidth), (150, 150, 150), 5)
