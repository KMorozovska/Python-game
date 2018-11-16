from GameObject import *
import pygame
from Constants import IMAGE_BALLOON_PATH

class ItemBalloon(GameObject):


    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.width = 50
        self.height = 120
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_BALLOON_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.speedx = 1
        self.speedy = 0
        self.was_moved = False


    def move(self):
        print("ruszam sie - balloon")


    def update(self):
        self.rect.top += self.speedy

        if self.rect.top < 0 or self.rect.bottom > 600:
            return
        if self.rect.left < 0 or self.rect.right > 800:
            return

    def collide(self,spriteGroup):
        if pygame.sprite.spritecollide(self,spriteGroup,False):
            print("byla kolizja")
