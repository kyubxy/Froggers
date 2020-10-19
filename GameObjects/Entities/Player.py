import pygame
import math
import constants
from Sprite import *
from Framework.KeyboardListener import *
from Framework.MouseListener import *
from GameObjects.Entities.Obstacle import *

class Player (Sprite, KeyboardListener):
    def __init__(self, level):
        # graphics
        self.deadimg = pygame.image.load ("res/textures/img_cave.png")        # TODO add dead player
        self.aliveimg = pygame.image.load("res/textures/img_player.png")
        super().__init__(img = self.aliveimg)
        self.Scale (64,64)

        # environment
        self.level = level
        self.absolute_y = 0

        # properties
        self.Alive = True   # determines if player is alive or is just a sludge of mangled frog parts
        self.Lives = 5      # 0 lives means a game over

    def KeyDown (self, e):
        if (self.Alive):
            if (e.key == pygame.K_DOWN):
                self.absolute_y += 64
                if (self.absolute_y > pygame.display.get_surface().get_size()[1] / 2):
                    self.level.change_pos_y(-64)
                else:
                    self.rect.y += 64
            elif (e.key == pygame.K_UP):
                if (self.absolute_y > 0):          # prevent the player from moving off screen
                    if (self.absolute_y <= pygame.display.get_surface().get_size()[1] / 2):     # prevent camera from panning off screen
                        self.rect.y -= 64
                    else:
                        self.level.change_pos_y(64)
                    self.absolute_y -= 64
                
            if (e.key == pygame.K_LEFT and self.rect.x > 0):# prevent the player from moving off screen
                self.rect.x -= 64
            elif (e.key == pygame.K_RIGHT and self.rect.x + 100 < pygame.display.get_surface().get_size()[0]):# prevent the player from moving off screen
                self.rect.x += 64
        else:
            self.restart()

    def MouseDown (self, e):
        pass        

    def Scale (self, width, height):
        super().Scale(width, height)

    def update (self):
        super().update()

        # collision detection
        for other in self.level.sprites():
            if self.rect.colliderect(other.rect):
                # obstacle collision
                if issubclass (type(other), Obstacle):
                    self.Alive = False
                    self.image = self.deadimg
                    self.Scale (64,64)

                # cave collision
                # TODO
                
    def restart (self):
        if (self.absolute_y > pygame.display.get_surface().get_size()[1] / 2):  # only move the background if it has been moved
            # offset by rounding to the nearest 64
            self.level.change_pos_y (self.absolute_y - math.ceil(pygame.display.get_surface().get_size()[1] / 128) * 64)        
        self.rect.y = 0
        self.Lives -= 1
        pygame.event.post (pygame.event.Event (pygame.USEREVENT + 2))
        self.absolute_y = 0
        self.Alive = True
        self.image = self.aliveimg
        self.Scale (64,64)
 
    # this method handles pygame.kill() it removes this instance from all groups
    def kill(self):
        super().kill()

