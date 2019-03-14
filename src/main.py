import pygame

from entity import Entity

TITLE = "Breakout"

BLACK = (0, 0, 0)
RED = (200, 72, 72)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20
PLAYER_X = WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2
PLAYER_Y = 550
PLAYER_VELOCITY = 10


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)

    running = True
    clock = pygame.time.Clock()

    vel = PLAYER_VELOCITY

    player = Entity(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, RED)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= vel
        if keys[pygame.K_RIGHT]:
            player.x += vel

        screen.fill(BLACK)
        player.render(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
