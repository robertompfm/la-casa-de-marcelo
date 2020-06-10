# imports
import pygame
from settings import *

# initialize pygame
pygame.init()

class Messenger:
    """
    class created to handle all text messages and interaction windows
    """
    def __init__(self, win):
        """
        initialize the Messenger class
        """
        self.win = win
        self.win_width, self.win_height = win.get_size()


    def text_format(self, message, font_src, size, color):
        """
        method used to format a text
        it receives the message as string, the font path, the desired text and color
        it returns the formatted text
        """
        new_font = pygame.font.Font(font_src, size)
        new_text = new_font.render(message, 0, color)
        
        return new_text


    def draw_multiline_text(self, message, font_src, size, color, pos):
        """
        method to draw a text on the screen, breaking the lines automatically
        """
        words = [word.split(' ') for word in message.splitlines()] # 2D array where each row is a list of words
        font = pygame.font.Font(font_src, size)
        space = font.size(' ')[0] # the width of a space
        max_width, max_height = self.win_width - 10, self.win_height - 10
        word_height = 0
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0] # reset x
                    y += word_height # start new row
                self.win.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0] # reset x
            y += word_height


    def draw_multiline_centered_text(self, message, font_src, size, color, pos):
        """
        method to draw a text on the screen, breaking the lines automatically with the text centered
        """
        lines = message.splitlines() # array or lines
        font = pygame.font.Font(font_src, size)
        max_width, max_height = self.win_width, self.win_height
        x, y = pos
        for line in lines:
            line_surface = font.render(line, 0, color)
            line_width, line_height = line_surface.get_size()
            x = (max_width // 2) - (line_width // 2)
            self.win.blit(line_surface, (x, y))
            y += line_surface.get_size()[1]


    def draw_input_text(self, input_txt):
        """
        method to draw the input text on the screen
        it should be used when the player is typing on the computer
        """
        label = self.text_format("Answer: ", FONT_ADV, 30, BLACK)
        label_pos = ((self.win_width // 2 - label.get_rect().width), (self.win_height // 2 + 70))
        self.win.blit(label, label_pos)

        input = self.text_format(input_txt, FONT_ADV, 30, BLACK)
        input_pos = ((self.win_width // 2), (self.win_height // 2 + 70))
        self.win.blit(input, input_pos)


    def draw_feedback_message(self, unlocked):
        """
        method to draw a message telling if the player entered the correct or the wrong password
        """
        feedback_dict = {True: 'CORRECT!', False: 'WRONG!'}
        feedback = self.text_format(feedback_dict[unlocked], FONT_ADV, 36, BLACK)
        feedback_pos = ((self.win_width // 2 - feedback.get_rect().width // 2), (self.win_height // 2 + 70))
        self.win.blit(feedback, feedback_pos)


    def draw_bottom_message(self, message):
        """
        draws a message box at the bottom of the screen
        """
        outer_rect_coord = [
            0,
            int(self.win_height * .8),
            self.win_width,
            self.win_height - int(self.win_height * .8)
        ]
        
        inner_rect_coord = [
            outer_rect_coord[0] + 5,
            outer_rect_coord[1] + 5,
            outer_rect_coord[2] - 10,
            outer_rect_coord[3] - 10
        ]

        pygame.draw.rect(self.win, GREY, outer_rect_coord)
        pygame.draw.rect(self.win, BLACK, inner_rect_coord, 2)
        self.draw_multiline_text(message, FONT_ADV, 24, BLACK, (15, outer_rect_coord[1] + 10))


    def draw_computer_window(self, message, input_txt, typing, unlocked):
        """
        draws a message box at the center of the screen
        """
        outer_rect_coord = [
            self.win_width // 10,
            self.win_height // 10,
            self.win_width - 2 * (self.win_width // 10),
            self.win_height - 2 * (self.win_height // 10)
        ]

        inner_rect_coord = [
            outer_rect_coord[0] + 5,
            outer_rect_coord[1] + 5,
            outer_rect_coord[2] - 10,
            outer_rect_coord[3] - 10
        ]
        # draws rectangle
        pygame.draw.rect(self.win, GREY, outer_rect_coord)
        pygame.draw.rect(self.win, BLACK, inner_rect_coord, 2)
        # draws riddle
        self.draw_multiline_centered_text(message, FONT_ADV, 30, BLACK, (0, inner_rect_coord[1] + 20))
        # draws input or feedback
        if typing:
            self.draw_input_text(input_txt)
        else:
            self.draw_feedback_message(unlocked)


