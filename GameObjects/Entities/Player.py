import pygame
import math
from constants import *
from Sprite import *
from Framework.MouseListener import *
from GameObjects.Entities.Obstacle import *
from GameObjects.Entities.Log import *
from GameObjects.turfs.GrassTurf import Cave

class Player (Sprite):
    def __init__(self, level):
        # graphics
        self.deadimg = pygame.image.load ("res/textures/img_playerdead.png")        # TODO add dead player
        self.aliveimg = pygame.image.load("res/textures/img_player.png")
        self.hideimg = pygame.Surface ((1,1))
        super().__init__(img = self.aliveimg)   # load image
        self.Scale (64,64)
        self.rect.x = 64 * 6

        # environment
        self.level = level
        self.absolute_y = 0

        # properties
        self.Alive = True   # determines if player is alive or is just a sludge of mangled frog parts
        self.Winning = False
        self.Lives = 5      # 0 lives means a game over
        self.Frogs = 5      # total number of players

        # key strokes require two keyboard states
        self.oldkeystate = pygame.key.get_pressed()
        self.newkeystate = pygame.key.get_pressed() 

        # mouse strokes also require two keyboard states
        self.oldmousestate = pygame.mouse.get_pressed()
        self.newmousestate = pygame.mouse.get_pressed()

        self.logoffset = 0
    
    def update (self):
        super().update()

        self.handleInput()
        self.collision()

    # collision detection
    def collision (self):
        for other in self.level.sprites():
            if self.rect.colliderect(other.rect):
                # obstacle collision
                if issubclass (type(other), Harmable):  # harmable is generic, check subclass
                    self.die()

                # cave collision
                if type (other) == Cave:
                    if not other.Occupied:  # check if occupied
                        other.Occupy()      # occupy if possible
                        self.win()

                # log collision
                if type (other) == Log:
                    self.logoffset = self.rect.x - other.rect.x
                    self.rect.x = other.rect.x + self.logoffset

    # input
    def handleInput (self):
        self.newkeystate = pygame.key.get_pressed()

        if self.Alive and not self.Winning:
            # left
            if get_keydown (self.oldkeystate, self.newkeystate, [pygame.K_LEFT, pygame.K_a]): 
                if self.rect.x > 0:
                    self.rect.x -= 64
            # right
            elif get_keydown (self.oldkeystate, self.newkeystate,[pygame.K_RIGHT, pygame.K_d]):
                if self.rect.x + 128 < pygame.display.get_surface().get_size()[0]:
                    self.rect.x += 64

            # down
            # TODO make downwards limit 
            if get_keydown (self.oldkeystate, self.newkeystate, [pygame.K_DOWN, pygame.K_s]):
                if (self.absolute_y >= pygame.display.get_surface().get_size()[1] / 2 - 64):    
                    self.level.change_pos_y(-64)
                else:
                    self.rect.y += 64

                self.absolute_y += 64
            # up
            elif get_keydown (self.oldkeystate, self.newkeystate, [pygame.K_UP, pygame.K_w]):
                if (self.absolute_y > 0):          # prevent the player from moving off screen
                    if (self.absolute_y < pygame.display.get_surface().get_size()[1] / 2):     # prevent camera from panning off screen
                        self.rect.y -= 64
                    else:
                        self.level.change_pos_y(64)

                    self.absolute_y -= 64

            self.oldmousestate = self.newmousestate

            if self.Winning:
                if self.newkeystate [pygame.K_SPACE]:
                    self.restart()        
        else:
            if self.newkeystate [pygame.K_SPACE]:
                self.restart()       

        # update old state
        self.oldkeystate = self.newkeystate

    def win (self):
        self.Winning = True
        self.image = self.hideimg
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

def get_keydown (oldkeystate, newkeystate, keys):
    return any ([newkeystate[k] and not oldkeystate[k] for k in keys])