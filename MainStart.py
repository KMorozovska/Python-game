from pygame.locals import *
import pygame, os
from Level import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

mw_width = 800
mw_height = 600

mainWindow = pygame.display.set_mode((mw_width, mw_height),RESIZABLE)
mainWindow.fill((22,22,152))

pygame.display.set_caption('Incredible Machine!')

current_level = Level(1)

level = current_level.create_level()
level = pygame.transform.scale(level, (650,600))

mainWindow.blit(level,[0,0])

pygame.draw.line(mainWindow, (150,0,0), [650, 600], [650, 0], 5)

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(mainWindow,(255,0,0),(40,40,50,50))

    pygame.display.update()


pygame.quit()