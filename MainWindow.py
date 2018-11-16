from pygame.locals import *
import pygame, os
from LevelSurface import *
from operator import attrgetter
from StartSurface import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

mw_width = 800
mw_height = 600

mainWindow = pygame.display.set_mode((mw_width, mw_height),RESIZABLE)
mainWindow.fill((170, 170, 240))

pygame.display.set_caption('Incredible Machine!')

run = True
started = False
mouse_held = False

welcome = StartSurface()
welcome_surf = welcome.create_surface()
mainWindow.blit(welcome_surf,[0,0])

i=1
current_level = LevelSurface(i)

while run:
    pygame.time.delay(5)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONUP:

            mouse_held = False
            pos = pygame.mouse.get_pos()

            if welcome.button_clicked(pos):
                level_surface = current_level.create_level()
                mainWindow.fill((170, 170, 240))
                mainWindow.blit(level_surface, [0, 0])
                started = True

            if started:
                which_button = current_level.mouse_clicked(pos)
                if which_button == 2:
                    mainWindow.blit(current_level.create_level(), [0, 0])
                    pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:

            if started:

                for item in current_level.movable_objects_group:
                    if item.collide(event.pos) == True:
                        temp = current_level.drag_objects(id(item),event.pos)
                        temp.draw(mainWindow)
                        mouse_held = True
                        break

        if mouse_held:
            print("still dragging!")
            temp = current_level.drag_objects(id(item),event.pos)
            temp.draw(mainWindow)
            #temp.empty()
            #temp.clear(mainWindow, mainWindow)
            #temp.update()

        pygame.display.update()

pygame.quit()