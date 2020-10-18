import pygame
from Sprite import *
from Framework.KeyboardListener import *

class Player (Sprite, KeyboardListener):
    def __init__(self, level):
        super().__init__("res/textures/img_player.png")
        self.Scale (64,64)
        self.level = level

    def KeyDown (self, e):
        if (e.key == pygame.K_DOWN):
            if (self.rect.y > pygame.display.get_surface().get_size()[1] / 2 - 100):
                self.level.change_pos_y(-64)
            else:
                self.rect.y += 64
        elif (e.key == pygame.K_UP):
            #self.rect.y -= 64
            self.level.change_pos_y(64)
        if (e.key == pygame.K_LEFT):
            self.rect.x -= 64
        elif (e.key == pygame.K_RIGHT):
            self.rect.x += 64

    def Scale (self, width, height):
        super().Scale(width, height)

    def update (self):
        super().update()

    def kill(self):
        super().kill()

