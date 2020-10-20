import pygame
import math
from constants import *
from Sprite import *
from Framework.MouseListener import *
from GameObjects.Entities.Obstacle import *
from GameObjects.turfs.GrassTurf import Cave

class Player (Sprite):
    def __init__(self, level):
        # graphics
        self.deadimg = pygame.image.load ("res/textures/img_cave.png")        # TODO add dead player
        self.aliveimg = pygame.image.load("res/textures/img_player.png")
        super().__init__(img = self.aliveimg)   # load image
        self.Scale (64,64)

        # environment
        self.level = level
        self.absolute_y = 0

        # properties
        self.Alive = True   # determines if player is alive or is just a sludge of mangled frog parts
        self.Winning = False
        self.Lives = 5      # 0 lives means a game over
        self.Frogs = 5      # total number of players

        # key strokes require two keyboard states
        self.oldstate = pygame.key.get_pressed()
        self.newstate = pygame.key.get_pressed() 
    
    def update (self):
        super().update()

        self.handleInput()
        self.collision()

    # collision detection
    def collision (self):
        for other in self.level.sprites():
            if self.rect.colliderect(other.rect):
                # obstacle collision
                if issubclass (type(other), Obstacle):
                    self.die()

                # cave collision
                if type (other) == Cave:
                    if not other.Occupied:  # check if occupied
                        other.Occupy()      # occupy if possible
                        self.win()

    # input
    def handleInput (self):
        self.newstate = pygame.key.get_pressed()

        if self.Alive and not self.Winning:
            if self.newstate[pygame.K_LEFT] and not self.oldstate[pygame.K_LEFT]:
                self.rect.x -= 64
            elif self.newstate[pygame.K_RIGHT] and not self.oldstate[pygame.K_RIGHT]:
                self.rect.x += 64

            if self.newstate[pygame.K_DOWN] and not self.oldstate[pygame.K_DOWN]:
                 # XXX subtracted 64 to fix regression in camera moving, consider removing if there's another regression
                if (self.absolute_y >=pygame.display.get_surface().get_size()[1] / 2 - 64):    
                    self.level.change_pos_y(-64)
                else:
                    self.rect.y += 64
                self.absolute_y += 64
            elif self.newstate[pygame.K_UP] and not self.oldstate[pygame.K_UP]:
                if (self.absolute_y > 0):          # prevent the player from moving off screen
                    if (self.absolute_y < pygame.display.get_surface().get_size()[1] / 2 - 64):     # prevent camera from panning off screen
                        self.rect.y -= 64
                    else:
                        self.level.change_pos_y(64)
                    self.absolute_y -= 64

            if self.Winning:
                if self.newstate [pygame.K_SPACE]:
                    self.restart()        
        else:
            if self.newstate [pygame.K_SPACE]:
                self.restart()       

        # update old state
        self.oldstate = self.newstate

    def win (self):
        self.Winning = True
        pygame.event.post (pygame.event.Event (WIN))

    # called after death
    def restart (self):
        pygame.event.post (pygame.event.Event (RESTART))
        if (self.absolute_y > pygame.display.get_surface().get_size()[1] / 2):  # only move the background if it has been moved
            # offset by rounding to the nearest 64
            self.level.change_pos_y (self.absolute_y - math.ceil(pygame.display.get_surface().get_size()[1] / 128) * 64 + 64) 

        self.rect.y = 0
        self.absolute_y = 0

        if (self.Winning):
            self.Frogs -= 1

        if (not self.Alive):
            self.Lives -= 1
            
        self.Alive = True
        self.Winning = False
        self.image = self.aliveimg
        self.Scale (64,64)
                
    # this method handles actual loss of the game
    def die (self):
        self.Alive = False
        self.image = self.deadimg
        self.Scale (64,64)
        pygame.event.post (pygame.event.Event (DEATH))

    # this method handles pygame.kill() it removes this instance from all groups
    def kill(self):
        super().kill()

    def Scale (self, width, height):
        super().Scale(width, height)
