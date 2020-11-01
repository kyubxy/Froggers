import pygame
from Sprite import *

# all text is drawn as a sprite
class SpriteText (Sprite):
    def __init__(self, text, size = 48, fontPath = None, font = None, colour = [255,255,255], Background = None):

        self.Background = Background          # text background
        self._colour = colour           # colour of text
        self._text = text

        # if there isn't any font specified, use the system default
        if fontPath is None:
            if font is None:
                self.Font = pygame.font.SysFont (None, size)
            else:
                self.Font = font
        else:
            self.Font = pygame.font.Font (fontPath, size)

        # draw the text through the constructor
        super().__init__(img = self.Font.render (self._text, True, self._colour, self.Background))

    def update (self):
        super().update()

    # change the text
    def SetText (self, text):
        self._text = text
        self.UpdateText() 

    # change the colour
    def SetColour (self, col):
        self._colour = col
        self.UpdateText()

    # call this to rerender the text
    def UpdateText (self):
        self.image = self.Font.render (self._text, True, self._colour, self.Background)

    # removes all instances from all groups
    def kill (self):
        super().kill()