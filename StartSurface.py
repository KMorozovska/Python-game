from Constants import *
from Button import *

pygame.init()

button_size_x = 450
button_size_y = 100
button_pos_x = 400
button_pos_y = 300

class StartSurface():

    def __init__(self):
        self.button_play = Button(BUTTON_PLAY,20,200,50,button_size_x,button_size_y)

    def create_surface(self):
        surface = pygame.Surface([800, 600], pygame.SRCALPHA, 32)

        button_play_surf = self.button_play.create_surface()

        surface.blit(button_play_surf,[button_pos_x,button_pos_y])

        return surface


    def button_clicked(self,mouse):
        if button_pos_x + button_size_x > mouse[0] > button_pos_x and button_pos_y + button_size_y > mouse[1] > button_pos_y:
            return True
