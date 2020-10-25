from GameObjects.Entities.Obstacle import *
import random

class Car (Obstacle, Harmable):
    def __init__(self, direc, pos, speed, game):
        self.dirname = "right" if direc == 1 else "left"
        self.path = "img_car_" + str(random.randint(1, 7)) + self.dirname
        super().__init__(self.path, direc, pos, speed, game)

    def update (self):
        super().update()