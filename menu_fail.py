# imports
import pygame
from messenger import Messenger
from settings import *
from menu import Menu

# initialize pygame
pygame.init()

class MenuFail(Menu):
    """
    Fail Menu class
    """
    def __init__(self, win):
        """
        initializes the class
        receives the window to blit
        """
        Menu.__init__(self, ['RESTART', 'QUIT'], FONT_LA_CASA, win)

    def draw(self):
        """
        method to draw the background text and info
        """
        self.win.fill(RED)
        title1 = self.messenger.text_format("GAME", self.font, 58, BLACK)
        title2 = self.messenger.text_format("OVER", self.font, 58, BLACK)
        title3 = self.messenger.text_format("Prof. Marcelo has caught you!", self.font, 38, BLACK)

        prof = pygame.Rect(190, 140, 0, 20)
        prof_image = pygame.image.load('images/others/prof.png').convert_alpha()
        prof_streched_image = pygame.transform.scale(prof_image, (130,132))

        title_rect1 = title1.get_rect()
        title_rect2 = title2.get_rect()

        self.win.blit(prof_streched_image, prof)
        self.win.blit(title1, (WIDTH / 2.5  - (title_rect1[2] / 2), 90))
        self.win.blit(title2, (WIDTH / 1.6 - (title_rect2[2] / 2), 90))
        self.win.blit(title3, (80, 40))
        
        self.draw_menu(BLACK, GREY)
