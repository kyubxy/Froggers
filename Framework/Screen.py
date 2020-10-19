import pygame
from SpriteText import *

# Drawables are sorted into screens that can be drawn at different times
class Screen (pygame.sprite.LayeredUpdates):
    def __init__(self, game):
        super(Screen, self).__init__(self)
        self.game = game

        # fps counter
        self.frameratecounter = SpriteText ("fps", 24)
        self.frameratecounter.Background = [0,0,0]

        # TODO remove if unnecessary
        self.Add (self.frameratecounter)

    def Update (self):
        super(Screen, self).update()

        # update fps counter
        fpstext = "fps: {0}".format (round(self.game.Clock.get_fps(), 2))
        self.frameratecounter.SetText (fpstext)
        # position fps counter to the bottom right corner
        self.frameratecounter.rect.x = pygame.display.get_surface().get_size()[0] - self.frameratecounter.image.get_size()[0]
        self.frameratecounter.rect.y = pygame.display.get_surface().get_size()[1] - self.frameratecounter.image.get_size()[1]

    def Add (self, sprite):
        super(Screen, self).add (sprite)
        self.move_to_front (self.frameratecounter)

    def Remove (self, sprite):
        super().remove (sprite)

    def Draw (self, win):
        super (Screen, self).draw (win)

    def EnableFPS (self):   # turn fps counter on
        self.Add (self.frameratecounter)

    def DisableFPS (self):  # turn fps counter off
        self.frameratecounter.kill()