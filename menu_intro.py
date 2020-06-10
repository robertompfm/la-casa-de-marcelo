# imports
import pygame
from messenger import Messenger
from settings import *
from menu import Menu

# initialize pygame
pygame.init()

class MenuIntro(Menu):
    """
    Start Menu class
    """
    def __init__(self, win):
        """
        initializes the class
        receives the window to blit
        """
        Menu.__init__(self, None, FONT_ADV, win)


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
        self.win.fill(BLACK)
        text_intro = """Professor Marcelo gave you another bad grade.\nBut not all is lost!\nYou have just invaded his house and now have the chance to change your grade in the Professor's PC.\nBut to have access you will need to answer an enigma.\nBe quick, the Professor is coming from the theater in 5 minutes!\nUse the arrow keys to move. Press SPACE to interact with the house objects. They may contain hints.\nNow, press any key to start!"""
        
        self.messenger.draw_multiline_text(text_intro, self.font, 30, WHITE, (20, 0))