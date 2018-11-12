from pygame.locals import *
import pygame, os
from LevelSurface import *

from StartSurface import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

mw_width = 800
mw_height = 600

mainWindow = pygame.display.set_mode((mw_width, mw_height),RESIZABLE)
mainWindow.fill((158,128,128))

pygame.display.set_caption('Incredible Machine!')

run = True
started = False

welcome = StartSurface()
welcome_surf = welcome.create_surface()
mainWindow.blit(welcome_surf,[0,0])

i=1

while run:
    pygame.time.delay(5)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()

            if welcome.button_clicked(pos):
                current_level = LevelSurface(i)
                level_surface = current_level.create_level()
                mainWindow.fill((158, 128, 128))
                mainWindow.blit(level_surface, [0, 0])
                started = True

            if started:
                current_level.mouse_clicked(pos)

        #elif event.type == pygame.MOUSEBUTTONDOWN:

            #if event.button == 1:
                #[dragging, dragged_object] = current_level.drag_objects(event.pos)

                #if dragging:
                    #mouse_x, mouse_y = event.pos
                    #offset_x = dragged_object.pos_x - mouse_x
                    #offset_y = dragged_object.pos_y - mouse_y


        #elif event.type == pygame.MOUSEMOTION:

            #if dragging:
                #mouse_x, mouse_y = event.pos
                #move_object(dragged_object,mouse_x,mouse_y,offset_x,offset_y)
                #rectangle.x = mouse_x + offset_x
                #rectangle.y = mouse_y + offset_y


        pygame.display.update()

pygame.quit()