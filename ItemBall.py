from GameObject import *
from Constants import IMAGE_BALL_PATH
import pygame

class ItemBall(GameObject):

    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.width = 45
        self.height = 45
        self.type = gameObject.type
        self.pos_x = gameObject.pos_x
        self.pos_y = gameObject.pos_y
        self.depth = gameObject.depth
        self.image = pygame.transform.scale((pygame.image.load(IMAGE_BALL_PATH).convert_alpha()),(self.width,self.height))
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

    def make_image(self):
        image = pygame.image.load(IMAGE_BALL_PATH)
        image = pygame.transform.scale(image, (self.width, self.height))
        return image

    def collide(self,pos):
        if self.pos_x + self.width > pos[0] > self.pos_x and self.pos_y + self.height > pos[1] > self.pos_y:
            print("była kolizja!")
            return True


    def update(self):
        print(self.pos_x, self.pos_y)
        self.rect.topleft = [self.pos_x,self.pos_y]
        print(self.rect)
