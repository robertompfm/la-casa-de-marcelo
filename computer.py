# imports
import pygame
from house_object import *
from messenger import *

# initialize pygame
pygame.init()

# Computer class
class Computer(HouseObject):
    """
    computer is a child of HouseObject class
    it will recieve a new argument called password
    it has two new boolean parameters: typing will be turned True while the user is typing; and unlocked will become True if the user inputs a correct answer
    it has two string parameters, input_txt and password, they will be compared to determine if the computer was unlocked
    """
    def __init__(self, name, coord, message, win, password):
        super().__init__(name, coord, message, win)
        self.typing = False
        self.unlocked = False
        self.password = password
        self.input_txt = ""


    def draw_message(self):
        """
        reveals the message the object has
        """
        if self.active:
            self.messenger.draw_computer_window(self.message, self.input_txt, self.typing, self.unlocked)


    def key_handler(self, event):
        """
        handles key event
        """
        if not self.active:
            if event.key == pygame.K_SPACE:
                self.active = True
                self.typing = True
        
        elif self.typing:
            key_name = pygame.key.name(event.key)
            if len(key_name) == 1:
                self.input_txt += key_name.upper()
            elif key_name == 'backspace':
                self.input_txt = self.input_txt[:-1]
            elif event.key == pygame.K_RETURN:
                self.typing = False
                self.unlocked = (self.input_txt == self.password)
                self.input_txt = ""
        
        else:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                self.active = False


    def was_invaded(self):
        """
        tells if the computer was invaded or not
        """
        return self.unlocked and not self.active


    def lock(self):
        """
        lock the computer again
        """
        self.unlocked = False