import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TITLE = "Breakout"


def init_screen():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)
    return screen
