import pygame
from instances import win
from vars import *

class square():
    def __init__(self, x, y, color):
        self.x = (x - 1) * squarewidth + x_border_distance + 40
        self.y = (y - 1) * squarewidth + y_border_distance + 40
        self.x2 = self.x + 109
        self.y2 = self.y + 109

        self.width = 110
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def rect_green(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.width), 3)

    def rect_red(self):
        pygame.draw.rect(win, (0, 255,0), (self.x, self.y, self.width, self.width), 5)
