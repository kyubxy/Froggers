import pygame
import random
import math
from Framework.TileArea import *
from GameObjects.turfs.RailTurf import *
from GameObjects.turfs.RoadTurf import *

class Level (pygame.sprite.LayeredUpdates): 
    def __init__(self, difficulty):
        super().__init__(self)
        # background
        self.background = TileArea("res/textures/img_grass.png", (pygame.display.get_surface().get_size()), (128,128))
        self.add (self.background)

        self.difficulty = difficulty

        # y position (scrolling only happpens on this axis)
        self.Position = 0

        # list of all available turfs
        self.turfs = [RailTurf, RoadTurf]

        self.generate()

    def generate (self, seed = None):
        random.seed (seed)

        # number of turfs to be generated
        self.turfno = random.randint (math.ceil (self.difficulty / 2), math.ceil(self.difficulty * 1.5))
        
        # list of all turfs in the level
        self.levelturfs = list()

        # generate turfs
        for _ in range(self.turfno):
            # add turf to level turfs
            self.turfid = random.randint (0, len (self.turfs)-1)
            self.workingturf = self.turfs[self.turfid]()

            # place the turf (should be directly adjacent to all other turfs)
            for t in self.levelturfs:
                self.workingturf.rect.y += t.tilesize[0]

            self.levelturfs.append (self.workingturf)

            print (self.workingturf, self.workingturf.rect.y)

        for t in self.levelturfs:
            self.add (t)

    # this update method is NOT included in the group call
    # and is instead called MANUALLY
    def Update (self):
        for s in self.sprites():
            s.rect.y -= self.Position
    
    #def performculling (self):


        

