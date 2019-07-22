import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

infos = pygame.display.Info()

screenwidth = infos.current_w
screenheight  = infos.current_h

x_border_distance = (screenwidth - 960) / 2
y_border_distance = (screenheight  - 960) / 2

squarewidth = 110

player = 0
