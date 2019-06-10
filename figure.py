import pygame
import instances

class figure():
    def __init__(self, player, xpos, ypos, URI):
        self.player = player
        self.position = position
        self.xpos = (xpos - 1) * 110 + 520
        self.ypos = (ypos - 1) * 110 + 520
        img = pygame.image.load(URI)
