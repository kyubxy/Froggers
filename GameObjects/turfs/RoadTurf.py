from GameObjects.turfs.Turf import Turf
from GameObjects.Entities.Obstacles.Car import *
import math
import random

# road turf
class RoadTurf (Turf):
    def __init__(self, difficulty, direc, game):
        self.difficulty = difficulty
        Turf.__init__ (self, 8, "img_roadstrip", game)

        # add 2 lanes
        for lane in range (2):
            # set a lane speed
            self.lanesp = random.randint (4,7 + self.difficulty)

            # add the cars
            for i in range(math.floor (self.difficulty / 10) + 1):
                self.laneyoffset = 150 if lane == 1 else 269     # aligning the car into the correct lane
                self.Add (Car(direc, (i * 300 + random.randint(30,100),self.laneyoffset), self.lanesp, game))
                
    def Update (self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive (self)