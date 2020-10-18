from GameObjects.Entities.Obstacle import *
import random

class Car (Obstacle):
    def __init__(self, dir, pos, speed, frequency_offset):
        self.dirname = "right" if dir == 1 else "left"
        self.path = "res/textures/img_car_" + str(random.randint(1, 7)) + self.dirname + ".png"
        super().__init__(self.path, dir, pos, speed, frequency_offset)