from GameObject import *
import pygame
from Constants import IMAGE_BALLOON_PATH, ITEM_BALLOON_WIDTH, ITEM_BALLOON_HEIGHT, ITEM_BAR_WIDTH, ITEM_BRICKS_HEIGHT

class ItemBalloon(GameObject):


    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.width = ITEM_BALLOON_WIDTH
        self.height = ITEM_BALLOON_HEIGHT
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_BALLOON_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.speedx = 0
        self.speedy = 1
        self.was_moved = False


    def move(self):
        if self.pos_y <= 0:
            return

        self.pos_x += self.speedx
        self.pos_y -= self.speedy
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))


    def update(self):
        self.rect.top += self.speedy

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
            self.pos_y = gameObject.pos_y-ITEM_BRICKS_HEIGHT
            self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

        if gameObject.type == "BAR":
            if self.pos_x == gameObject.pos_x - ITEM_BAR_WIDTH / 2:
                self.pos_y = gameObject.pos_y
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
            if self.pos_x > gameObject.pos_x - ITEM_BAR_WIDTH / 2:
                gameObject.react_to_collision(self)
                self.pos_y = gameObject.pos_y
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
            if self.pos_x < gameObject.pos_x - ITEM_BAR_WIDTH / 2:
                gameObject.react_to_collision(self)
                self.pos_y = gameObject.pos_y
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

