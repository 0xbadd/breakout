import pygame

from ball import Ball
from block import init_blocks
from colors import BLACK
from player import Player
from wall import init_walls


class Game:
    def __init__(self):
        self.player = Player()
        self.ball = Ball()
        self.walls = init_walls()
        self.blocks = init_blocks()

    def update(self, action):
        move = action.get("move")
        launch = action.get("launch")

        self.player.update(move, self.walls)
        self.ball.update(launch, self.player, self.blocks, self.walls)

    def render(self, screen):
        screen.fill(BLACK)
        self.player.render(screen)
        self.ball.render(screen)
        for block in self.blocks:
            block.render(screen)
        for wall in self.walls:
            wall.render(screen)
        pygame.display.flip()
