from GameObjects.gacha.stickman import Stickman
import pygame
from Framework.Sprite import *

# TODO make a cutscene class that has dictionary and code

# container instance for the introductory fishing animation
class FishingAnimation (pygame.sprite.Group):
    def __init__(self, game):
        super().__init__()

        # window dimensions
        self.w, self.h = pygame.display.get_surface().get_size()

        # background
        self.background = Sprite ("img_gachabg", resources=game.ResourceCache.Resources)
        self.background.Scale (self.w, self.h)
        self.add (self.background)

        # foreground
        # dock
        self.dock = Sprite ("img_dock", resources=game.ResourceCache.Resources)
        self.dock.Scale (self.w, self.h)
        self.add (self.dock)

        # water
        self.water = Sprite ("img_fgwater", resources=game.ResourceCache.Resources)
        self.water.Scale (self.w, self.h)
        self.add (self.water)

        # stickman
        self.stickman = Stickman (game)
        self.stickman.change_pos ((700,285))
        self.add (self.stickman)

        # time gacha animation was started since beginning of runtime
        self.startTime = pygame.time.get_ticks ()

    def update(self):
        # time elpased since start of animation
        self.time = (pygame.time.get_ticks () - self.startTime) / 1000

        # update children
        self.stickman.update()

        # animation
        if self.time < 3.8:
            # approaching end of dock
            self.stickman.change_pos_x (1)
        elif self.time > 3.8 and self.time < 4:
            # reset arms
            self.stickman.arm1_angle = 15
            self.stickman.arm2_angle = -15
        elif self.time > 4 and self.time < 4.5:
            # moving arms to initial position and resetting legs
            self.stickman.arm1_angle += 0.5
            self.stickman.arm2_angle += 0.5
            self.stickman.leg1_angle = 15
            self.stickman.leg2_angle = -15
        elif self.time > 4.5 and self.time < 5:
            # hesitating arms 
            self.stickman.arm1_angle += 3
            self.stickman.arm2_angle += 3
        elif self.time > 5 and self.time < 5.2:
            # casting rod
            self.stickman.arm1_angle -= 5
            self.stickman.arm2_angle -= 5

# container instance for the gacha rolling animation
class WaterAnimation (pygame.sprite.Group):
    def __init__(self):
        pass