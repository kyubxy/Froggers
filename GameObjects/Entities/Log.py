from GameObjects.Entities.Obstacle import *
import random

class Log (Obstacle):
    def __init__(self, dir, pos, speed, width):
        self.dirname = "right" if dir == 1 else "left"
        self.direc = dir
        self.path = "res/textures/img_log.png"
        super().__init__(self.path, dir, pos, speed)
        self.Scale (width * 64, 64)