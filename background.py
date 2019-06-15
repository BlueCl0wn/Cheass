import pygame
from instances import win
from vars import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class square():
    def __init__(self, x, y, color):
        self.x = (x - 1) * 110 + 520
        self.y = (y - 1) * 110 + 100
        self.width = 110
        self.color = color
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    def rect_green(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.width), 1)
    def rect_red(self):
        pygame.draw.rect(win, (0, 255,0), (self.x, self.y, self.width, self.width), 1)

# 1
A1 = square(1, 1, WHITE)
A2 = square(1, 2, BLACK)
A3 = square(1, 3, WHITE)
A4 = square(1, 4, BLACK)
A5 = square(1, 5, WHITE)
A6 = square(1, 6, BLACK)
A7 = square(1, 7, WHITE)
A8 = square(1, 8, BLACK)

# 2
B1 = square(2, 1, BLACK)
B2 = square(2, 2, WHITE)
B3 = square(2, 3, BLACK)
B4 = square(2, 4, WHITE)
B5 = square(2, 5, BLACK)
B6 = square(2, 6, WHITE)
B7 = square(2, 7, BLACK)
B8 = square(2, 8, WHITE)

# 3
C1 = square(3, 1, WHITE)
C2 = square(3, 2, BLACK)
C3 = square(3, 3, WHITE)
C4 = square(3, 4, BLACK)
C5 = square(3, 5, WHITE)
C6 = square(3, 6, BLACK)
C7 = square(3, 7, WHITE)
C8 = square(3, 8, BLACK)

# # 4
# D2 = square(4, 2)
# D2 = square(4, 2)
# D2 = square(4, 2)
# D2 = square(4, 2)
# D2 = square(4, 2)
# D4 = square(4, 4)
# D6 = square(4, 6)
# D8 = square(4, 8)
#
# # 5
# E1 = square(5, 1)
# E3 = square(5, 3)
# E5 = square(5, 5)
# E7 = square(5, 7)
#
# # 6
# F2 = square(6, 2)
# F4 = square(6, 4)
# F6 = square(6, 6)
# F8 = square(6, 8)
#
# # 7
# G1 = square(7, 1)
# G3 = square(7, 3)
# G5 = square(7, 5)
# G7 = square(7, 7)
#
# # 8
# H2 = square(8, 2)
# H4 = square(8, 4)
# H6 = square(8, 6)
# H8 = square(8, 8)

squares =   [A1, A3, A5, A7,
            B2, B4, B6, B8,
            C1, C3, C5, C7]
            # D2, D4, D6, D8,
            # E1, E3, E5, E7,
            # F2, F4, F6, F8,
            # G1, G3, G5, G7,
            # H2, H4, H6, H8]

def background():
    win.fill((150, 150, 150))

    pygame.draw.rect(win, (110, 60, 19), (480, 60, 960, 960))
    pygame.draw.rect(win, (0, 0, 0), (520, 80 + 20, 880, 880))

    for square in squares:
        square.draw()
        square.rect_green()
