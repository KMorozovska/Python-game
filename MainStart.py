import pygame
from Constants import LEVEL_SURFACE_PATH
import pygame, os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

mw_width = 800
mw_height = 600

lvl_width = 0
lvl_height = 0

mainWindow = pygame.display.set_mode((mw_width, mw_height))

pygame.display.set_caption('Incredible Machine!')

level = pygame.image.load(LEVEL_SURFACE_PATH)

mainWindow.blit(level,[0,0])

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(mainWindow,(255,0,0),(40,40,50,50))
    pygame.display.update()


pygame.quit()