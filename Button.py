import pygame


class Button():

    def __init__(self,title,color_r,color_g,color_b,width,height):
        self.title = title
        self.color_r = color_r
        self.color_g = color_g
        self.color_b =  color_b
        self.width = width
        self.height = height


    def create_button(self):

        border = 2
        myfont = pygame.font.SysFont("monospace", 15)

        surface = pygame.Surface([self.width+2*border,self.height+2*border], pygame.SRCALPHA, 32)

        pygame.draw.rect(surface,(0,0,0),pygame.Rect(0,0,self.width+border,self.height+border))
        pygame.draw.rect(surface,(self.color_r, self.color_g, self.color_b),pygame.Rect(border,border,self.width-border,self.height-border))

        label = myfont.render(self.title, 1, (255, 255, 0))
        surface.blit(label,[(self.width+2*border)/4,(self.height+2*border)/4])

        return surface


    def interact(self,type):

        if(type=="PLAY"):
            print("Hey")
        elif(type=="RESTART"):
            print("Restart")
