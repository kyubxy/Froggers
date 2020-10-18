from GameObjects.Entities.Obstacle import *
import random

class Train (Obstacle):
    def __init__(self, dir, pos, speed, frequency_offset):
        self.dirname = "right" if dir == 1 else "left"
        self.path = "res/textures/img_train_" + self.dirname + ".png"
        super().__init__(self.path, dir, pos, speed, frequency_offset)