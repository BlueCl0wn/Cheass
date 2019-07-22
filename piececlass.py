import pygame
import instances
import background
from vars import *
from instances import win
from pieces import pieces

class piece():
    def __init__(self, player, position):
        self.player = player # Boolean
        # self.position = position # on Chessboard, example: "B3"


        self.xpos = (position[0]  - 1) * 110 + 520
        self.ypos = (position[1] - 1) * 110 + 100
        self.selected = False

        self.color = (255, 0, 0) # später weg!!!!!
        # self.img =

        # self.moves = moves # ex. [[self.xpos + 1, self.ypos - 1], [self.xpos + 1], [self.xpos + 1, self.ypos + <1]]


        # self.vertical = moves[0]
        # self.horizontal = moves[1]
        # self.diagonal = moves[2]
        # self.horse = moves[3]
        # self.range = range

        # img = pygame.image.load(URI)

    def draw(self, x, y):
        pygame.draw.rect(win, self.color, (self.xpos, self.ypos,  60, 60))

    def hover(self, x, y, button1):
            # tests if cursor is on the square
            if x >= (self.xpos) and x <= (self.xpos + 109) and y >= (self.ypos) and y <= (self.ypos + 109):
                # square is surrounded with grey rectangle
                pygame.draw.rect(win, (130, 130, 130), (self.xpos, self.ypos, squarewidth, squarewidth), 5)

                # tests if piece is chosen
                if button1 == True:
                    for piece in pieces:
                        piece.selected = False
                        piece.color = (255, 0, 0)
                    self.selected = True
                    self.color = (0, 255, 0)

            else:
                pass

    def select_piece(self):
        print(self.xpos)

# class king(piece): # Koenig
#     def __init__(self, m):
#         self.character = king
#
# class queen(piece): # Dame
#     def __init__(self):
#         self.character = queen
#
# class rook(piece): # Turm
#     def __init__(self):
#         self.character = farmer
#
# class knight(piece): # Springer
#     def __init__(self):
#         self.character = farmer
#
# class pawn(piece): # Bauer
#     def __init__(self):
#         self.character = farmer
