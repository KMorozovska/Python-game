from GameObject import *
from Constants import IMAGE_BASKETBALL_PATH, ITEM_BAR_WIDTH, ITEM_BASKETBALL_HEIGHT, ITEM_BASKETBALL_WIDTH, ITEM_BRICKS_HEIGHT, ITEM_BRICKS_WIDTH
import pygame

class ItemBasketBall(GameObject):

    def __init__(self,gameObject):
        super(GameObject, self).__init__()
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.width = ITEM_BASKETBALL_WIDTH
        self.height = ITEM_BASKETBALL_HEIGHT
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

        if self.rect.top < 0 or self.rect.bottom > 600:
            return
        if self.rect.left < 0 or self.rect.right > 800:
            return

    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            collided_object = pygame.sprite.spritecollide(self, spriteGroup, False)
            print("byla kolizja pilki do kosza")
            print(collided_object)
            return collided_object


    def react_to_collision(self, gameObject):

        if gameObject.type == "BRICKS":

            self.pos_y = gameObject.pos_y-ITEM_BRICKS_HEIGHT
            self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))

            if self.pos_y == gameObject.pos_y-ITEM_BRICKS_HEIGHT and self.pos_x == gameObject.pos_x+ITEM_BRICKS_WIDTH/2:
                self.pos_x = gameObject.pos_x+ITEM_BRICKS_WIDTH/2
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
            return True


        if gameObject.type == "BAR":
            if self.pos_x == gameObject.pos_x - ITEM_BAR_WIDTH/2:
                pass
            elif self.pos_x > gameObject.pos_x - ITEM_BAR_WIDTH/2:
                self.pos_x += 1
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
            elif self.pos_x < gameObject.pos_x - ITEM_BAR_WIDTH/2:
                self.pos_x -= 1
                self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
            return False

        if gameObject.type == "BASKET":
            print("Congratulations you won !!!! ")
            return True
