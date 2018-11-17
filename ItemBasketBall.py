from GameObject import *
from Constants import *
import pygame

class ItemBasketBall(GameObject):

    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.width = ITEM_BASKETBALL_WIDTH
        self.height = ITEM_BASKETBALL_HEIGHT
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_BASKETBALL_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.speedx = 0
        self.speedy = 0.5
        self.was_moved = False

    def move(self):
        self.pos_x += self.speedx
        self.pos_y += self.speedy
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        if self.rect.bottom >= 500:
            return False
        else:
            return True

    def update(self):
        self.pos_y += self.speedy
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        if self.rect.top < 0 or self.rect.bottom > 600:
            return
        if self.rect.left < 0 or self.rect.right > 800:
            return

    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            collided_object = pygame.sprite.spritecollide(self, spriteGroup, False)
            return collided_object


    def react_to_collision(self, gameObject):

        if gameObject.type == "BRICKS":
            self.pos_y = gameObject.pos_y-ITEM_BRICKS_HEIGHT-ITEM_BASKETBALL_HEIGHT/2
            if abs(self.pos_x-gameObject.pos_x) > abs(self.pos_x-(gameObject.pos_x+ITEM_BRICKS_WIDTH)):
                self.pos_x += 2
            else:
                self.pos_x -= 2
            self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))


        if gameObject.type == "BAR":

            if gameObject.already_reacted:
                if gameObject.right:
                    self.pos_x += -2
                    self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
                if gameObject.left:
                    self.pos_x += 1
                    self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
            else:
                self.pos_y = gameObject.pos_y - ITEM_BAR_HEIGHT - ITEM_BASKETBALL_HEIGHT/2
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
                return True

        if gameObject.type == "BASKET":
            if (self.pos_y > (gameObject.pos_y)-5 or self.pos_y < (gameObject.pos_y)+5) and (self.pos_x > gameObject.pos_x-5 or self.pos_x < gameObject.pos_x+5):
                return True

