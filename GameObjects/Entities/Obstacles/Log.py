from GameObjects.Entities.Obstacles.Obstacle import *
import random

# log obstacle
class Log (Obstacle):
    def __init__(self, dir, pos, speed, width, game):
        self.direc = dir
        super().__init__("img_log", dir, pos, speed, game)
        self.Scale (width * 64, 64)