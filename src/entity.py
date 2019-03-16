from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def render(self, screen):
        pygame.draw.rect(
            screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height)
        )

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def get_bounding_box(self):
        return (self.x, self.y, self.width, self.height)


def is_collision(bbox1, bbox2):
    a_x = bbox1[0]
    a_y = bbox1[1]
    a_width = bbox1[2]
    a_height = bbox1[3]

    b_x = bbox2[0]
    b_y = bbox2[1]
    b_width = bbox2[2]
    b_height = bbox2[3]

    if (
        a_x >= b_x + b_width
        or a_y >= b_y + b_height
        or b_x >= a_x + a_width
        or b_y >= a_y + a_height
    ):
        return False
    else:
        return True


def is_side_collision(x1, y1, bbox2):
    b_x = bbox2[0]
    b_y = bbox2[1]
    b_width = bbox2[2]
    b_height = bbox2[3]

    return x1 >= b_x and x1 <= b_x + b_width and y1 >= b_y and y1 <= b_y + b_height
