import math
import random

import pygame

from ball import BALL_VELOCITY_X, BALL_VELOCITY_Y, Ball
from block import init_blocks
from game import render_game
from input_handlers import handle_keys
from player import Player
from wall import init_walls
from window import WINDOW_HEIGHT, WINDOW_WIDTH

TITLE = "Breakout"
FPS = 60


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)

    player = Player()
    ball = Ball()
    walls = init_walls()
    blocks = init_blocks()

    running = True
    clock = pygame.time.Clock()
    while running:
        keys = pygame.key.get_pressed()
        action = handle_keys(keys)

        move = action.get("move")
        launch = action.get("launch")
        quit = action.get("quit")

        if quit:
            running = False

        if move:
            player.velocity.x = move
        else:
            player.velocity.x = 0

        if launch and not ball.velocity.is_moving():
            if keys[pygame.K_LEFT]:
                ball.velocity.x = -BALL_VELOCITY_X
                ball.velocity.y = BALL_VELOCITY_Y
            if keys[pygame.K_RIGHT]:
                ball.velocity.x = BALL_VELOCITY_X
                ball.velocity.y = BALL_VELOCITY_Y
            else:
                ball.velocity.x = BALL_VELOCITY_X * math.pow(-1, random.randint(1, 3))
                ball.velocity.y = BALL_VELOCITY_Y

        player.update(walls)
        ball.update(player, blocks, walls)

        render_game(screen, player, ball, blocks, walls)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
