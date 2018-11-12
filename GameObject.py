import pygame


class GameObject(pygame.sprite.Sprite):

    def __init__(self,type,pos_x,pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type = type


    def __repr__(self):
        return "type: " + self.type + ", pos_x: {}, pos_y: {}".format(self.pos_x, self.pos_y)


    def make_surface(self):
        pass

    def collide(self,pos):
        pass




