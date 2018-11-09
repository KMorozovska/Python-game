from pygame.locals import *
import pygame, os
from LevelSurface import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

mw_width = 800
mw_height = 600

mainWindow = pygame.display.set_mode((mw_width, mw_height),RESIZABLE)
mainWindow.fill((158,128,128))

pygame.display.set_caption('Incredible Machine!')

current_level = LevelSurface(1)

level = current_level.create_level(False)
#level = pygame.transform.scale(level, (650,600))

mainWindow.blit(level,[0,0])

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()