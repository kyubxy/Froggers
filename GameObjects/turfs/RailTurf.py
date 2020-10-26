from GameObjects.turfs.Turf import Turf
from GameObjects.Entities.Train import *
import math

# rail turf
class RailTurf (Turf):
    def __init__(self, difficulty, direc, game):
        Turf.__init__ (self, 2, "img_railstrip", game)
        
        # add the train
        self.Add (Train(direc, (0,0), random.randint (10,15 + math.floor(difficulty/4)), game))
    
    def Update(self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive(self)
