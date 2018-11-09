from GameObject import *
import pygame
from Constants import IMAGE_BAR_PATH

class ItemBar(GameObject):


    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        print("Hello Bar")


    def make_image(self):
        image = pygame.image.load(IMAGE_BAR_PATH)
        image = pygame.transform.scale(image,(150,20))
        return image