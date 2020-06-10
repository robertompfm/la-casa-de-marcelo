# imports
import pygame
from messenger import Messenger
from settings import *
from menu import Menu

# initialize pygame
pygame.init()

class MenuSuccess(Menu):
    """
    Start Menu class
    """
    def __init__(self, win):
        """
        initializes the class
        receives the window to blit
        """
        Menu.__init__(self, None, FONT_LA_CASA, win)


    def key_handler(self, event):
        """
        key handler for selecting options
        """
        if event.type == pygame.KEYUP:    
            self.done = True


    def draw(self):
        """
        method to draw the screen
        """
        self.win.fill(WHITE)
        title_win1 = self.messenger.text_format("Grade changed successfully.", self.font, 32, BLACK)
        title_win2 = self.messenger.text_format("Student APPROVED!", self.font, 32, BLACK)
        title_win3 = self.messenger.text_format("The job market awaits you!", self.font, 32, BLACK)

        diplo = pygame.Rect(220, 90, 0, 20)
        diplo_image = pygame.image.load('images/others/diploma.png').convert_alpha()
        diplo_streched_image = pygame.transform.scale(diplo_image, (70, 70))

        boss = pygame.Rect(190, 212, 0, 20)
        boss_image = pygame.image.load('images/others/ronald.png').convert_alpha()
        boss_streched_image = pygame.transform.scale(boss_image, (150, 150))

        self.win.blit(diplo_streched_image, diplo)
        self.win.blit(boss_streched_image, boss)
        self.win.blit(title_win1, (120, 20))
        self.win.blit(title_win2, (185, 55))
        self.win.blit(title_win3, (125, 185))


