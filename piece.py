import pygame
import instances
import background

class piece():
    def __init__(self, player, xpos, ypos, URI, moves, range):
        self.player = player # Boolean

        self.position = position # on Chessboard, example: "B3"

        self.xpos = (xpos - 1) * 110 + 520
        self.ypos = (ypos - 1) * 110 + 520

        self.vertical = moves[0]
        self.horizontal = moves[1]
        self.diagonal = moves[2]
        self.horse = moves[3]
        self.range = range

        img = pygame.image.load(URI)

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
