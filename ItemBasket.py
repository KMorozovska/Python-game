from GameObject import *
import pygame
from Constants import *

class ItemBasket(GameObject):


    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.width = ITEM_BASKET_WIDTH
        self.height = ITEM_BASKET_HEIGHT
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_BASKET_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))


    def collide(self,spriteGroup):
        if pygame.sprite.spritecollide(self,spriteGroup,False):
            collided_object = pygame.sprite.spritecollide(self,spriteGroup,False)
            return collided_object

    def update(self):
        pass


    def move(self):
        pass

    def react_to_collision(self,gameObject):
        if gameObject.type == "BASKETBALL":
            pass

