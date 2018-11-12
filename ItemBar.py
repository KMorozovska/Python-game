from GameObject import *
import pygame
from Constants import IMAGE_BAR_PATH

class ItemBar(GameObject):


    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.width = 150
        self.height = 20


    def make_image(self):
        image = pygame.image.load(IMAGE_BAR_PATH)
        image = pygame.transform.scale(image,(self.width,self.height))
        return image

    def collide(self,pos):
        if self.pos_x + self.width > pos[0] > self.pos_x and self.pos_y + self.height > pos[1] > self.pos_y:
            return True