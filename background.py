import pygame
from instances import win
from vars import *


class field():
    def __init__(self, x, y):
        self.x = x + 520
        self.y = y + 100
        self.width = 110
        self.color = color

    def draw(self):
        pygame.draw.rect(win, (255, 255, 255), ())

field()



fields = []

def background():
    win.fill((150, 150, 150))

    pygame.draw.rect(win, (110, 60, 19), (480, 60, 960, 960))
    pygame.draw.rect(win, (0, 0, 0), (520, 80 + 20, 880, 880))

    for field in fields:
        field.draw()
