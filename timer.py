# imports
import pygame

# initialize pygame
pygame.init()

# constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

TIMER_FONT = pygame.font.Font("fonts/advanced_pixel.ttf", 34)
REL_POS = [75, 10]

# Timer class
class Timer():
    """
    class for the timer that appears at the top-right corner of the screen
    """

    def __init__(self, start_time, fps, win):
        """
        initialize the timer
        receives the starting time, the frames per seconds and the window of the game
        """
        self.start_time = start_time
        self.remaining_time = start_time
        self.framme_count = 0
        self.fps = fps
        self.win = win
        self.pause = False
        win_size = win.get_size()
        self.pos = [win_size[0] - REL_POS[0], REL_POS[1]]


    def pause(self):
        """
        pauses the timer
        """
        self.pause = True


    def resume(self):
        """
        resumes the timer
        """
        self.pause = False


    def reset(self):
        """
        reset the timer
        """
        self.remaining_time = self.start_time
        self.framme_count = 0


    def get_time(self):
        """
        returns the time remaining
        """
        return self.remaining_time


    def run(self):
        """
        makes the timer run if it is not paused
        """
        if not self.pause:
            self.remaining_time = self.start_time - (self.framme_count // self.fps)

            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60

            self.draw(minutes, seconds)

            self.framme_count += 1
            

    def draw(self, minutes, seconds):
        """
        method to draw the timer clock at the top-rigth corner of the screen
        """
        timer_str = "{0:02}:{1:02}".format(minutes, seconds)
        timer_text = TIMER_FONT.render(timer_str, True, BLACK)
        self.win.blit(timer_text, self.pos)
