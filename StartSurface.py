from Constants import *
from Button import *

from tkinter import Tk
from tkinter import messagebox

pygame.init()

button_size_x = 160
button_size_y = 80
button_play_pos_x = 130
button_play_pos_y = 350
button_info_pos_x = 340
button_info_pos_y = 350
title_pos_x = 20
title_pos_y = 20

class StartSurface():

    def __init__(self):
        self.button_play = Button(BUTTON_PLAY,230,120,140,button_size_x,button_size_y)
        self.button_info = Button(BUTTON_INFO,230,120,240,2*button_size_x, button_size_y)

    def create_surface(self):
        surface = pygame.Surface([800, 600], pygame.SRCALPHA, 32)

        image = pygame.image.load(TITLE_PATH).convert()
        image_surface = pygame.transform.scale(image, (750, 300))
        button_play_surf = self.button_play.create_surface()
        button_info_surf = self.button_info.create_surface()

        surface.blit(button_play_surf,[button_play_pos_x,button_play_pos_y])
        surface.blit(button_info_surf, [button_info_pos_x, button_info_pos_y])
        surface.blit(image_surface, [title_pos_x, title_pos_y])

        return surface


    def button_clicked(self,mouse):
        if button_play_pos_x + button_size_x > mouse[0] > button_play_pos_x and button_play_pos_y + button_size_y > mouse[1] > button_play_pos_y:
            return True
        if button_info_pos_x + button_size_x > mouse[0] > button_info_pos_x and button_info_pos_y + button_size_y > mouse[1] > button_info_pos_y:
            Tk().wm_withdraw()
            messagebox.showinfo('Instructions', 'Make the basketball fall into the basket, using given objects!')