import pygame
from instances import win
from background import squares
from vars import *

# pygame.init()

def hover():
    pos = pygame.mouse.get_pos()
    x, y  = pos[0], pos[1]

    for line in squares:
        for square in line:
            # tests if cursor is on the square
            if x >= (square.x) and x <= (self.xpos + 109) and y >= (self.ypos) and y <= (self.ypos + 109):
                # square is surrounded with grey rectangle
                pygame.draw.rect(win, (130, 130, 130), (square.x, square.y, squarewidth, squarewidth), 5)
