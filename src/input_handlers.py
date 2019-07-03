import pygame

from player import PLAYER_VELOCITY
from game_states import GameStates


def handle_keys(keys, game_state):
    if game_state == GameStates.MAIN_MENU or game_state == GameStates.GAME_OVER:
        return handle_menu()
    if game_state == GameStates.PLAYING:
        return handle_player_keys(keys)

    return {}


def handle_player_keys(keys):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return {"quit": True}
        elif event.type == pygame.QUIT:
            return {"quit": True}

    if keys[pygame.K_SPACE]:
        return {"launch": True}

    if keys[pygame.K_LEFT]:
        return {"move": -PLAYER_VELOCITY}
    elif keys[pygame.K_RIGHT]:
        return {"move": PLAYER_VELOCITY}
    else:
        return {"move": 0}

    return {}


def handle_menu():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                return {"new_game": True}
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_2:
                return {"quit": True}
        elif event.type == pygame.QUIT:
            return {"quit": True}

    return {}
