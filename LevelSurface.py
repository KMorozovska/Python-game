import pygame
from Constants import *
import pandas as pd
from ItemBall import *
from ItemBar import *
from Button import *

pygame.init()

class LevelSurface():

    def __init__(self,number):
        self.number = number
        self.levels = pd.read_csv(LEVELS_CSV_PATH, delimiter=",")

    def create_level(self,running):

        surface = pygame.Surface([800, 600], pygame.SRCALPHA, 32)

        (still_objects_surface, movable_objects_surface) = self.load_objects()

        surface.blit(still_objects_surface,[0,0])
        surface.blit(movable_objects_surface, [650, 0])

        pygame.draw.line(surface, (150, 0, 0), [650, 600], [650, 0], 5)
        pygame.draw.line(surface, (150, 0, 0), [0, 500], [650, 500], 5)

        button_play = Button("Play",20,200,50,100,40)
        button_play = button_play.create_button()

        button_restart = Button("Restart", 40, 80, 200, 100, 40)
        button_restart = button_restart.create_button()

        surface.blit(button_play, [200, 520])
        surface.blit(button_restart, [350, 520])

        while running:
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONUP:
                    mouse = pygame.mouse.get_pos()
                    if 200 + 100 > mouse[0] > 200 and 520 + 40 > mouse[1] > 520:
                        button_play.interact()

                    if 200 + 100 > mouse[0] > 200 and 520 + 40 > mouse[1] > 520:
                        button_restart.interact()

        return surface


    def load_objects(self):

        still_objects_surface = pygame.image.load(LEVEL_SURFACE_PATH).convert()
        still_objects_surface = pygame.transform.scale(still_objects_surface,(650,500))
        still_objects_surface = still_objects_surface.convert_alpha()

        movable_objects_surface = pygame.Surface([200, 600], pygame.SRCALPHA, 32)
        movable_objects_surface = movable_objects_surface.convert_alpha()

        current_lvl_objects = self.levels[self.levels.lvl_number==self.number]

        still_objects_list = []
        movable_objects_list = []

        for i in range(len(current_lvl_objects)):
            if current_lvl_objects.at[i,'movable']==0:
                still_objects_list.append(
                    GameObject(self.levels.at[i,'item'],self.levels.at[i,'pos_x'],self.levels.at[i,'pos_y']))
            else:
                movable_objects_list.append(
                    GameObject(self.levels.at[i, 'item'], self.levels.at[i, 'pos_x'], self.levels.at[i, 'pos_y']))


        for i in range(len(still_objects_list)):

            temp_object = GameObject(still_objects_list[i].type,still_objects_list[i].pos_x,still_objects_list[i].pos_y)

            if(still_objects_list[i].type=="BALL"):
                object = ItemBall(temp_object)

            elif(still_objects_list[i].type == "BAR"):
                object = ItemBar(temp_object)

            still_objects_surface.blit(object.make_image(),[object.pos_x, object.pos_y])


        for i in range(len(movable_objects_list)):

            temp_object = GameObject(movable_objects_list[i].type,movable_objects_list[i].pos_x,movable_objects_list[i].pos_y)

            if(movable_objects_list[i].type=="BALL"):
                object = ItemBall(temp_object)

            elif(movable_objects_list[i].type == "BAR"):
                object = ItemBar(temp_object)

            movable_objects_surface.blit(object.make_image(),[object.pos_x, object.pos_y])

        return (still_objects_surface,movable_objects_surface)



