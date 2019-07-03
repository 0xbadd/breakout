import pygame

from game import Game
from input_handlers import handle_keys
from window import init_screen
from game_states import GameStates

FPS = 60


def main():
    pygame.init()

    screen = init_screen()
    game = Game()

    running = True
    game_state = GameStates.MAIN_MENU
    clock = pygame.time.Clock()
    while running:
        keys = pygame.key.get_pressed()
        action = handle_keys(keys)

        if game_state == GameStates.MAIN_MENU:
            new_game = action.get("new_game")
            quit = action.get("quit")

            if new_game:
                game_state = GameStates.PLAYING

            if quit:
                running = False
        elif game_state == GameStates.PLAYING:
            quit = action.get("quit")

            if quit:
                running = False

            results = game.update(action)

            lost = results.get("lost")

            if lost:
                game = Game()

        game.render(screen, game_state)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
