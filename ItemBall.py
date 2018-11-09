from GameObject import *
from Constants import IMAGE_BALL_PATH
import pygame

class ItemBall(GameObject):

    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        print("Hello Ball")

    def make_image(self):
        image = pygame.image.load(IMAGE_BALL_PATH)
        image = pygame.transform.scale(image, (45, 45))
        return image
