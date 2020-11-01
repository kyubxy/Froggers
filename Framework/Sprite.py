import pygame
import math

# anything that draws to the screen must be or inherit from this type
# path can either be a direct path to image or resource name (if a resource cache is supplied)
class Sprite (pygame.sprite.Sprite):
    def __init__(self, path = "", img = None, resources = None):
        super().__init__()

        # load the image from file if there isn't already an image parsed through the constructor
        if img is None:
            # use image from resource cache if possible
            if not resources is None:
                self.image = resources[path]
            else:
                self.image = pygame.image.load (path).convert_alpha()
        else:
            self.image = img

        self.rect = self.image.get_rect()
        self.angle = 0

        self._originalimage = self.image

    # rotate object about the vertical axis
    def Rotate(self, angle):
        # prevent the angle from being too large
        modangle = angle % 360
        # rotate the image
        self.image = pygame.transform.rotate (self._originalimage, modangle)

        self._updateCenter ()

        self.angle = modangle

    # you can also modify self.image directly however problems arise when the sprite is rotated and is generally not recommended
    def ChangeImage (self, surface):
        self.image = surface
        self.rect = surface.get_rect()
        self._originalimage = surface

    # changes width and height
    def Scale (self, width, height):
        self.rect.width = width
        self.rect.height = height
        # perform the scaling move
        self.image = pygame.transform.scale(self._originalimage, (int(width), int(height)))  

    def _updateCenter (self):
        # update the center of the rectangle. 
        # the size of the surface changes and so too does the center so the current rectangle needs its center updated accordingly
        old_x, old_y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (old_x, old_y)

    def Show (self):
        self.image = self._originalimage

    def Hide (self):
        self.image = pygame.Surface ((1,1))

    # used by pygame group, called once per frame
    def update (self):
        pass

    # removes all instances of this object from all pygame groups
    def kill (self):
        super().kill()
