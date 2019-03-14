import pygame

PLAYER_VELOCITY = 10


def handle_keys(keys):
    return handle_player_keys(keys)


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
