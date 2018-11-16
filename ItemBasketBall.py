from GameObject import *
from Constants import IMAGE_BASKETBALL_PATH
import pygame

class ItemBasketBall(GameObject):

    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.width = 45
        self.height = 45
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_BASKETBALL_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.speedx = 0
        self.speedy = 1
        self.was_moved = False

    def move(self):
        print("ruszam sie - ball")
        self.pos_x += self.speedx
        self.pos_y += self.speedy
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        print("-------------")
        print(id(self))
        print(self.pos_y)

        if self.rect.bottom >= 500:
            print("koniec ruszania")
            return False
        else:
            return True

    def update(self):
        self.pos_y += self.speedy
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        print(self.rect.top, self.rect.top, self.rect.left,self.rect.right)

        if self.rect.top < 0 or self.rect.bottom > 600:
            return
        if self.rect.left < 0 or self.rect.right > 800:
            return


    def collide(self,spriteGroup):
        if pygame.sprite.spritecollide(self,spriteGroup,False):
            print("byla kolizja")




