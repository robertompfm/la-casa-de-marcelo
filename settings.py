# imports
import pygame

# initialize pygame
pygame.init()

TITLE = "La Casa de Marcelo"

BLACK = (0, 0, 0)
GREY = (235, 235, 235)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 520
HEIGHT = 376

PLAYER_WIDTH = 36
PLAYER_HEIGHT = 65
PLAYER_SPEED = 5

TIME = 60 * 5

PASSWORD = '14'

BACKGROUND = pygame.image.load('images/background/background.png')

PLAYER_IMAGES_PATH = 'images/player'

FONT_ADV = 'fonts/advanced_pixel.ttf'
FONT_LA_CASA = 'fonts/lacasa.otf'
TEXT_FONT = pygame.font.Font('fonts/advanced_pixel.ttf', 24)

FPS = 27

OBJ_INFO = {
    'bed': [
        [10, 240, 62, 55],
        'Wow, he sleeps!!\n '
    ],
    'robot': [
        [43, 38, 36, 35],
        'BB-8: Hello stranger, the solution is really simple! \nAll you have to do is multiply 111 by 10.'
    ],
    'shelf': [
        [379, 13, 61, 67],
        'A Big Bang Theory collection... \nand an old book called \'Binary Code\''
    ],
    'video game': [
        [448, 51, 49, 74],
        'I prefer Mario...\n '
    ],
    'periodic table': [
        [149, 20, 69, 8],
        'Who has a periodic table in its room? \nMaybe this is a clue'
    ]
}

COMP_INFO = {
    'computer': [
        [276, 41, 89, 38],
        'Riddle me this:\nArrah, Arrah, and gather \'round,\nthis hero is legion-bound\nHe multiplies N by the number of He,\nand in this room the thing you\'ll see.',
        PASSWORD
    ]
}
