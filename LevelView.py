import pygame
from Constants import LEVEL_SURFACE_PATH

class LevelView:

    def __init__(self):
        surface = pygame.image.load(LEVEL_SURFACE_PATH).convert()
        pygame.display.update()
        return surface




