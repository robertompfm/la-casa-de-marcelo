# imports
import pygame
from settings import *

# initialize pygame
pygame.init()

# Player class
class Player():
    """
    Player class that will create the character for the game
    """
    
    moving = {
        'right': False, 
        'left': False, 
        'down': False, 
        'up': False
        }

    vel = PLAYER_SPEED
    walk_count = 0


    def __init__(self, x, y, width, height, path, fps, win):
        """
        initializing the player images and dimensions
        receives x and y initial position, player's 
        width and height, the path for the player images
        and a value of how many frames per seconds the
        display will be updated
        """
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = pygame.Rect(x, y, width, height) # used to move and check for collisions
        self.walk_right = [
            pygame.image.load(path + '/R1.png'),
            pygame.image.load(path + '/R2.png'),
            pygame.image.load(path + '/R3.png')
            ]
        self.walk_left = [
            pygame.image.load(path + '/L1.png'),
            pygame.image.load(path + '/L2.png'),
            pygame.image.load(path + '/L3.png')
            ]
        self.walk_front = [
            pygame.image.load(path + '/F1.png'),
            pygame.image.load(path + '/F2.png'),
            pygame.image.load(path + '/F3.png')
            ]
        self.walk_back = [
            pygame.image.load(path + '/B1.png'),
            pygame.image.load(path + '/B2.png'),
            pygame.image.load(path + '/B3.png')
            ]
        self.position = self.walk_back
        self.fps = fps
        self.win = win
    

    def draw(self):
        """
        method that will draw the player image on the window
        """
        if self.moving['right']:
            self.win.blit(self.walk_right[self.walk_count // (self.fps // 3)], (self.rect.left, self.rect.top))
        
        elif self.moving['left']:
            self.win.blit(self.walk_left[self.walk_count // (self.fps // 3)], (self.rect.left, self.rect.top))

        elif self.moving['down']:
            self.win.blit(self.walk_front[self.walk_count // (self.fps // 3)], (self.rect.left, self.rect.top))

        elif self.moving['up']:
            self.win.blit(self.walk_back[self.walk_count // (self.fps // 3)], (self.rect.left, self.rect.top))

        else:
            self.win.blit(self.position[1], (self.rect.left, self.rect.top))
            return 
        
        self.walk_count += 1
        self.walk_count %= self.fps


    def key_handler(self, event):
        """
        method to handle key events
        """
        # for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.moving['right'] = True
            elif event.key == pygame.K_LEFT:
                self.moving['left'] = True
            elif event.key == pygame.K_DOWN:
                self.moving['down'] = True
            elif event.key == pygame.K_UP:
                self.moving['up'] = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.moving['right'] = False
                self.position = self.walk_right
            elif event.key == pygame.K_LEFT:
                self.moving['left'] = False
                self.position = self.walk_left
            elif event.key == pygame.K_DOWN:
                self.moving['down'] = False
                self.position = self.walk_front
            elif event.key == pygame.K_UP:
                self.moving['up'] = False
                self.position = self.walk_back
    

    def update_pos(self):
        """
        update player position
        """
        if self.moving['right']:
            self.rect.left += self.vel

        elif self.moving['left']:
            self.rect.left -= self.vel

        elif self.moving['down']:
            self.rect.top += self.vel

        elif self.moving['up']:
            self.rect.top -= self.vel
    

    def get_rect(self):
        """
        method that returns the player's rectangle
        """
        return self.rect


    def can_move(self, house_objects):
        """
        check if the player is colliding with the edges of the screen or with house objects
        returns true if the player can move
        """
        # check collision with the right edge
        if (self.moving['right']) and ((self.rect.right + self.vel) > self.win.get_size()[0]):
            return False
        # check collision with the left edge
        if (self.moving['left']) and (self.rect.left - self.vel) < 0:
            return False
        # check collision with the bottom edge
        if (self.moving['down']) and ((self.rect.bottom + self.vel) > self.win.get_size()[1]):
            return False
        # check collision with the top edge (a little lower to consider the wall)
        if (self.moving['up']) and (self.rect.top - self.vel) < 20:
            return False

        # check collision with the house objects
        for house_obj in house_objects:
            if house_obj.check_collision(self.rect):
                return False
        return True


    def can_interact(self, house_objects):
        """
        check if the player can interact with an object from a list of objects
        it returns a tuple of a boolean, which will tell if the player can interact, and a house object itself
        """
        for house_object in house_objects:
            if house_object.check_interaction(self.rect):
                return (True, house_object)
        return (False, None)


    def move(self, house_objects):
        """
        makes the player update its position and move
        """
        curr_pos = self.rect.left, self.rect.top
        self.update_pos()
        if not self.can_move(house_objects):
            self.rect.left, self.rect.top = curr_pos
        self.draw()

    
    def reset(self):
        """
        reset player position to its initial position
        """
        for key in self.moving:
            self.moving[key] = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.position = self.walk_back
        self.walk_count = 0
