import pygame

from game import Game
from input_handlers import handle_keys
from window import init_screen

FPS = 60


def main():
    pygame.init()

    screen = init_screen()
    game = Game()

    running = True
    clock = pygame.time.Clock()
    while running:
        keys = pygame.key.get_pressed()
        action = handle_keys(keys)

        quit = action.get("quit")

        if quit:
            running = False

        game.update(action)
        game.render(screen)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
