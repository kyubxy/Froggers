from Framework.Sprite import Sprite
from Framework.GeometricGroup import *
import pygame
import math

class Stickman (GeometricGroup):
    def __init__(self, game):
        super().__init__ ()

        self.game = game
        self.res = game.ResourceCache.Resources # resource cache (for local use)
        
        # BODY PARTS
        # head
        self.head = Sprite ("img_stickmanhead", resources=self.res)
        self.head.Scale (32,32)
        self.head.rect.x = 16
        self.Add (self.head)

        # body
        self.body = Sprite ("img_linefull", resources=self.res)
        self.body.Scale (32,60)
        self.body.rect.y = 32
        self.body.rect.x = 16
        self.Add (self.body)

        # legs
        self.leg1 = Sprite ("img_limb", resources=self.res)
        self.leg1_angle = 15
        self.leg1.Rotate (self.leg1_angle)
        self.leg1.rect.y = 20
        self.leg1.rect.x = 1
        self.Add (self.leg1)

        self.leg2 = Sprite ("img_limb", resources=self.res)
        self.leg2_angle = -15
        self.leg2.Rotate (-15)
        self.leg2.rect.y = 20
        self.leg2.rect.x = 1
        self.Add (self.leg2)

        # arms
        self.arm1 = Sprite ("img_limb", resources=self.res)
        self.arm1_angle = 15
        self.arm1.Rotate (self.leg1_angle)
        self.arm1.rect.y = -20
        self.arm1.rect.x = 1
        self.Add (self.arm1)

        self.arm2 = Sprite ("img_limb", resources=self.res)
        self.arm2_angle = -15
        self.arm2.Rotate (-15)
        self.arm2.rect.y = -20
        self.arm2.rect.x = 1
        self.Add (self.arm2)

        # rod
        self.rod = Rod (self.game, self)
        self.rod.change_pos((-40,-80))
        self.Add (self.rod)

        # OTHER VARIABLES

        # whether or not to play the walking animation
        self.walking = False

        self.timer = 0

    def update (self):
        self.timer = pygame.time.get_ticks() / 20

        # update rod
        self.rod.update()

        # walking animation
        if self.walking:
            # LEGS
            # angle of legs for character's stride. the angle oscillates so a sin function is used
            self.leg1_angle = 20*math.sin (0.1 * self.timer)        
            self.leg2_angle = -20*math.sin (0.1 * self.timer) 

            # ARMS
            # angle of arms for character's stride. the angle oscillates so a sin function is used
            self.arm1_angle = 20*math.sin (0.1 * (self.timer - 20))        
            self.arm2_angle = -20*math.sin (0.1 * (self.timer - 20)) # introduce phase shift so arms are out of sync with legs
            
        self.walking = False
        
        # update limbs
        self.leg1.Rotate (self.leg1_angle)
        self.leg2.Rotate (self.leg2_angle)
        self.arm1.Rotate (self.arm1_angle)
        self.arm2.Rotate (self.arm2_angle)
        # update the rod as well
        self.rod.rod.Rotate (self.arm1_angle - 90)

    def change_pos_x (self, speed):
        self.walking = True
        super().change_pos_x (speed)

    def change_pos_y (self, speed):
        super().change_pos_y (speed)

class Rod (GeometricGroup):
    def __init__(self, game, stickman):
        super().__init__ ()

        self.game = game
        self.res = self.game.ResourceCache.Resources
        self.stickman = stickman

        # rod
        self.rod = Sprite ("img_rod", resources=self.res)
        self.add (self.rod)

        # line
        self.line = Sprite (img = pygame.Surface ((0,32)))
        self.add (self.line)

        self.casting = False

        self.t = 0

    def update (self):
        self.line.rect.x = self.rod.rect.x + 220
        self.line.rect.y = self.rod.rect.y + 70
        if self.casting:
            self.t += 1
            self.line.Scale (2, 32 + 5 * self.t)
