import pygame
from constants import *

# TODO, support cache loading directly
# anything that draws to the screen must be or inherit from this type
class Sprite (pygame.sprite.Sprite):
    def __init__(self, path = "", img = None):
        super().__init__()

        # load the image from file if there isn't already an image parsed through the constructor
        if img is None:
            self.image = pygame.image.load (path).convert_alpha()
        else:
            self.image = img

        self.rect = self.image.get_rect()
        self.paused = False

    # update the sprite's bounding box, call this whenever self.image changes
    #def UpdateRect (self):

    # changes width and height
    def Scale (self, width, height):
        self.rect.width = width
        self.rect.height = height
        # perform scale
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))  

    # used by pygame group, called once per frame
    def update (self):
        pass

    # removes all instances of this object from all pygame groups
    def kill (self):
        super().kill()