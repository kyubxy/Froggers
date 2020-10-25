import pygame

class SoundLoader:
    def __init__ (self):
        pass

    def get_asset (self, path):
        return pygame.mixer.Sound (path)