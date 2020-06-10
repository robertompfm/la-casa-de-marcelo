# imports
import pygame
from player import Player
from house_object import HouseObject
from computer import Computer
from messenger import Messenger
from timer import Timer
from settings import *
from menu_start import MenuStart
from menu_fail import MenuFail
from menu_intro import MenuIntro
from menu_success import MenuSuccess

# initialize pygame
pygame.init()

# global constants


class GameHandler:
    """
    class that will manage the game, it will handle the events and objects interactions
    """
    def __init__(self):
        """
        initialize the game handler class
        """
        pygame.display.set_caption(TITLE)
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player(200, 300, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_IMAGES_PATH, FPS, self.win)
        self.timer = Timer(TIME, FPS, self.win)
        

        self.start_menu = MenuStart(self.win)
        self.intro_menu = MenuIntro(self.win)
        self.failure_menu = MenuFail(self.win)
        self.success_menu = MenuSuccess(self.win)

        house_objects = [HouseObject(key, val[0], val[1], self.win) for key, val in OBJ_INFO.items()]
        computer_objects = [Computer(key, val[0], val[1], self.win, val[2]) for key, val in COMP_INFO.items()]
        self.all_objects = house_objects + computer_objects

        self.run = True
        self.showing_message = False

        self.stage = 0
        pygame.mixer.music.load('sound/loop.wav')


    def quit_game(self):
        pygame.quit()
        quit()


    def quit_handler(self, event):
        if event.type == pygame.QUIT:
            self.run = False
            self.quit_game()


    def start_handler(self, event):
        self.start_menu.key_handler(event)


    def intro_handler(self, event):
        self.intro_menu.key_handler(event)


    def failure_handler(self, event):
        self.failure_menu.key_handler(event)


    def success_handler(self, event):
        self.success_menu.key_handler(event)
        

    def action_handler(self, event):
        # interactions
        interaction, obj = self.player.can_interact(self.all_objects)
        if interaction and event.type == pygame.KEYUP:
            obj.key_handler(event)
            self.showing_message = obj.is_active()
        # player actions
        if not self.showing_message:
            self.player.key_handler(event)
    

    def key_handler(self, event):
        self.quit_handler(event)
        if self.stage == 0:
            self.start_handler(event)
        elif self.stage == 1:
            self.intro_handler(event)
        elif self.stage == 2:
            self.action_handler(event)
        elif self.stage == 3:
            self.failure_handler(event)
        else:
            self.quit_game()


    def game_loop(self):
        while self.run:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.key_handler(event)

            self.update()    
            
    ## MAKE AN UPDATE METHOD
    def update(self):
        if self.stage == 0:
            self.start_menu.draw()
            if self.start_menu.is_done():
                if self.start_menu.get_selection() == 0:
                    self.stage += 1
                else:
                    self.stage = -1
                self.start_menu.set_done(False)

        elif self.stage == 1:
            self.intro_menu.draw()
            if self.intro_menu.is_done():
                self.stage += 1
                self.intro_menu.set_done(False)
                pygame.mixer.music.play(-1)

        elif self.stage == 2:
            self.win.blit(BACKGROUND, (0, 0))
            self.player.move(self.all_objects)
            self.timer.run()
            for obj in self.all_objects:
                obj.draw_message()
            # check loss
            if self.timer.get_time() <= 0:
                self.stage += 1
                self.timer.reset()
                self.player.reset()
                pygame.mixer.music.stop()
            # check victory
            computer = self.all_objects[-1]
            if computer.was_invaded():
                self.stage += 2 # CHANGE THIS!!!
                computer.lock()
                pygame.mixer.music.stop()
            
        elif self.stage == 3:
            self.failure_menu.draw()
            if self.failure_menu.is_done():
                if self.failure_menu.get_selection() == 0:
                    self.stage -= 1
                    pygame.mixer.music.play(-1)
                else:
                    self.quit_game()         
                self.failure_menu.set_done(False)
        
        elif self.stage == 4:
            self.success_menu.draw()
            if self.failure_menu.is_done():
                if self.success_menu.is_done():
                    self.stage += 1
                    self.success_menu.set_done(False)


        pygame.display.update()