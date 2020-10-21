from GameObjects.turfs.Turf import Turf
from GameObjects.Entities.Log import *
import math
import random

class LakeTurf (Turf):
    def __init__(self, difficulty, direc):
        Turf.__init__ (self, 4, "res/textures/img_water.jpg")
        
        self.Add (Log(1, (0,0), random.randint (5, 10)))
    
    def Update(self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive(self)
