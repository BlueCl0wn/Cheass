import pygame
import instances
from instances import win
from vars import *
import background
from hover import hover
from background import squares

pygame.init()

# def select():
#     pos = pygame.mouse.get_pos()
#     x, y  = pos[0], pos[1]
#     button1 = pygame.mouse.get_pressed()[0]
#
#     for piece in pieces:
#         square.hover()

run = True
while run:
    pygame.time.delay(30)

    # Quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and bool(event.mod & pygame.KMOD_ALT)):
            run = False
    background.background()

    # select()

    hover()

    pygame.display.update()


pygame.quit()
