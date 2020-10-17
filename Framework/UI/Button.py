from Sprite import *
from SpriteText import *
from MouseListener import *
import pygame

class Pane (Sprite, MouseListener):
    def __init__(self, w, h):
        self._s = pygame.Surface ([w,h])
        self._s.fill([255,255,255])
        super().__init__ (img = self._s)

    def update (self):
        pass

    def MouseDown (self, event):
        if (self.rect.collidepoint (event.pos)):
            print ("click")

class Button (pygame.sprite.OrderedUpdates):
    def __init__(self, label = "button", w = 200, h=50):
        super().__init__()
        
        self._pane = Pane (w, h)
        self.add (self._pane)

        self._label = SpriteText (label, 48)
        self._label.SetColour ([0,0,0])
        self.add (self._label)

    def rect_get (self):
        return self._pane.rect

    def rect_set (self, rect):
        self._pane.rect = rect

    def kill (self):
        super().kill()
        