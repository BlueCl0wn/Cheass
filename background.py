import pygame
from instances import win
from vars import *


class square():
    def __init__(self, x, y):
        self.x = (x - 1) * 110 + 520
        self.y = (y - 1) * 110 + 100
        self.width = 110
        self.color =(255, 255, 255)
    def draw(self):
        pygame.draw.rect(win, color, (self.x, self.y, self.width, self.width))

# 1
A1 = square(1, 1)
A3 = square(1, 3)
A5 = square(1, 5)
A7 = square(1, 7)

# 2
B2 = square(2, 2)
B4 = square(2, 4)
B6 = square(2, 6)
B8 = square(2, 8)

# 3
C1 = square(3, 1)
C3 = square(3, 3)
C5 = square(3, 5)
C7 = square(3, 7)

# 4
D2 = square(4, 2)
D4 = square(4, 4)
D6 = square(4, 6)
D8 = square(4, 8)

# 5
E1 = square(5, 1)
E3 = square(5, 3)
E5 = square(5, 5)
E7 = square(5, 7)

# 6
F2 = square(6, 2)
F4 = square(6, 4)
F6 = square(6, 6)
F8 = square(6, 8)

# 7
G1 = square(7, 1)
G3 = square(7, 3)
G5 = square(7, 5)
G7 = square(7, 7)

# 8
H2 = square(8, 2)
H4 = square(8, 4)
H6 = square(8, 6)
H8 = square(8, 8)

squares =   [A1, A3, A5, A7,
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

    for square in squares:
        square.draw()
