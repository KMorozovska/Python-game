import pygame
import random

class GameObject(pygame.sprite.Sprite):

    def __init__(self,type,pos_x,pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type = type
        self.depth = random.randint(1, 11)
        self.was_moved = False


    def __repr__(self):
        return "type: " + self.type + ", pos_x: {}, pos_y: {}".format(self.pos_x, self.pos_y)


    def make_surface(self):
        pass

    def check_mouse_collision(self,pos):
        if self.pos_x + self.width > pos[0] > self.pos_x and self.pos_y + self.height > pos[1] > self.pos_y:
            return True

    def move_with_mouse(self):
        if self.pos_x > self.width/4 and self.pos_x < 800 and self.pos_y > self.height/4 and self.pos_y < 600-self.height/4:
            self.rect.topleft = [self.pos_x,self.pos_y]
        else:
            return

    def check_position(self):
        if self.rect.top < 0 or self.rect.bottom > 500 or self.rect.left < 0 or self.rect.right > 650:
            self.was_moved = False
        else:
            self.was_moved = True
