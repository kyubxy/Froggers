from GameObjects.Entities.Obstacle import *
import random

class Log (Obstacle):
    def __init__(self, dir, pos, speed):
        self.dirname = "right" if dir == 1 else "left"
        self.path = "res/textures/img_grass.png"
        super().__init__(self.path, dir, pos, speed)
        self.Scale (64 * 4, 64)