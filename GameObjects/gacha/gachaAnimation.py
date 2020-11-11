import pygame
import logging
from Framework.Shapes.Box import Box
from Framework.Shapes.Circle import Circle
from Framework.Sprite import *
from Framework.SpriteText import *
from Framework.GeometricGroup import GeometricGroup
from Framework.MouseListener import MouseListener
from GameObjects.gacha.stickman import Stickman

# container instance for the introductory fishing animation
class IntroductionAnimation (pygame.sprite.Group):
    def __init__(self, game):
        super().__init__()

        # window dimensions
        self.w, self.h = pygame.display.get_surface().get_size()

        # background
        self.background = Sprite ("img_bg", resources=game.ResourceCache.Resources)
        self.background.Scale (self.w, self.h)
        self.add (self.background)

        # foreground
        # dock
        self.dock = Sprite ("img_dock", resources=game.ResourceCache.Resources)
        self.dock.Scale (self.w, self.h)
        self.add (self.dock)

        # stickman
        self.stickman = Stickman (game)
        self.stickman.change_pos ((700,285))
        self.add (self.stickman)

        # water
        self.water = Sprite ("img_fgwater", resources=game.ResourceCache.Resources)
        self.water.Scale (self.w, self.h)
        self.add (self.water)

        # time gacha animation was started since beginning of runtime
        self.startTime = pygame.time.get_ticks ()

        # whether or not the animation is finished
        self.playing = True

    def play(self, parent):
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
            self.playing = False
            parent.Roll()

        return self.playing

