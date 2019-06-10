import pygame
from instances import win
from vars import *


class field():
    def __init__(self, x, y):
        self.x = (x - 1) * 110 + 520
        self.y = (y - 1) * 110 + 100
        self.width = 110
    def draw(self):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.width))

# 1
A1 = field(1, 1)
A3 = field(1, 3)
A5 = field(1, 5)
A7 = field(1, 7)

# 2
B2 = field(2, 2)
B4 = field(2, 4)
B6 = field(2, 6)
B8 = field(2, 8)

# 3
C1 = field(3, 1)
C3 = field(3, 3)
C5 = field(3, 5)
C7 = field(3, 7)

# 4
D2 = field(4, 2)
D4 = field(4, 4)
D6 = field(4, 6)
D8 = field(4, 8)

# 5
E1 = field(5, 1)
E3 = field(5, 3)
E5 = field(5, 5)
E7 = field(5, 7)

# 6
F2 = field(6, 2)
F4 = field(6, 4)
F6 = field(6, 6)
F8 = field(6, 8)

# 7
G1 = field(7, 1)
G3 = field(7, 3)
G5 = field(7, 5)
G7 = field(7, 7)

# 8
H2 = field(8, 2)
H4 = field(8, 4)
H6 = field(8, 6)
H8 = field(8, 8)

fields =   [A1, A3, A5, A7,
            B2, B4, B6, B8,
            C1, C3, C5, C7,
            D2, D4, D6, D8,
            E1, E3, E5, E7,
            F2, F4, F6, F8,
            G1, G3, G5, G7,
            H2, H4, H6, H8]

def background():
    win.fill((150, 150, 150))

    pygame.draw.rect(win, (110, 60, 19), (480, 60, 960, 960))
    pygame.draw.rect(win, (0, 0, 0), (520, 80 + 20, 880, 880))

    for field in fields:
        field.draw()
