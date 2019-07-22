import pygame
import instances
import background
from vars import *

class piece():
    def __init__(self, player, position):
        self.player = player # Boolean

        # self.position = position # on Chessboard, example: "B3"

        square = position

        self.xpos = square[0]
        self.ypos = square.[1]
        self.selected = False

        self.moves = moves # ex. [[self.xpos + 1, self.ypos - 1], [self.xpos + 1], [self.xpos + 1, self.ypos + 1]]


        # self.vertical = moves[0]
        # self.horizontal = moves[1]
        # self.diagonal = moves[2]
        # self.horse = moves[3]
        # self.range = range

        # img = pygame.image.load(URI)
    def hover():
            # tests if cursor is on the square
            if x >= (square.x) and x <= (square.x2) and y >= square.y and y <= square.y2:
                # square is surrounded with grey rectangle
                pygame.draw.rect(win, (130, 130, 130), (square.x, square.y, squarewidth, squarewidth), 5)

                # tests if piece is chosen
                if button1 == True:
                    self.selected = True

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
