from GameObjects.turfs.Turf import Turf
from GameObjects.Entities.Car import *
import math
import random

class RoadTurf (Turf):
    def __init__(self, difficulty, direc):
        self.difficulty = difficulty
        Turf.__init__ (self, 8, "res/textures/img_roadstrip.png")

        # 2 lanes
        for lane in range (2):
            self.lanesp = random.randint (4,7 + self.difficulty)
            for i in range(math.floor (self.difficulty / 10) + 1):
                self.laneyoffset = 150 if lane == 1 else 269     # aligning the car into the correct lane
                self.Add (Car(direc, (i * 300 + random.randint(30,100),self.laneyoffset), self.lanesp))

    def Update (self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive (self)