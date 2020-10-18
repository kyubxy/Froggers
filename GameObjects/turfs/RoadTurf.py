from GameObjects.turfs.Turf import Turf
from GameObjects.Entities.Car import *
import math
import random

class RoadTurf (Turf):
    def __init__(self, difficulty, direc):
        self.difficulty = difficulty
        Turf.__init__ (self, 6, "res/textures/img_roadstrip.png")

        for _ in range(math.floor (self.difficulty / 10)):
            self.Add (Car(direc, (0,64), random.randint (10,15), random.randint(0,10)))

    def Update (self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive (self)