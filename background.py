import pygame
from squareclass import square
from vars import *
from instances import *

# 1
A1 = square(1, 1, WHITE)
B1 = square(1, 2, BLACK)
C1 = square(1, 3, WHITE)
D1 = square(1, 4, BLACK)
E1 = square(1, 5, WHITE)
F1 = square(1, 6, BLACK)
G1 = square(1, 7, WHITE)
H1 = square(1, 8, BLACK)

# 2
A2 = square(2, 1, BLACK)
B2 = square(2, 2, WHITE)
C2 = square(2, 3, BLACK)
D2 = square(2, 4, WHITE)
E2 = square(2, 5, BLACK)
F2 = square(2, 6, WHITE)
G2 = square(2, 7, BLACK)
H2 = square(2, 8, WHITE)

# 3
A3 = square(3, 1, WHITE)
B3 = square(3, 2, BLACK)
C3 = square(3, 3, WHITE)
D3 = square(3, 4, BLACK)
E3 = square(3, 5, WHITE)
F3 = square(3, 6, BLACK)
G3 = square(3, 7, WHITE)
H3 = square(3, 8, BLACK)

# 4
A4 = square(4, 1, BLACK)
B4 = square(4, 2, WHITE)
C4 = square(4, 3, BLACK)
D4 = square(4, 4, WHITE)
E4 = square(4, 5, BLACK)
F4 = square(4, 6, WHITE)
G4 = square(4, 7, BLACK)
H4 = square(4, 8, WHITE)

# 5
A5 = square(5, 1, WHITE)
B5 = square(5, 2, BLACK)
C5 = square(5, 3, WHITE)
D5 = square(5, 4, BLACK)
E5 = square(5, 5, WHITE)
F5 = square(5, 6, BLACK)
G5 = square(5, 7, WHITE)
H5 = square(5, 8, BLACK)

# 6
A6 = square(6, 1, BLACK)
B6 = square(6, 2, WHITE)
C6 = square(6, 3, BLACK)
D6 = square(6, 4, WHITE)
E6 = square(6, 5, BLACK)
F6 = square(6, 6, WHITE)
G6 = square(6, 7, BLACK)
H6 = square(6, 8, WHITE)

# 7
A7 = square(7, 1, WHITE)
B7 = square(7, 2, BLACK)
C7 = square(7, 3, WHITE)
D7 = square(7, 4, BLACK)
E7 = square(7, 5, WHITE)
F7 = square(7, 6, BLACK)
G7 = square(7, 7, WHITE)
H7 = square(7, 8, BLACK)

# 8
A8 = square(8, 1, BLACK)
B8 = square(8, 2, WHITE)
C8 = square(8, 3, BLACK)
D8 = square(8, 4, WHITE)
E8 = square(8, 5, BLACK)
F8 = square(8, 6, WHITE)
G8 = square(8, 7, BLACK)
H8 = square(8, 8, WHITE)

squares =  [[A1, B1, C1, D1, E1, F1, G1, H1],
            [A2, B2, C2, D2, E2, F2, G2, H2],
            [A3, B3, C3, D3, E3, F3, G3, H3],
            [A4, B4, C4, D4, E4, F4, G4, H4],
            [A5, B5, C5, D5, E5, F5, G5, H5],
            [A6, B6, C6, D6, E6, F6, G6, H6],
            [A7, B7, C7, D7, E7, F7, G7, H7],
            [A8, B8, C8, D8, E8, F8, G8, H8]]

def background():
    win.fill((150, 150, 150))

    pygame.draw.rect(win, (110, 60, 19), (x_border_distance, y_border_distance, 960, 960))
    pygame.draw.rect(win, (0, 0, 0), (x_border_distance + 40, y_border_distance + 40, 880, 880))

    for squareline in squares:
        for square in squareline:
            square.draw()
