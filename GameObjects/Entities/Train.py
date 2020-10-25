from GameObjects.Entities.Obstacle import *
import random

class Train (Obstacle, Harmable):
    def __init__(self, dir, pos, speed, game):
        self.dirname = "right" if dir == 1 else "left"
        self.path = "img_train_" + self.dirname
        super().__init__(self.path, dir, pos, speed, game)

    def update (self):
        super().update()