import pygame
import math
from Framework.Sprite import *

# any tiled surface repeated over some area
class TileArea (Sprite):
    def __init__(self, path, coverarea, tilesize = None):

        # procedurally create a single tile surface that covers the width of the screen   
        self.tile = pygame.image.load (path)    # load tile texture
        self.tilesize = (self.tile.get_rect().width,self.tile.get_rect().height) if tilesize is None else tilesize    # size of each of the tiles
        self.tile = pygame.transform.scale (self.tile, tilesize)                 # scale tile with tilesize

        # generate empty surface
        self.surf = pygame.Surface (coverarea)
        self.surf.fill([255,255,255])

        for x in range (math.ceil(coverarea[0]/self.tilesize[0])):          # find total number of tiles that can fit 
            for y in range (math.ceil(coverarea[1]/self.tilesize[1])):
                self.surf.blit (self.tile, (x * self.tile.get_rect().width, y * self.tile.get_rect().height))     # blit directly to surface

        # load the completed surface into the sprite
        super().__init__(img = self.surf)

