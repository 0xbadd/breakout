import pygame

from entity import Entity

TITLE = "Breakout"

BLACK = (0, 0, 0)
GREY = (142, 142, 142)
RED = (200, 72, 72)
ORANGE = (198, 108, 58)
BROWN = (180, 122, 48)
YELLOW = (162, 162, 42)
GREEN = (72, 160, 72)
BLUE = (66, 72, 200)

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

BLOCK_WIDTH = 80
BLOCK_HEIGHT = 20
NUM_BLOCKS_X = 9
NUM_BLOCKS_Y = 6

WALL_SIZE = 40

FPS = 60


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)

    player = Entity(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, RED)

    ball = Entity(BALL_X, BALL_Y, BALL_SIZE, BALL_SIZE, RED)

    walls = []
    left_wall = Entity(0, 50, WALL_SIZE, WINDOW_HEIGHT - 80, GREY)
    right_wall = Entity(
        WINDOW_WIDTH - WALL_SIZE, 50, WALL_SIZE, WINDOW_HEIGHT - 80, GREY
    )
    top_wall = Entity(0, 50, WINDOW_WIDTH, WALL_SIZE, GREY)
    walls.append(left_wall)
    walls.append(right_wall)
    walls.append(top_wall)

    blocks = []
    for row in range(0, NUM_BLOCKS_Y):
        for col in range(0, NUM_BLOCKS_X):
            block_x = col * BLOCK_WIDTH
            block_y = row * BLOCK_HEIGHT
            block_color = None
            if row == 0:
                block_color = RED
            elif row == 1:
                block_color = ORANGE
            elif row == 2:
                block_color = BROWN
            elif row == 3:
                block_color = YELLOW
            elif row == 4:
                block_color = GREEN
            else:
                block_color = BLUE
            blocks.append(
                Entity(
                    WALL_SIZE + block_x,
                    WALL_SIZE * 2 + 48 + block_y,
                    BLOCK_WIDTH,
                    BLOCK_HEIGHT,
                    block_color,
                )
            )

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

        if player.x < left_wall.width:
            player.x = left_wall.width
        if player.x + player.width > right_wall.x:
            player.x = right_wall.x - player.width

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
