# imports
import pygame
from messenger import *
from settings import *

# initialize pygame
pygame.init()


class Menu():
    """
    class to create and handle the start and game over screens
    """
    def __init__(self, options, font, win):
        """
        initialize the class
        it recieves a main message, the menu options, the type of menu and the window to blit
        """
        self.options = options
        self.font = font
        self.win = win
        self.selected = 0
        self.done = False
        self.messenger = Messenger(win)


    def key_handler(self, event):
        """
        key handler for selecting options
        """
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.selected += 1
            elif event.key == pygame.K_DOWN:
                self.selected -= 1
            elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                self.done = True

        self.selected %= len(self.options)


    def is_done(self):
        """
        returns true if the return key was pressed
        """
        return self.done


    def set_done(self, done):
        """
        setter for done attribute
        """
        self.done = done


    def set_selected(self, selected):
        """
        setter for selected attribute
        """
        self.selected = selected


    def get_selection(self):
        """
        returns which option was selected
        """
        return self.selected

    
    def draw_menu(self, color_one, color_two):
        """
        method to draw the menu window
        """
        width, height = self.win.get_size()
        y = 3 * height // 4
        for option in self.options:
            color = color_one
            font_size = 30
            if self.options[self.selected] == option:
                color = color_two
                font_size = 36
            option_msg = self.messenger.text_format(option, self.font, font_size, color)
            option_rect = option_msg.get_rect()
            x = (width // 2 - option_rect.width // 2)
            self.win.blit(option_msg, (x, y))
            y += 40

        


