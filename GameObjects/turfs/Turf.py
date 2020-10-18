import pygame
import math
from Framework.GeometricGroup import *
from Framework.TileSurface import *

# any tiled surface repeated over the width of the screen
class Turf (GeometricGroup):
    def __init__(self, tilesize, path):
        super().__init__()

        self.turftex = pygame.image.load (path).convert()
        self.notex = pygame.Surface ((1,1))

        # width of window
        self.screenwidth = pygame.display.get_surface().get_size()[0]
        # in this case, 64 is the side length of a frogger unit square
        self.bgtex = TileSurface (tile = self.turftex, coverarea = (self.screenwidth, tilesize * 64), tilesize = (tilesize * 64, tilesize * 64))
        self.background = Sprite (img = self.bgtex)
        self.Add (self.background)

    def Active (self):
        self.background.image = self.bgtex

    def NonActive (self):
        self.background.image = self.notex

    # parent methods
    def change_pos (self, pos):
        super().change_pos(pos)
    def change_pos_x (self, pos):
        super().change_pos_x(pos)
    def change_pos_y (self, pos):
        super().change_pos_y(pos)
    def Add (self, sprite):
        super().Add (sprite)