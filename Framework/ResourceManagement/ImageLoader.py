import pygame

class ImageLoader:
    def __init__(self):
        pass

    def get_asset (self, path):
        return pygame.image.load (path).convert_alpha()