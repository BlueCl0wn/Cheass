import pygame
# from squareclass import square
from vars import *
from squares import squares
from instances import win


def background():
    win.fill((150, 150, 150))

    pygame.draw.rect(win, (110, 60, 19), (x_border_distance, y_border_distance, 960, 960))
    pygame.draw.rect(win, (0, 0, 0), (x_border_distance + 40, y_border_distance + 40, 880, 880))

    for squareline in squares:
        for square in squareline:
            square.draw()
