import math
import random

from colors import RED
from entity import Entity, is_collision, is_side_collision
from player import PLAYER_Y
from velocity import Velocity
from window import WINDOW_HEIGHT, WINDOW_WIDTH

BALL_SIZE = 20
BALL_X = WINDOW_WIDTH / 2 - BALL_SIZE / 2
BALL_Y = PLAYER_Y - BALL_SIZE
BALL_VELOCITY_X = 5
BALL_VELOCITY_Y = -10
BALL_SPEED_MODIFIER = 5


class Ball(Entity):
    def __init__(self):
        self.x = BALL_X
        self.y = BALL_Y
        self.width = BALL_SIZE
        self.height = BALL_SIZE
        self.color = RED
        self.velocity = Velocity()

    def move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    def update(self, launch, player, blocks, walls):
        if launch and not self.velocity.is_moving():
            self.velocity.x = BALL_VELOCITY_X * math.pow(-1, random.randint(1, 3))
            self.velocity.y = BALL_VELOCITY_Y

        if not self.velocity.is_moving():
            self.x = player.x + player.width / 2 - self.width / 2
            self.y = player.y - player.height
        else:
            self.move()

        return self._handle_collisions(player, blocks, walls)

    def _handle_collisions(self, player, blocks, walls):
        self._handle_wall_collisions(walls)
        self._handle_player_collisions(player)
        return self._handle_block_collisions(blocks)

    def _handle_player_collisions(self, player):
        if is_collision(self.get_bounding_box(), player.get_bounding_box()):
            self.velocity.reverse()
            self.y = player.y - self.width

    def _handle_wall_collisions(self, walls):
        left_wall = walls[0]
        right_wall = walls[1]
        top_wall = walls[2]

        if self.x < left_wall.width:
            self.x = left_wall.width
            self.velocity.reverse_x()
        if self.x + self.width > right_wall.x:
            self.x = right_wall.x - self.width
            self.velocity.reverse_x()
        if self.y < top_wall.y + top_wall.height:
            self.y = top_wall.y + top_wall.height
            self.velocity.reverse_y()

    def _handle_block_collisions(self, blocks):
        left_x = self.x
        left_y = self.y + self.height / 2
        right_x = self.x + self.width
        right_y = self.y + self.height / 2
        top_x = self.x + self.width / 2
        top_y = self.y
        bottom_x = self.x + self.width / 2
        bottom_y = self.y + self.height

        for block in blocks:
            if is_side_collision(left_x, left_y, block.get_bounding_box()):
                self.y += self.height
                self.velocity.reverse_x()
                blocks.remove(block)
                return block.value
            elif is_side_collision(right_x, right_y, block.get_bounding_box()):
                self.y -= self.height
                self.velocity.reverse_x()
                blocks.remove(block)
                return block.value
            elif is_side_collision(top_x, top_y, block.get_bounding_box()):
                self.y += self.height
                self.velocity.reverse_y()
                blocks.remove(block)
                return block.value
            elif is_side_collision(bottom_x, bottom_y, block.get_bounding_box()):
                self.y -= self.height
                self.velocity.reverse_y()
                blocks.remove(block)
                return block.value
        return 0

    def _handle_loss_collisions(self):
        bottom_y = self.y + self.height

        if bottom_y > WINDOW_HEIGHT:
            return {"loss": True}
