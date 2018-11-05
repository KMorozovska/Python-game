import pygame
from Constants import *
import pandas as pd
from GameObject import *

class Level():

    def __init__(self,number):
        self.number = number
        self.levels = pd.read_csv(LEVELS_CSV_PATH, delimiter=",")

    def create_level(self):

        surface = pygame.image.load(LEVEL_SURFACE_PATH).convert()

        (still_objects_surface, movable_objects_surface) = self.load_objects()

        surface.blit(still_objects_surface,[0,0])
        surface.blit(movable_objects_surface, [0, 0])

        return surface

    def load_objects(self):

        still_objects_surface = pygame.Surface([640, 480], pygame.SRCALPHA, 32)
        still_objects_surface = still_objects_surface.convert_alpha()

        movable_objects_surface = pygame.Surface([640, 480], pygame.SRCALPHA, 32)
        movable_objects_surface = still_objects_surface.convert_alpha()

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

        print(still_objects_list)
        print(movable_objects_list)

        return (still_objects_surface,movable_objects_surface)