import math
import random

import pygame

from entity import Entity
from game import (
    handle_ball_collisions,
    handle_player_collisions,
    init_blocks,
    init_walls,
    render_game,
)
from velocity import Velocity

TITLE = "Breakout"

RED = (200, 72, 72)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20
PLAYER_X = WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2
PLAYER_Y = 550
PLAYER_VELOCITY = 10

BALL_SIZE = 20
BALL_X = WINDOW_WIDTH / 2 - BALL_SIZE / 2
BALL_Y = PLAYER_Y - BALL_SIZE
BALL_VELOCITY_X = 5
BALL_VELOCITY_Y = -10
BALL_SPEED_MODIFIER = 5

FPS = 60


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)

    player = Entity(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, RED)
    ball = Entity(BALL_X, BALL_Y, BALL_SIZE, BALL_SIZE, RED, Velocity())
    walls = init_walls()
    blocks = init_blocks()

    entities = []
    entities.append(player)
    entities.append(ball)
    entities.extend(walls)
    entities.extend(blocks)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.move(-PLAYER_VELOCITY, 0)
        if keys[pygame.K_RIGHT]:
            player.move(PLAYER_VELOCITY, 0)
        if keys[pygame.K_SPACE] and ball.velocity.x == 0 and ball.velocity.y == 0:
            if keys[pygame.K_LEFT]:
                ball.velocity.x = -BALL_VELOCITY_X
                ball.velocity.y = BALL_VELOCITY_Y
            if keys[pygame.K_RIGHT]:
                ball.velocity.x = BALL_VELOCITY_X
                ball.velocity.y = BALL_VELOCITY_Y
            else:
                ball.velocity.x = BALL_VELOCITY_X * math.pow(-1, random.randint(1, 3))
                ball.velocity.y = BALL_VELOCITY_Y

        if ball.velocity.x == 0 and ball.velocity.y == 0:
            ball.x = player.x + player.width / 2 - ball.width / 2
            ball.y = player.y - player.height
        else:
            ball.move(ball.velocity.x, ball.velocity.y)

        handle_player_collisions(player, walls)
        handle_ball_collisions(ball, player, walls)

        render_game(screen, entities)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
