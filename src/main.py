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
        action = handle_keys(keys, game_state)

        quit = action.get("quit")

        if quit:
            running = False

        if game_state == GameStates.MAIN_MENU or game_state == GameStates.GAME_OVER:
            new_game = action.get("new_game")

            if new_game:
                if game_state == GameStates.GAME_OVER:
                    game = Game()
                game_state = GameStates.PLAYING
        elif game_state == GameStates.PLAYING:
            results = game.update(action)

            lost = results.get("lost")

            if lost:
                game_state = GameStates.GAME_OVER

        game.render(screen, game_state)

        clock.tick(FPS)


if __name__ == "__main__":
    main()
