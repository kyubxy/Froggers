import pygame
from Framework.Sprite import *

class LivesDisplay (pygame.sprite.Group):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.lifetex = pygame.image.load ("res/textures/img_lives.png")
        self.UpdateLives()

    def UpdateLives (self):
        self.empty()
        for life in range(self.player.Lives):
            self.lifesprite = Sprite (img = self.lifetex)
            self.lifesprite.rect.x += life * self.lifesprite.rect.width
            self.lifesprite.rect.y = pygame.display.get_surface().get_size()[1] - self.lifesprite.rect.height
            self.add (self.lifesprite)

    def empty (self):
        super().empty()