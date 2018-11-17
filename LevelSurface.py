import pygame
from Constants import *
import pandas as pd
from ItemBall import *
from ItemBar import *
from ItemBasket import *
from ItemBasketBall import *
from ItemBalloon import *
from ItemBricks import *

from Button import *

pygame.init()

button_size_x = 160
button_size_y = 40
button_play_pos_x = 20
button_play_pos_y = 520
button_restart_pos_x = 200
button_restart_pos_y = 520
button_next_pos_x = 430
button_next_pos_y = 520

class LevelSurface():

    def __init__(self,number):
        self.number = number
        self.levels = pd.read_csv(LEVELS_CSV_PATH, delimiter=",")
        self.button_play = Button(BUTTON_CHECK,20,200,50,button_size_x,button_size_y)
        self.button_restart = Button(BUTTON_RETRY,40,80,200,button_size_x,button_size_y)
        self.button_next = Button(BUTTON_NEXT, 128, 128, 128, button_size_x, button_size_y)
        self.still_objects_group = pygame.sprite.Group()
        self.movable_objects_group = pygame.sprite.Group()
        self.all_objects_group = pygame.sprite.Group()
        self.level_surface = pygame.Surface([800, 600], pygame.SRCALPHA, 32)
        self.level_beginning_surface = pygame.Surface([800, 600], pygame.SRCALPHA, 32)
        self.level_restart_surface = pygame.Surface([800, 600], pygame.SRCALPHA, 32)
        self.level_empty_surface = pygame.Surface([800, 600], pygame.SRCALPHA, 32)
        self.passed = False


    def create_level(self):

        print("-----create level -------")

        self.level_beginning_surface.fill((170, 170, 240))

        (still_beginning_objects, moving_beginning_objects) = self.load_objects()

        still_objects_surface = pygame.image.load(LEVEL_SURFACE_PATH).convert()
        still_objects_surface = pygame.transform.scale(still_objects_surface, (650, 500))
        still_objects_surface = still_objects_surface.convert_alpha()

        movable_objects_surface = pygame.Surface([200, 600], pygame.SRCALPHA, 32)
        movable_objects_surface = movable_objects_surface.convert_alpha()

        self.level_beginning_surface.blit(still_objects_surface,[0,0])
        self.level_beginning_surface.blit(movable_objects_surface, [650, 0])

        pygame.draw.line(self.level_beginning_surface, (150, 0, 0), [650, 600], [650, 0], 5)
        pygame.draw.line(self.level_beginning_surface, (150, 0, 0), [0, 500], [650, 500], 5)

        button_play_surface = self.button_play.create_surface()
        button_restart_surface = self.button_restart.create_surface()
        button_next_surface = self.button_next.create_surface()

        self.level_beginning_surface.blit(button_play_surface, [button_play_pos_x, button_play_pos_y])
        self.level_beginning_surface.blit(button_restart_surface, [button_restart_pos_x, button_restart_pos_y])
        self.level_beginning_surface.blit(button_next_surface, [button_next_pos_x, button_next_pos_y])

        self.level_empty_surface = self.level_beginning_surface.copy()

        still_beginning_objects.draw(self.level_beginning_surface)

        self.level_surface = self.level_beginning_surface.copy()

        self.level_restart_surface = self.level_beginning_surface.copy()
        moving_beginning_objects.draw(self.level_restart_surface)

        self.still_objects_group = still_beginning_objects
        self.movable_objects_group = moving_beginning_objects

        self.still_objects_group.draw(self.level_surface)
        self.movable_objects_group.draw(self.level_surface)

        print("----- created level finished -------")

        return self.level_surface


    def load_objects(self):

        print("-----load objects -------")

        current_lvl_objects = self.levels[self.levels.lvl_number==self.number]

        still_objects_group = pygame.sprite.Group()
        movable_objects_group = pygame.sprite.Group()

        still_objects_list = []
        movable_objects_list = []

        for i in range(len(current_lvl_objects)):
            if current_lvl_objects.at[i,'movable']==0:
                still_objects_list.append(
                    GameObject(self.levels.at[i,'item'],self.levels.at[i,'pos_x'],self.levels.at[i,'pos_y']))
            else:
                movable_objects_list.append(
                    GameObject(self.levels.at[i, 'item'], self.levels.at[i, 'pos_x'], self.levels.at[i, 'pos_y']))


        for i in range(len(still_objects_list)):

            temp_object = GameObject(still_objects_list[i].type,still_objects_list[i].pos_x,still_objects_list[i].pos_y)

            if still_objects_list[i].type=="BALL":
                object = ItemBall(temp_object)

            elif still_objects_list[i].type=="BASKETBALL":
                object = ItemBasketBall(temp_object)

            elif still_objects_list[i].type == "BAR":
                object = ItemBar(temp_object)

            elif still_objects_list[i].type == "BALLOON":
                object = ItemBar(temp_object)

            elif still_objects_list[i].type == "BRICKS":
                object = ItemBar(temp_object)

            elif still_objects_list[i].type == "BASKET":
                object = ItemBasket(temp_object)

            still_objects_group.add(object)
            self.all_objects_group.add(object)

        for i in range(len(movable_objects_list)):

            temp_object = GameObject(movable_objects_list[i].type,movable_objects_list[i].pos_x,movable_objects_list[i].pos_y)

            if movable_objects_list[i].type=="BALL":
                object = ItemBall(temp_object)

            elif movable_objects_list[i].type=="BASKETBALL":
                object = ItemBasketBall(temp_object)

            elif movable_objects_list[i].type == "BAR":
                object = ItemBar(temp_object)

            elif movable_objects_list[i].type == "BALLOON":
                object = ItemBalloon(temp_object)

            elif movable_objects_list[i].type == "BRICKS":
                object = ItemBricks(temp_object)


            movable_objects_group.add(object)
            self.all_objects_group.add(object)

        return (still_objects_group,movable_objects_group)


    def check_mouse_pos(self,mouse):
        if button_play_pos_x + button_size_x > mouse[0] > button_play_pos_x and button_play_pos_y + button_size_y > mouse[1] > button_play_pos_y:
            self.button_play.interact(self.button_play.title)

        if button_restart_pos_x + button_size_x > mouse[0] > button_restart_pos_x and button_restart_pos_y + button_size_y > mouse[1] > button_restart_pos_y:
            self.button_restart.interact(self.button_restart.title)


    def mouse_clicked(self,mouse):
        if button_play_pos_x + button_size_x > mouse[0] > button_play_pos_x and button_play_pos_y + button_size_y > mouse[1] > button_play_pos_y:
            #self.button_play.press(self.button_play.title,self)
            return 1

        if button_restart_pos_x + button_size_x > mouse[0] > button_restart_pos_x and button_restart_pos_y + button_size_y > mouse[1] > button_restart_pos_y:
            #self.button_restart.press(self.button_restart.title,self)
            return 2


    def drag_objects(self,item_id,mouse):

        for item in self.movable_objects_group:
            if(id(item) == item_id):

                item.pos_x = mouse[0]-(item.rect.width/2)
                item.pos_y = mouse[1]-(item.rect.height/2)
                item.move_with_mouse()

        self.movable_objects_group.clear(self.level_surface,self.level_beginning_surface)
        self.movable_objects_group.draw(self.level_surface)


    def move_everything(self):

        still_checking = True

        for item in self.all_objects_group:
            self.all_objects_group.remove(item)

            if item.collide(self.all_objects_group):
                collided_object = item.collide(self.all_objects_group)
                item.react_to_collision(collided_object[0])

            item.move()
            if item.type == "BASKETBALL":
                still_checking = item.move()

            self.all_objects_group.add(item)

        return still_checking


    def restart(self):
        self.still_objects_group.empty()
        self.movable_objects_group.empty()
        self.level_surface = self.level_beginning_surface.copy()
        (self.still_objects_group,self.movable_objects_group) = self.load_objects()


