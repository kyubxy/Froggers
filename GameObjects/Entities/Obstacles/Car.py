from GameObjects.Entities.Obstacles.Obstacle import *
import random

# car obstacle
class Car (Obstacle, Harmable):
    def __init__(self, direc, pos, speed, game):
        # find appropriate texture
        self.dirname = "right" if direc == 1 else "left"
        self.path = "img_car_" + str(random.randint(1, 7)) + self.dirname

        super().__init__(self.path, direc, pos, speed, game)

    def update (self):
        super().update()