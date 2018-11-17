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
passed = False
failed = False

welcome = StartSurface()
welcome_surf = welcome.create_surface()
mainWindow.blit(welcome_surf,[0,0])

lvl_number=1
current_level = LevelSurface(lvl_number)

while run:

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
                    current_level.movable_objects_group.clear(mainWindow, current_level.level_empty_surface)
                    current_level.still_objects_group.clear(mainWindow, current_level.level_empty_surface)
                    current_level.all_objects_group.clear(mainWindow, current_level.level_empty_surface)
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
                print(len(current_level.movable_objects_group))
                for item in current_level.movable_objects_group:
                    if item.check_mouse_collision(event.pos):
                        mouse_held = True
                        break

        if mouse_held:
            current_level.drag_objects(id(item),event.pos)
            mainWindow.blit(current_level.level_surface,[0,0])

    if checking_level:
        (checking_level, passed, failed) = current_level.move_everything()
        current_level.movable_objects_group.clear(mainWindow, current_level.level_empty_surface)
        current_level.still_objects_group.clear(mainWindow, current_level.level_empty_surface)
        current_level.all_objects_group.clear(mainWindow, current_level.level_empty_surface)
        current_level.all_objects_group.draw(mainWindow)

    if passed:
        Tk().wm_withdraw()
        messagebox.showinfo('Wow!', 'Congratulations, you did it!')
        lvl_number += 1
        passed = False
        checking_level = False
        del current_level
        started = True
        current_level = LevelSurface(lvl_number)
        new_level_surface = current_level.create_level()
        mainWindow.fill((170, 170, 240))
        mainWindow.blit(new_level_surface, [0, 0])

    if failed:
        Tk().wm_withdraw()
        messagebox.showinfo('Oops', 'Level failed - try again!')
        current_level.movable_objects_group.clear(mainWindow, current_level.level_empty_surface)
        current_level.still_objects_group.clear(mainWindow, current_level.level_empty_surface)
        current_level.all_objects_group.clear(mainWindow, current_level.level_empty_surface)
        current_level.restart()
        mainWindow.blit(current_level.level_empty_surface, [0, 0])
        failed = False
        checking_level = False

    pygame.display.update()

pygame.quit()