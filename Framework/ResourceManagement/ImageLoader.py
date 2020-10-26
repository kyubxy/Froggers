import pygame

# loads image formats and returns surfaces
class ImageLoader:
    def __init__(self):
        pass

    def get_asset (self, path):
        return pygame.image.load (path).convert_alpha()