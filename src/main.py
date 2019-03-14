import pygame

TITLE = "Breakout"

BLACK = (0, 0, 0)
RED = (200, 72, 72)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 20
PLAYER_STARTING_X = WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2
PLAYER_STARTING_Y = 550
PLAYER_VELOCITY = 10


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)

    running = True
    clock = pygame.time.Clock()

    player_x = PLAYER_STARTING_X
    player_y = PLAYER_STARTING_Y
    vel = PLAYER_VELOCITY

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_x -= vel
        if keys[pygame.K_RIGHT]:
            player_x += vel

        screen.fill(BLACK)
        pygame.draw.rect(
            screen, RED, pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        )
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
