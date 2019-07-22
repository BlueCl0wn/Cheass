import pygame
from instances import win
from background import squares
from vars import *
from pieces import pieces

# pygame.init()


def hover():
    pos = pygame.mouse.get_pos()
    x, y  = pos[0], pos[1]
    button1 = pygame.mouse.get_pressed()[0]

    for piece in pieces:
        if piece.player == player:
            # tests if cursor is on the square of the piece
            if x >= (piece.xpos) and x <= (piece.xpos + 109) and y >= (piece.ypos) and y <= (piece.ypos + 109):
                # square is surrounded with grey rectangle
                pygame.draw.rect(win, (130, 130, 130), (piece.xpos, piece.ypos, squarewidth, squarewidth), 5)

                # tests if piece is chosen
                if button1 == True:
                    for piec in pieces:
                        piec.selected = False
                        piec.color = (255, 0, 0)
                    piece.selected = True
                    piece.color = (0, 255, 0)
