import pygame
from Constants import *
import pandas as pd
import numpy as np

class Level():

    def __init__(self,number):
        self.number = number
        self.levels = pd.read_csv(LEVELS_CSV_PATH, delimiter=",")

    def create_level(self):

        surface = pygame.image.load(LEVEL_SURFACE_PATH).convert()

        still_objects_surface = self.load_objects()

        surface.blit(still_objects_surface,[0,0])

        return surface

    def load_objects(self):

        still_objects_surface = pygame.Surface([640, 480], pygame.SRCALPHA, 32)
        still_objects_surface = still_objects_surface.convert_alpha()

        count_objects = len(self.levels[self.levels.lvl_number==self.number])

        for i in range(count_objects):
            print(self.levels.at[i,'item'])

        return still_objects_surface