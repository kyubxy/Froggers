import pygame
from Framework.Sprite import *

class FrogDisplay (pygame.sprite.Group):
    def __init__(self, player, game):
        super().__init__()
        self.player = player
        self.frogtex = game.ResourceCache.Resources["img_player"]
        self.colouredfrog = game.ResourceCache.Resources ["img_playercurrent"]
        self.UpdateFrogs()

    # update the frog display according to how many frogs are contained within the player
    def UpdateFrogs (self):
        self.empty()
        # draw each of the remaining frogs
        for frog in range(self.player.Frogs):            
            self.frogsprite = Sprite (img = self.frogtex)
            self.frogsprite.Scale (32,32)
            self.frogsprite.rect.x += pygame.display.get_surface().get_size()[0]- frog * self.frogsprite.rect.width
            self.frogsprite.rect.y = 0
            self.add (self.frogsprite)

    def empty (self):
        super().empty()