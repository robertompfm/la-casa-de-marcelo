# imports
import pygame
from messenger import Messenger
from settings import *
from menu import Menu

# initialize pygame
pygame.init()

class MenuStart(Menu):
    """
    Start Menu class
    """
    def __init__(self, win):
        """
        initializes the class
        receives the window to blit
        """
        Menu.__init__(self, ['START', 'QUIT'], FONT_LA_CASA, win)

    def draw(self):
        """
        method to draw the background text and info
        """
        self.win.fill(BLACK)
        title1 = self.messenger.text_format("La casa", self.font, 58, WHITE)
        title2 = self.messenger.text_format("de", self.font, 48, WHITE)
        title3 = self.messenger.text_format("Marcelo", self.font, 58, WHITE)

        title_rect1 = title1.get_rect()
        title_rect2 = title2.get_rect()
        title_rect3 = title3.get_rect()

        self.win.blit(title1, (WIDTH / 3.4 - (title_rect1[2] / 2), 90))
        pygame.draw.rect(self.win, RED, (238, 92, 45, 45))
        self.win.blit(title2, (WIDTH / 2 - (title_rect2[2] / 2), 95))
        self.win.blit(title3, (WIDTH / 1.4  - (title_rect3[2] / 2), 90))
        self.draw_menu(WHITE, WHITE)