# container instance for the gacha rolling animation
class FishingAnimation (pygame.sprite.LayeredUpdates, MouseListener):
    def __init__(self, game, parent):
        super().__init__()
         
        self.game = game
        self.res = self.game.ResourceCache.Resources        
        self.parent = parent

        # constants
        self.CIRCLE_RADIUS = 500
        self.SQUARE_SIZE = 250
        self.COL_SQUARE_SIZE  = 75
        self.RARITY_4_COL = [96, 123, 230]
        self.RARITY_5_COL = [230, 220, 110]

        # window dimensions
        self.w, self.h = pygame.display.get_surface().get_size()
        self.center = (self.w - self.w // 2, self.h - self.h // 2)

    def Start (self, card):
        self.empty ()

        # background
        self.bg_tex = pygame.Surface ((self.w,self.h))
        self.bg_tex.fill ([87, 151, 255])
        self.background = Sprite (img=self.bg_tex)
        self.background.Scale (self.w, self.h)
        self.add (self.background)

        # main circle piece
        self.circle_piece = Circle (self.center[0] - self.CIRCLE_RADIUS, self.center[1] - self.CIRCLE_RADIUS, self.CIRCLE_RADIUS, 30)
        self.add (self.circle_piece)

        # other circle piece
        self.aux_circle_piece = Circle (self.center[0] - self.CIRCLE_RADIUS, self.center[1] - self.CIRCLE_RADIUS, self.CIRCLE_RADIUS, 15)
        self.add (self.aux_circle_piece)

        # squares
        self.coloured_square = Box (pygame.Rect (self.center[0] - self.COL_SQUARE_SIZE  // 2, self.center[1] - self.COL_SQUARE_SIZE  // 2, self.COL_SQUARE_SIZE , self.COL_SQUARE_SIZE))

        self.square1 = Box (pygame.Rect (self.center[0] - self.SQUARE_SIZE // 2, self.center[1] - self.SQUARE_SIZE // 2, self.SQUARE_SIZE, self.SQUARE_SIZE), 25)
        self.square2 = Box (pygame.Rect (self.center[0] - self.SQUARE_SIZE // 2, self.center[1] - self.SQUARE_SIZE // 2, self.SQUARE_SIZE, self.SQUARE_SIZE), 25)
        self.square3 = Box (pygame.Rect (self.center[0] - self.SQUARE_SIZE // 2, self.center[1] - self.SQUARE_SIZE // 2, self.SQUARE_SIZE, self.SQUARE_SIZE), 25)

        # whether or not the animation is finished
        self.finished = False
        self.animating = True

        self.aux_offset = 0
        self.auxrad = 0
        self.aux_accel_offset = 0
        
        # Card (information)
        self.card = card
        self.rarity = int(self.card.meta["rarity"])
        self.raritycounter = 1

        # Card (sprite)
        self.add (self.card)
        self.card.Scale (200,200)
        self.card.rect.center = self.center
        self.move_to_front (self.card)
        self.card.Hide()

        # Card text
        self.card_name_text = SpriteText (self.card.meta["name"], font = self.res["fnt_Berlin_48"], Background=[64,64,64])
        self.card_name_text.rect.centerx = self.center[0]
        self.card_name_text.rect.centery = self.h - 200
        self.add (self.card_name_text)
        self.card_name_text.Hide()
        self.move_to_front (self.card_name_text)

        # Card stars
        self.stars = GeometricGroup ()
        for star in range (self.rarity):    # add stars
            star_sprite = Sprite ("img_star", resources=self.res)
            star_sprite.rect.x += star * 200
            star_sprite.rect.y = self.h - star_sprite.rect.height
            self.stars.add (star_sprite)  
        self.add (self.stars)
        self.stars.change_pos_y (self.h + 800)
        
        # time gacha animation was started from reset since beginning of runtime
        self.startTime = pygame.time.get_ticks ()

        # SQUARES
        # single square in the middle which changes colour depending on card rarity
        self.add (self.coloured_square)
        # rotating squares
        self.add (self.square1)
        self.add (self.square2)
        self.add (self.square3)

        # move everything to back
        self.move_to_back (self.square1)
        self.move_to_back (self.square2)
        self.move_to_back (self.square3)
        self.move_to_back (self.background)
        
        # initialise rotation
        self.square1.Rotate (0)
        self.square2.Rotate (0)
        self.square3.Rotate (0)
        
        self.wow = self.res["se_wow"]

    def play(self):
        # time elpased since start of animation
        self.time = (pygame.time.get_ticks () - self.startTime) / 500

        if self.animating:
            # NOTE: all transformations have an acceleration 

            # rotate squares
            self.square1.Rotate (20 * self.time ** 2)
            self.square2.Rotate (25 * self.time ** 2)
            self.square3.Rotate (30 * self.time ** 2) 

            # make the main circle grow larger
            self.circle_piece.Scale (self.CIRCLE_RADIUS + 10 * self.time ** 2, self.CIRCLE_RADIUS + 10 * self.time ** 2)
            self.circle_piece.rect.center = self.center

        # ensure the auxilary circle snaps back to the size of the main circle after scaling out of the screen
        self.auxrad = self.circle_piece.rect.width + (400 + self.aux_accel_offset) * (self.time - self.aux_offset) ** 2
        self.aux_circle_piece.Scale (self.auxrad, self.auxrad)
        self.aux_circle_piece.rect.center = self.center

        # snap the auxilary circle back
        if self.aux_circle_piece.rect.width - self.CIRCLE_RADIUS > self.w:
            self.aux_offset = self.time
            if self.animating:
                self.aux_accel_offset += 600

            self.raritycounter += 1

            # change rarity square's colour
            if self.raritycounter == 3:
                self.coloured_square.image.fill (self.RARITY_4_COL)
            elif (self.raritycounter == 4):
                self.coloured_square.image.fill (self.RARITY_5_COL)
                
            # show the card after the rarity has been revelaed
            if self.raritycounter == self.rarity:
                self.animating = False
                self.card.Show()
                self.card.Scale (180,180)
                self.card.rect.center = self.center
                self.card_name_text.Show()
                self.coloured_square.Hide()

                # play a special sound effect for good cards
                if self.rarity > 3:
                    self.wow.play()
                self.move_to_front (self.card_name_text)    
            elif (self.raritycounter == self.rarity + 1):
                self.stars.change_pos_y (-(self.h + 800))
                logging.info ("rolled {0}".format (self.card.meta))
            
        # continue rolling
        if pygame.mouse.get_pressed()[0] and self.raritycounter >= self.rarity + 1:
                self.parent.Roll()