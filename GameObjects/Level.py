import pygame
import random
import math
from Framework.GeometricGroup import *
from Framework.TileSurface import *
from GameObjects.turfs.RailTurf import *
from GameObjects.turfs.RoadTurf import *
from GameObjects.turfs.GrassTurf import *
from GameObjects.turfs.LakeTurf import *

from Framework.KeyboardListener import *

# the physical composition of the level itself.
class Level (GeometricGroup): 
    def __init__(self, difficulty, game):
        super().__init__()
        
        self.game = game

        # arbitrary value defining relatively difficulty of current level
        # influences variables like level length, entity speeds, general complexity etc
        self.difficulty = difficulty

        # list of all available turfs
        self.turfs = [RailTurf, RoadTurf, LakeTurf]

        # generate level
        self.generate()

    # randomly generates the level
    def generate (self, seed = None):
        print ("Starting level", self.difficulty)

        if seed is None:
            seed = random.randint (0,999999)
        random.seed (seed)      
        print (seed)

        # number of turfs to be generated
        self.turfno = random.randint (math.ceil (self.difficulty / 2), math.ceil(self.difficulty * 1.5))
        
        # list of all turfs in the level
        self.levelturfs = list()

        # first strip
        self.levelturfs.append (GrassTurf(self.game))

        # generate turfs
        for _ in range(self.turfno):
            # add turf to level turfs
            self.turfid = random.randint (0, len (self.turfs)-1)
            self.directions = [-1, 1]
            self.workingturf = self.turfs[self.turfid](self.difficulty, self.directions[random.randint (0,1)], self.game)

            # place the turf (should be directly adjacent to all other turfs)
            for t in self.levelturfs:
                self.workingturf.change_pos_y (t.background.rect.height)

            self.levelturfs.append (self.workingturf)

        # last strip
        self._l = GrassEndTurf(self.game)
        # place the turf (should be directly adjacent to all other turfs)
        for t in self.levelturfs:
            self._l.change_pos_y (t.background.rect.height)
        self.levelturfs.append (self._l)

        for t in self.levelturfs:
            self.Add (t)

    # this update method is NOT included in the group call
    # and is instead called MANUALLY
    def Update (self):
        self.performculling()
    
    # prevents turfs that aren't currently on screen from drawing
    # marginally increases performance
    def performculling (self):
        for t in self.levelturfs:
            if (t.background.rect.bottom >= 0 and t.background.rect.y < pygame.display.get_surface().get_size()[1]):
                t.Active()
                t.Update()
            else:
                t.NonActive()

    def change_pos_y (self, pos):
        super().change_pos_y (pos)