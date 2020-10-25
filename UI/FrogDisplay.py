import pygame
from Framework.Sprite import *

class FrogDisplay (pygame.sprite.Group):
    def __init__(self, player, game):
        super().__init__()
        self.player = player
        self.frogtex = game.ResourceCache.Resources["img_player"]
        self.colouredfrog = game.ResourceCache.Resources ["img_playercurrent"]
        self.UpdateFrogs()

    def UpdateFrogs (self):
        self.empty()
        for frog in range(self.player.Frogs):
            if frog == self.player.Frogs - 1:
                self.frogsprite = Sprite (img = self.colouredfrog)
            else:
                self.frogsprite = Sprite (img = self.frogtex)
            self.frogsprite.Scale (32,32)
            self.frogsprite.rect.x += frog * self.frogsprite.rect.width
            self.frogsprite.rect.y =32
            self.add (self.frogsprite)

    def empty (self):
        super().empty()