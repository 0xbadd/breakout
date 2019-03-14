class Velocity:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def is_moving(self):
        return self.x != 0 and self.y != 0
