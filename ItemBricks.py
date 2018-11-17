from GameObject import *
import pygame
from Constants import IMAGE_BRICKS_PATH, ITEM_BRICKS_WIDTH, ITEM_BRICKS_HEIGHT

class ItemBricks(GameObject):


    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.width = ITEM_BRICKS_WIDTH
        self.height = ITEM_BRICKS_HEIGHT
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_BRICKS_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.speedx = 1
        self.speedy = 0
        self.was_moved = False


    def move(self):
        pass


    def update(self):
        self.rect.top += self.speedy

        if self.rect.top < 0 or self.rect.bottom > 600:
            return
        if self.rect.left < 0 or self.rect.right > 800:
            return

    def collide(self,spriteGroup):
        if pygame.sprite.spritecollide(self,spriteGroup,False):
            pass
