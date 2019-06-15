import pygame
import instances
import background
from vars import *

class piece():
    def __init__(self, player, position):
        self.player = player # Boolean

        # self.position = position # on Chessboard, example: "B3"

        square = position

        self.xpos = square.x
        self.ypos = square.y


        # self.vertical = moves[0]
        # self.horizontal = moves[1]
        # self.diagonal = moves[2]
        # self.horse = moves[3]
        # self.range = range

        # img = pygame.image.load(URI)

    def select_piece(self):
        print(self.xpos)

abc = piece(1, background.B3)
abc.select_piece()

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
