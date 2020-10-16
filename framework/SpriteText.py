import pygame
from Sprite import *

# all text is drawn as a sprite
class SpriteText (Sprite):
    def __init__(self, text, size = 48, font = None):

        self.Colour = [255,255,255]
        self.Background = None
        self._text = text

        # if there isn't a font, use the system default
        if font is None:
            self.Font = pygame.font.SysFont (None, size)

        # draw the font through the constructor
        super().__init__(img = self.Font.render (self._text, True, self.Colour, self.Background))

    def update (self):
        super().update()

    def SetText (self, text):
        self._text = text
        self.UpdateText() 

    def UpdateText (self):
        self.image = self.Font.render (self._text, True, self.Colour, self.Background)

    def kill (self):
        super().kill()