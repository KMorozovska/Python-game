from GameObject import *
from Constants import *
import pygame

class ItemWeight(GameObject):

    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.width = ITEM_WEIGHT_WIDTH
        self.height = ITEM_WEIGHT_HEIGHT
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_WEIGHT_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.speedx = 0
        self.speedy = 2
        self.was_moved = False

    def move(self):
        if self.pos_y >= 500 - ITEM_WEIGHT_HEIGHT:
            return

        self.pos_x += self.speedx
        self.pos_y += self.speedy
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))


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
            collided_object = pygame.sprite.spritecollide(self,spriteGroup,False)
            return collided_object


    def react_to_collision(self,gameObject):

        if gameObject.type == "BRICKS":
            self.pos_y = gameObject.pos_y-ITEM_BRICKS_HEIGHT-ITEM_WEIGHT_HEIGHT/2
            self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        if gameObject.type == "BAR":
            if self.pos_x > gameObject.pos_x and self.pos_x < gameObject.pos_x + ITEM_BAR_WIDTH / 2:
                gameObject.react_to_collision(self)
                self.pos_y = gameObject.pos_y - ITEM_WEIGHT_HEIGHT
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
            if self.pos_x > gameObject.pos_x/2 and self.pos_x < gameObject.pos_x + ITEM_BAR_WIDTH:
                gameObject.react_to_collision(self)
                self.pos_y = gameObject.pos_y - ITEM_WEIGHT_HEIGHT
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

