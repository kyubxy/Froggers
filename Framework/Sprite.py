import pygame
from constants import *

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

    def Scale (self, width, height):
        # update rect
        self.rect.width = width
        self.rect.height = height

        # perform scale
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))     

    # used by pygame group
    def update (self):
        pass

    def kill (self):
        super().kill()