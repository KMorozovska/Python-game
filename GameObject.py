import pygame
import random

class GameObject(pygame.sprite.Sprite):

    def __init__(self,type,pos_x,pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type = type
        self.depth = random.randint(1, 11)


    def __repr__(self):
        return "type: " + self.type + ", pos_x: {}, pos_y: {}".format(self.pos_x, self.pos_y)


    def make_surface(self):
        pass

    def collide(self,pos):
        pass

    def update(self):
        self.mouse_coordinates = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.mouse_coordinates) == True:
            self.rect.centerx = self.mouse_coordinates[0]
            self.rect.centery = self.mouse_coordinates[1]
