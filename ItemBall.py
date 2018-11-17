from GameObject import *
from Constants import ITEM_BALL_HEIGHT, ITEM_BALL_WIDTH, IMAGE_BALL_PATH,ITEM_BAR_WIDTH, ITEM_BRICKS_HEIGHT
import pygame

class ItemBall(GameObject):

    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.width = ITEM_BALL_WIDTH
        self.height = ITEM_BALL_HEIGHT
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_BALL_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.speedx = 0
        self.speedy = 1
        self.was_moved = False

    def move(self):
        print("ruszam sie - ball")

        if self.pos_y >= 500 - ITEM_BALL_HEIGHT:
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
            print("byla kolizja pilki z czyms")
            print(collided_object)
            return collided_object


    def react_to_collision(self,gameObject):

        if gameObject.type == "BRICKS":
            self.pos_y = gameObject.pos_y-ITEM_BRICKS_HEIGHT
            self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        if gameObject.type == "BAR":
            if self.pos_x == gameObject.pos_x - ITEM_BAR_WIDTH/2:
                pass
            elif self.pos_x > gameObject.pos_x - ITEM_BAR_WIDTH/2:
                self.pos_x += 1
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
            elif self.pos_x < gameObject.pos_x - ITEM_BAR_WIDTH/2:
                self.pos_x -= 1
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))







