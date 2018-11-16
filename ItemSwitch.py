from GameObject import *
import pygame
from Constants import IMAGE_SWITCH_PATH

class ItemSwitch(GameObject):


    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.width = 70
        self.height = 70
        self.type = gameObject.type
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_SWITCH_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = gameObject.pos_x
        self.rect.y = gameObject.pos_y



    def collide(self,pos):
        if self.pos_x + self.width > pos[0] > self.pos_x and self.pos_y + self.height > pos[1] > self.pos_y:
            print("Była kolizja!!!")
            return True

    def update(self):
        print(self.pos_x, self.pos_y)
        self.rect.topleft = [self.pos_x,self.pos_y]
        print(self.rect)