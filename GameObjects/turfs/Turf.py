import pygame
import math
from Framework.GeometricGroup import *
from Framework.TileSurface import *

# a single strip of obstacles
class Turf (GeometricGroup):
    def __init__(self, tilesize, path, game):
        super().__init__()

        # load textures
        self.turftex = game.ResourceCache.Resources[path]
        self.notex = pygame.Surface ((1,1))

        # width of window
        self.screenwidth = pygame.display.get_surface().get_size()[0]
        # in this case, 64 is the side length of a frogger unit square

        # add the background
        self.bgtex = TileSurface (tile = self.turftex, coverarea = (self.screenwidth, tilesize * 64), tilesize = (tilesize * 64, tilesize * 64))
        self.background = Sprite (img = self.bgtex)
        self.Add (self.background)

    def Active (self):
        self.background.image = self.bgtex

    def NonActive (self):
        self.background.image = self.notex