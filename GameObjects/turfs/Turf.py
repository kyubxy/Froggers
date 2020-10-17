import pygame
import math
from Framework.TileArea import TileArea

# any tiled surface repeated over the width of the screen
class Turf (TileArea, ):
    def __init__(self, path, tilesize):
        # width of window
        self.screenwidth = pygame.display.get_surface().get_size()[0]

        super().__init__(path, (self.screenwidth, tilesize * 64),(tilesize * 64, tilesize * 64))
        # in this case, 64 is the side length of a frogger unit square
        