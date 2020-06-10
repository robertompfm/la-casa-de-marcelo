# imports
import pygame
from messenger import *

# initialize pygame
pygame.init()

# HouseObjects class
class HouseObject():
    """
    class for the house objects presents in the game
    """
    def __init__(self, name, coord, message, win):
        """
        initializes the object, it recieves the object's name, x and y origin position, width and height

        the house objects have a small_rect and big_rect, which are used for checking collisions with the player
        """
        self.name = name
        x, y, width, height = coord
        self.small_rect = pygame.Rect(x, y, width, height)
        self.big_rect = pygame.Rect(x - 6, y - 6, width + 12, height + 12)
        self.message = message
        self.win = win
        self.messenger = Messenger(win)
        self.active = False


    def check_collision(self, player_rect):
        """
        used to prevent the player from passing through the house object
        this function recieves the player's rectangle
        it returns true if there is a collision between the player's rectangle and the house object's small_rect
        """
        return self.small_rect.colliderect(player_rect)


    def check_interaction(self, player_rect):
        """
        used to check if the player is near enough to interact with the  house object
        this function recieves the player's rectangle
        it returns true if there is a collision between the player's rectangle and the house object's big_rect
        """
        return self.big_rect.colliderect(player_rect)


    def draw_message(self):
        """
        reveals the message the object has
        """
        if self.active:
            self.messenger.draw_bottom_message(self.message)


    def key_handler(self, event):
        """
        handles key event
        """
        if not self.active:
            if event.key == pygame.K_SPACE:
                self.active = True
        else:
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                self.active = False


    def is_active(self):
        """
        returns true if the object is showing a message
        """
        return self.active

    