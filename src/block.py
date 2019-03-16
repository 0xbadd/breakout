from colors import BLUE, BROWN, GREEN, ORANGE, RED, YELLOW
from entity import Entity
from wall import WALL_SIZE

BLOCK_WIDTH = 80
BLOCK_HEIGHT = 20
NUM_BLOCKS_X = 9
NUM_BLOCKS_Y = 6


class Block(Entity):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

    def __eq__(self, other):
        return (self.x, self.y, self.width, self.height) == (
            other.x,
            other.y,
            other.width,
            other.height,
        )

    def move():
        pass

    def update():
        pass


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
                Block(
                    WALL_SIZE + block_x,
                    WALL_SIZE * 2 + 48 + block_y,
                    BLOCK_WIDTH,
                    BLOCK_HEIGHT,
                    block_color,
                )
            )
    return blocks
