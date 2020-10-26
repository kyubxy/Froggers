import pygame
import math
from Sprite import *

# generate a surface from a tile
def TileSurface (coverarea, path = "", tile = None, tilesize = None):
    # procedurally create a single tile surface 
    if (tile is None): 
        tile = pygame.image.load (path).convert()   # load tile texture
    else:
        tile = tile
            
    tilesize = (tile.get_rect().width, tile.get_rect().height) if tilesize is None else tilesize    # size of each of the tiles
    tile = pygame.transform.scale (tile, tilesize)                 # scale tile with tilesize

    # generate empty surface
    surf = pygame.Surface (coverarea)
    surf.fill([255,255,255])

    for x in range (math.ceil(coverarea[0]/tilesize[0])):          # find total number of tiles that can fit 
        for y in range (math.ceil(coverarea[1]/tilesize[1])):
            surf.blit (tile, (x * tile.get_rect().width, y * tile.get_rect().height))     # blit directly to surface

    # return the completed surface
    return surf