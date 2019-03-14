from entity import Entity

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
