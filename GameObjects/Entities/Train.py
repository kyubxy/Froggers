from GameObjects.Entities.Obstacle import *
import random

# train obstacle
class Train (Obstacle, Harmable):
    def __init__(self, dir, pos, speed, game):
        # load appropriate texture
        self.dirname = "right" if dir == 1 else "left"
        self.path = "img_train_" + self.dirname
        
        super().__init__(self.path, dir, pos, speed, game)

    def update (self):
        super().update()