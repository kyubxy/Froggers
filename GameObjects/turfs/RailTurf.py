from GameObjects.turfs.Turf import Turf
from GameObjects.Entities.Train import *
import math

class RailTurf (Turf):
    def __init__(self, difficulty, direc):
        Turf.__init__ (self, 2, "res/textures/img_railstrip.png")
        
        self.Add (Train(direc, (0,0), random.randint (10,15 + math.floor(difficulty/4))))
    
    def Update(self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive(self)
