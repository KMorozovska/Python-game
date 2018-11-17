from GameObject import *
import pygame
from Constants import *

class ItemBar(GameObject):


    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.width = ITEM_BAR_WIDTH
        self.height = ITEM_BAR_HEIGHT
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_BAR_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.speedx = 1
        self.speedy = 0
        self.was_moved = False
        self.already_reacted = False


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


    def react_to_collision(self,gameObject):

        if gameObject.type == "BALLOON" and not self.already_reacted:
            if gameObject.pos_x > self.pos_x - ITEM_BAR_WIDTH/2:
                self.image = pygame.transform.scale((pygame.image.load(IMAGE_BAR_LEFT_PATH).convert_alpha()),(self.width+10, self.height+10))
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
                self.already_reacted = True
            if gameObject.pos_x < self.pos_x - ITEM_BAR_WIDTH/2:
                self.image = pygame.transform.scale((pygame.image.load(IMAGE_BAR_RIGHT_PATH).convert_alpha()),(self.width+10, self.height+10))
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
                self.already_reacted = True

        if gameObject.type == "BALL" and not self.already_reacted:
            if gameObject.pos_x > self.pos_x - ITEM_BAR_WIDTH/2:
                self.image = pygame.transform.scale((pygame.image.load(IMAGE_BAR_RIGHT_PATH).convert_alpha()),(self.width+10, self.height+10))
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
                self.already_reacted = True
            if gameObject.pos_x < self.pos_x - ITEM_BAR_WIDTH/2:
                self.image = pygame.transform.scale((pygame.image.load(IMAGE_BAR_LEFT_PATH).convert_alpha()),(self.width+10, self.height+10))
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
                self.already_reacted = True
