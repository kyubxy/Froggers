import pygame
import math
import random
from constants import *
from Sprite import *
from Framework.MouseListener import *
from Framework.KeyboardListener import get_keydown
from GameObjects.Entities.Obstacle import *
from GameObjects.Entities.Log import *
from GameObjects.turfs.GrassTurf import Cave
from GameObjects.turfs.LakeTurf import *

# main frog
class Player (Sprite):
    def __init__(self, level, game):
        self.game = game

        # graphics
        self.deadimg = game.ResourceCache.Resources["img_playerdead"]
        self.aliveimg = game.ResourceCache.Resources["img_player"]
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
        self.Lives = LIVES      # 0 lives means a game over
        self.Frogs = FROGS      # total number of players

        # key strokes require two keyboard states
        self.oldkeystate = pygame.key.get_pressed()
        self.newkeystate = pygame.key.get_pressed() 

        # whether or not player is touching log
        self.logging = False

    def update (self):
        super().update()
   
        # move player according to controls
        self.handleInput()

        if self.Alive:
            # handle all player collisions
            self.collision()

        # true if the player is touching a log
        self.logging = False

        # handle offscreen deaths
        if self.rect.x > pygame.display.get_surface().get_size()[0] or self.rect.x + self.rect.width < 0:
            self.die()

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
                    # work using a rate of change rather than position
                    self.rect.x += other.speed * other.direc 
                    self.logging = True

                if type (other) == Water and not self.logging:
                    self.die()

    # input
    def handleInput (self):
        # continually update the new state
        self.newkeystate = pygame.key.get_pressed()

        if self.Alive and not self.Winning:
            # left
            if get_keydown (self.oldkeystate, self.newkeystate, [pygame.K_LEFT, pygame.K_a]): 
                if self.rect.x > 0:
                    self.rect.x -= 64
                    self.playJumpSound()

            # right
            elif get_keydown (self.oldkeystate, self.newkeystate,[pygame.K_RIGHT, pygame.K_d]):
                if self.rect.x + 128 < pygame.display.get_surface().get_size()[0]:
                    self.rect.x += 64
                    self.playJumpSound()

            # down
            # TODO make downwards limit 
            if get_keydown (self.oldkeystate, self.newkeystate, [pygame.K_DOWN, pygame.K_s]):
                if (self.absolute_y >= pygame.display.get_surface().get_size()[1] / 2 - 64):    
                    self.level.change_pos_y(-64)
                else:
                    self.rect.y += 64

                self.absolute_y += 64
                self.playJumpSound()
            # up
            elif get_keydown (self.oldkeystate, self.newkeystate, [pygame.K_UP, pygame.K_w]):
                if (self.absolute_y > 0):          # prevent the player from moving off screen
                    if (self.absolute_y < pygame.display.get_surface().get_size()[1] / 2):     # prevent camera from panning off screen
                        self.rect.y -= 64
                    else:
                        self.level.change_pos_y(64)

                    self.absolute_y -= 64
                    self.playJumpSound()

            self.oldmousestate = self.newmousestate

            # exit the win screen
            if self.Winning:
                if self.newkeystate [pygame.K_SPACE]:
                    self.restart()        
        else:
            # exit the death screen
            if self.newkeystate [pygame.K_SPACE]:
                self.restart()       

        # update old state after making all the key checks
        self.oldkeystate = self.newkeystate

    # plays a random jump sound
    def playJumpSound (self):
        self.game.ResourceCache.Resources["se_jump_{0}".format(random.randint (1,4))].play()

    # called when the player touches a cave
    def win (self):
        self.game.ResourceCache.Resources["se_roundend"].play()
        self.Winning = True
        self.image = self.hideimg
        pygame.event.post (pygame.event.Event (WIN))

    # called when the level restarts
    def restart (self):
        self.rect.x = 64 * 8
        # only move the background if it has been moved
        if (self.absolute_y > pygame.display.get_surface().get_size()[1] / 2):  
            # offset by rounding to the nearest 64
            self.level.change_pos_y (self.absolute_y - math.ceil(pygame.display.get_surface().get_size()[1] / 128) * 64 + 64) 

        # reset positions
        self.rect.y = 0
        self.absolute_y = 0

        if (self.Winning):
            # remove a frog after moving one into the cave
            self.Frogs -= 1

        if (not self.Alive):
            # remove a life after dying
            self.Lives -= 1
            
        # reset player attributes
        self.Alive = True
        self.Winning = False
        self.image = self.aliveimg
        self.Scale (64,64)

        # broadcast event to the rest of the game
        pygame.event.post (pygame.event.Event (RESTART))
                
    # this method handles actual loss of the game
    def die (self):
        # play death sound
        self.game.ResourceCache.Resources["se_death"].play()

        # handle variables
        self.Alive = False
        self.image = self.deadimg
        self.Scale (64,64)

        # broadcast event to the rest of the game
        pygame.event.post (pygame.event.Event (DEATH))

    # this method handles pygame.kill() it removes this instance from all groups
    def kill(self):
        super().kill()

    def Scale (self, width, height):
        super().Scale(width, height)