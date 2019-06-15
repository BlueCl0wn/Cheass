import pygame
import instances
from instances import win
from vars import *
import background
import piececlass

pygame.init()

run = True
while run:
    pygame.time.delay(30)

    # Quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and bool(event.mod & pygame.KMOD_ALT)):
            run = False

    background.background()

    pygame.display.update()


pygame.quit()
