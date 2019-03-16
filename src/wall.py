from colors import GREY
from entity import Entity
from window import WINDOW_HEIGHT, WINDOW_WIDTH

WALL_SIZE = 40


class Wall(Entity):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

    def move():
        pass

    def update():
        pass


def init_walls():
    walls = []
    left_wall = Wall(0, 50, WALL_SIZE, WINDOW_HEIGHT - 80, GREY)
    right_wall = Wall(WINDOW_WIDTH - WALL_SIZE, 50, WALL_SIZE, WINDOW_HEIGHT - 80, GREY)
    top_wall = Wall(0, 50, WINDOW_WIDTH, WALL_SIZE, GREY)
    walls.append(left_wall)
    walls.append(right_wall)
    walls.append(top_wall)

    return walls
