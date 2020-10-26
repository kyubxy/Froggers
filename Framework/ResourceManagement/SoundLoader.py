import pygame

# load in exclusively sound effects (se)
# use pygame.mixer.music for bgm
class SoundLoader:
    def __init__ (self):
        pass

    def get_asset (self, path):
        return pygame.mixer.Sound (path)