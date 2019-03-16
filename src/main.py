import pygame

from ball import BALL_VELOCITY_X, BALL_VELOCITY_Y, Ball
from block import init_blocks
from game import render_game
from input_handlers import handle_keys
from player import Player
from wall import init_walls
from window import init_screen

FPS = 60


def main():
    pygame.init()

    screen = init_screen()

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

        player.update(move, walls)
        ball.update(launch, player, blocks, walls)

        render_game(screen, player, ball, blocks, walls)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
