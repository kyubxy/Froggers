from Framework.Shapes.Circle import Circle
from Framework.Shapes.Box import Box
from Framework.Sprite import *
from GameObjects.gacha.stickman import Stickman
import pygame

# TODO make a cutscene class that has dictionary and code

# container instance for the introductory fishing animation
class IntroductionAnimation (pygame.sprite.Group):
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

        # whether or not the animation is finished
        self.finished = False

    def play(self):
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
            # BEGIN CASTING
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
        elif self.time > 5.2 and self.time < 8:
            # make the line go down
            self.stickman.rod.casting = True
        elif self.time > 8:
            # make the line stop going down and declare the animation finished
            self.stickman.rod.casting = False
            self.finished = True

        return self.finished

# TODO
# make fishing animation a sprite
# add all "children" to a private rendergroup
# have the render group draw to the sprite's image
# manipulate the sprite image for zooming (etc)

# ALSO FADING !

# container instance for the gacha rolling animation
class FishingAnimation (pygame.sprite.RenderPlain):
    def __init__(self, game):
        super().__init__()

        # constants
        self.CIRCLE_RADIUS = 300
        self.SQUARE_SIZE = 250
        self.COL_SQUARE_SIZE  = 75

        # window dimensions
        self.w, self.h = pygame.display.get_surface().get_size()
        self.center = (self.w - self.w // 2, self.h - self.h // 2)

        # background
        self.bg_tex = pygame.Surface ((self.w,self.h))
        self.bg_tex.fill ([87, 151, 255])
        self.background = Sprite (img=self.bg_tex)
        self.background.Scale (self.w, self.h)
        self.add (self.background)

        # main circle piece
        self.circle_piece = Circle (self.center[0] - self.CIRCLE_RADIUS, self.center[1] - self.CIRCLE_RADIUS, self.CIRCLE_RADIUS, 15)
        self.add (self.circle_piece)

        # squares
        self.coloured_square = Box (pygame.Rect (self.center[0] - self.COL_SQUARE_SIZE  // 2, self.center[1] - self.COL_SQUARE_SIZE  // 2, self.COL_SQUARE_SIZE , self.COL_SQUARE_SIZE ))

        self.square1 = Box (pygame.Rect (self.center[0] - self.SQUARE_SIZE // 2, self.center[1] - self.SQUARE_SIZE // 2, self.SQUARE_SIZE, self.SQUARE_SIZE), 25)
        self.square2 = Box (pygame.Rect (self.center[0] - self.SQUARE_SIZE // 2, self.center[1] - self.SQUARE_SIZE // 2, self.SQUARE_SIZE, self.SQUARE_SIZE), 25)
        self.square3 = Box (pygame.Rect (self.center[0] - self.SQUARE_SIZE // 2, self.center[1] - self.SQUARE_SIZE // 2, self.SQUARE_SIZE, self.SQUARE_SIZE), 25)

        # whether or not the animation is finished
        self.finished = False

    def play(self):
        # time elpased since start of animation
        self.time = (pygame.time.get_ticks () - self.startTime) / 1000

        self.square1.Rotate (10 * self.time ** 2)
        self.square2.Rotate (15 * self.time ** 2)
        self.square3.Rotate (20 * self.time ** 2)

        self.draw ()

    def reset (self):        
        # time gacha animation was started from reset since beginning of runtime
        self.startTime = pygame.time.get_ticks ()

        self.add (self.coloured_square)
        self.add (self.square1)
        self.add (self.square2)
        self.add (self.square3)
        
        self.square1.Rotate (0)
        self.square2.Rotate (0)
        self.square3.Rotate (0)