import pygame

from entity import Entity, is_collision, is_side_collision

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BLACK = (0, 0, 0)
GREY = (142, 142, 142)
RED = (200, 72, 72)
ORANGE = (198, 108, 58)
BROWN = (180, 122, 48)
YELLOW = (162, 162, 42)
GREEN = (72, 160, 72)
BLUE = (66, 72, 200)

BLOCK_WIDTH = 80
BLOCK_HEIGHT = 20
NUM_BLOCKS_X = 9
NUM_BLOCKS_Y = 6

WALL_SIZE = 40


def render_game(screen, player, ball, blocks, walls):
    screen.fill(BLACK)
    player.render(screen)
    ball.render(screen)
    for block in blocks:
        block.render(screen)
    for wall in walls:
        wall.render(screen)
    pygame.display.flip()


def update_player(player):
    player.move()


def update_ball(ball, player):
    if not ball.velocity.is_moving():
        ball.x = player.x + player.width / 2 - ball.width / 2
        ball.y = player.y - player.height
    else:
        ball.move()


def handle_player_collisions(player, walls):
    left_wall = walls[0]
    right_wall = walls[1]

    if player.x < left_wall.width:
        player.x = left_wall.width
    if player.x + player.width > right_wall.x:
        player.x = right_wall.x - player.width


def handle_ball_collisions(ball, player, walls):
    left_wall = walls[0]
    right_wall = walls[1]
    top_wall = walls[2]

    if ball.x < left_wall.width:
        ball.x = left_wall.width
        ball.velocity.x *= -1
    if ball.x + ball.width > right_wall.x:
        ball.x = right_wall.x - ball.width
        ball.velocity.x *= -1
    if ball.y < top_wall.y + top_wall.height:
        ball.y = top_wall.y + top_wall.height
        ball.velocity.y *= -1

    if is_collision(ball.get_bounding_box(), player.get_bounding_box()):
        ball.velocity.x *= -1
        ball.velocity.y *= -1
        ball.y = player.y - ball.width


def handle_block_collisions(ball, blocks):
    left_x = ball.x
    left_y = ball.y + ball.height / 2
    right_x = ball.x + ball.width
    right_y = ball.y + ball.height / 2
    top_x = ball.x + ball.width / 2
    top_y = ball.y
    bottom_x = ball.x + ball.width / 2
    bottom_y = ball.y + ball.height

    for block in blocks:
        if is_side_collision(left_x, left_y, block.get_bounding_box()):
            ball.y += ball.height
            ball.velocity.x *= -1
            blocks.remove(block)
        if is_side_collision(right_x, right_y, block.get_bounding_box()):
            ball.y -= ball.height
            ball.velocity.x *= -1
            blocks.remove(block)
        if is_side_collision(top_x, top_y, block.get_bounding_box()):
            ball.y += ball.height
            ball.velocity.y *= -1
            blocks.remove(block)
        if is_side_collision(bottom_x, bottom_y, block.get_bounding_box()):
            ball.y -= ball.height
            ball.velocity.y *= -1
            blocks.remove(block)


def init_walls():
    walls = []
    left_wall = Entity(0, 50, WALL_SIZE, WINDOW_HEIGHT - 80, GREY)
    right_wall = Entity(
        WINDOW_WIDTH - WALL_SIZE, 50, WALL_SIZE, WINDOW_HEIGHT - 80, GREY
    )
    top_wall = Entity(0, 50, WINDOW_WIDTH, WALL_SIZE, GREY)
    walls.append(left_wall)
    walls.append(right_wall)
    walls.append(top_wall)

    return walls


def init_blocks():
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
    return blocks
