import pygame
import math
from constants import *
from Sprite import *
from Framework.MouseListener import *
from GameObjects.Entities.Obstacle import *

class Player (Sprite):
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

        # key strokes require two keyboard states
        self.oldstate = pygame.key.get_pressed()
        self.newstate = pygame.key.get_pressed() 

    def Scale (self, width, height):
        super().Scale(width, height)

    def update (self):
        super().update()

        self.handleInput()
        #self.collision()

    # collision detection
    def collision (self):
        for other in self.level.sprites():
            if self.rect.colliderect(other.rect):
                # obstacle collision
                if issubclass (type(other), Obstacle):
                    self.Alive = False
                    self.image = self.deadimg
                    self.Scale (64,64)
                    pygame.event.post (pygame.event.Event (DEATH))

                # cave collision
                # TODO

    def handleInput (self):
        # input
        self.newstate = pygame.key.get_pressed()

        if self.Alive:
            if self.newstate[pygame.K_LEFT] and not self.oldstate[pygame.K_LEFT]:
                self.rect.x -= 64
            elif self.newstate[pygame.K_RIGHT] and not self.oldstate[pygame.K_RIGHT]:
                self.rect.x += 64

            if self.newstate[pygame.K_DOWN] and not self.oldstate[pygame.K_DOWN]:
                if (self.absolute_y >=pygame.display.get_surface().get_size()[1] / 2-64):
                    self.level.change_pos_y(-64)
                else:
                    self.rect.y += 64
                self.absolute_y += 64
            elif self.newstate[pygame.K_UP] and not self.oldstate[pygame.K_UP]:
                if (self.absolute_y > 0):          # prevent the player from moving off screen
                    if (self.absolute_y < pygame.display.get_surface().get_size()[1] / 2):     # prevent camera from panning off screen
                        self.rect.y -= 64
                    else:
                        self.level.change_pos_y(64)
                    self.absolute_y -= 64
        else:
            if self.newstate [pygame.K_SPACE]:
                pygame.event.post (pygame.event.Event (RESTART))
                self.restart()           

        print (self.absolute_y)

        # update old state
        self.oldstate = self.newstate
                
    def restart (self):
        pygame.event.post (pygame.event.Event (RESTART))
        if (self.absolute_y > pygame.display.get_surface().get_size()[1] / 2):  # only move the background if it has been moved
            # offset by rounding to the nearest 64
            self.level.change_pos_y (self.absolute_y- math.ceil(pygame.display.get_surface().get_size()[1] / 128) * 64 - 64) 

        self.rect.y = 0
        self.Lives -= 1
        self.absolute_y = 0
        self.Alive = True
        self.image = self.aliveimg
        self.Scale (64,64)
 
    # this method handles pygame.kill() it removes this instance from all groups
    def kill(self):
        super().kill()

