from GameObjects.Entities.Obstacle import *
import random

class Car (Obstacle, Harmable):
    def __init__(self, direc, pos, speed):
        self.dirname = "right" if direc == 1 else "left"
        self.path = "res/textures/img_car_" + str(random.randint(1, 7)) + self.dirname + ".png"
        super().__init__(self.path, direc, pos, speed)