from pygame.locals import *
import pygame, os
from LevelSurface import *
from tkinter import *
from tkinter import messagebox
from StartSurface import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

mw_width = 800
mw_height = 600

mainWindow = pygame.display.set_mode([mw_width, mw_height])
mainWindow.fill((170, 170, 240))

pygame.display.set_caption('Incredible Machine!')

run = True
started = False
mouse_held = False
checking_level = False

welcome = StartSurface()
welcome_surf = welcome.create_surface()
mainWindow.blit(welcome_surf,[0,0])

i=1
current_level = LevelSurface(i)

while run:
    #pygame.time.delay(5)

    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONUP:

            mouse_held = False
            pos = pygame.mouse.get_pos()

            if not started and welcome.button_clicked(pos):
                level_surface = current_level.create_level()
                mainWindow.fill((170, 170, 240))
                mainWindow.blit(level_surface, [0, 0])
                started = True

            if started:
                which_button = current_level.mouse_clicked(pos)
                if which_button == 2:
                    current_level.restart()
                    mainWindow.blit(current_level.level_restart_surface, [0, 0])

                if which_button == 1:
                    for i in current_level.movable_objects_group:
                        i.check_position()
                    if all(item.was_moved for item in current_level.movable_objects_group):
                        checking_level = True
                    else:
                        Tk().wm_withdraw()
                        messagebox.showinfo('Oops', 'Please place all of the given items in the level area')

        if event.type == pygame.MOUSEBUTTONDOWN:

            if started:
                for item in current_level.movable_objects_group:
                    if item.check_mouse_collision(event.pos):
                        mouse_held = True
                        break

        if mouse_held:
            current_level.drag_objects(id(item),event.pos)
            mainWindow.blit(current_level.level_surface,[0,0])

    if checking_level:
        checking_level = current_level.move_everything()
        current_level.movable_objects_group.clear(mainWindow, current_level.level_empty_surface)
        current_level.still_objects_group.clear(mainWindow, current_level.level_empty_surface)
        current_level.all_objects_group.clear(mainWindow, current_level.level_empty_surface)
        current_level.all_objects_group.draw(mainWindow)

    pygame.display.update()

pygame.quit()