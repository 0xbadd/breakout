import math
import random

import pygame

from entity import Entity, is_collision
from game import handle_ball_collisions, handle_player_collisions, init_blocks
from velocity import Velocity

TITLE = "Breakout"

BLACK = (0, 0, 0)
GREY = (142, 142, 142)
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

WALL_SIZE = 40

FPS = 60


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)

    player = Entity(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, RED)

    ball = Entity(BALL_X, BALL_Y, BALL_SIZE, BALL_SIZE, RED, Velocity())

    walls = []
    left_wall = Entity(0, 50, WALL_SIZE, WINDOW_HEIGHT - 80, GREY)
    right_wall = Entity(
        WINDOW_WIDTH - WALL_SIZE, 50, WALL_SIZE, WINDOW_HEIGHT - 80, GREY
    )
    top_wall = Entity(0, 50, WINDOW_WIDTH, WALL_SIZE, GREY)
    walls.append(left_wall)
    walls.append(right_wall)
    walls.append(top_wall)

    blocks = init_blocks()

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

        screen.fill(BLACK)
        player.render(screen)
        ball.render(screen)
        for block in blocks:
            block.render(screen)
        for wall in walls:
            wall.render(screen)
        pygame.display.flip()

        clock.tick(FPS)


if __name__ == "__main__":
    main()
