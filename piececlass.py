import pygame
import instances
import background
from vars import *
from instances import win

class piece():
    def __init__(self, player, position):
        self.player = player # Boolean
        # self.position = position # on Chessboard, example: "B3"


        self.xpos = (position[0]  - 1) * 110 + 520
        self.ypos = (position[1] - 1) * 110 + 100
        self.selected = False

        self.color = (255, 0, 0) # später weg!!!!!
        # self.img =

        self.moves = moves # ex. [[self.xpos + 1, self.ypos - 1], [self.xpos + 1], [self.xpos + 1, self.ypos + <1]]


        # self.vertical = moves[0]
        # self.horizontal = moves[1]
        # self.diagonal = moves[2]
        # self.horse = moves[3]
        # self.range = range

        # img = pygame.image.load(URI)

    def draw(self):
        pygame.draw.rect(win, self.color, (self.xpos, self.ypos,  60, 60))

    def moving(self):
        if self.selected = True:
            pass
