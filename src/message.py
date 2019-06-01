import pygame

from window import WINDOW_WIDTH

FONT = "Square"
FONT_SIZE = 30
SCORE_X = WINDOW_WIDTH / 4
SCORE_Y = 10
LIVES_Y = 10
LIVES_X = SCORE_X * 3


def get_rendered_text(used_font, size, color, message):
    font_object = pygame.font.Font(used_font, size)
    return font_object.render(message, True, color)


def search_font(name):
    return pygame.font.match_font(name)
