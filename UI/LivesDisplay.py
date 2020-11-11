import pygame
from Framework.Sprite import *

# shows number of lives
class LivesDisplay (pygame.sprite.Group):
    def __init__(self, player, game):
        super().__init__()
        self.player = player
        self.lifetex = game.ResourceCache.Resources ["img_lives"]
        self.UpdateLives()

    def UpdateLives (self):
        self.empty()
        # draw all lives
        for life in range(self.player.Lives):
            self.lifesprite = Sprite (img = self.lifetex)
            self.lifesprite.rect.x += life * self.lifesprite.rect.width
            self.lifesprite.rect.y = 0
            self.add (self.lifesprite)

    def empty (self):
        super().empty()