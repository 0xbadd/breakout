import pygame

from colors import RED
from entity import Entity
from velocity import Velocity
from window import WINDOW_WIDTH

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20
PLAYER_X = WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2
PLAYER_Y = 550
PLAYER_VELOCITY = 10


class Player(Entity):
    def __init__(self):
        self.x = PLAYER_X
        self.y = PLAYER_Y
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.color = RED
        self.velocity = Velocity()

    def render(self, screen):
        pygame.draw.rect(
            screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height)
        )

    def move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    def update(self, walls):
        self.move()
        self.handle_collisions(walls)

    def handle_collisions(self, walls):
        left_wall = walls[0]
        right_wall = walls[1]

        if self.x < left_wall.width:
            self.x = left_wall.width
        if self.x + self.width > right_wall.x:
            self.x = right_wall.x - self.width
