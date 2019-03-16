import pygame

from colors import BLACK


def render_game(screen, player, ball, blocks, walls):
    screen.fill(BLACK)
    player.render(screen)
    ball.render(screen)
    for block in blocks:
        block.render(screen)
    for wall in walls:
        wall.render(screen)
    pygame.display.flip()
