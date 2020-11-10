from GameObjects.turfs.Turf import Turf
from GameObjects.Entities.Obstacles.Train import *
import math

# rail turf
class RailTurf (Turf):
    def __init__(self, difficulty, direc, game):
        Turf.__init__ (self, 2, "img_railstrip", game)
        
        # add the train
        self.Add (Train(game, direc, (0,0), random.randint (10,15 + math.floor(difficulty/4)), random.randint (2,5), random.randint (0,2)))
    
    def Update(self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive(self)
