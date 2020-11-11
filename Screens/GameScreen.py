from Framework.Screen import *
from Framework.SpriteText import *
from GameObjects.Level import *
from GameObjects.Entities.Player import *
from UI.LivesDisplay import *
from UI.FrogDisplay import *
from Screens.GameOverScreen import *
from constants import *
from Stats import GameStats
from UI.PauseMenu import *
from Framework.KeyboardListener import get_keydown
import pygame

# TODO: add UI to foreground group

class GameScreen (Screen):        
    def __init__ (self, game, seeds = None):
        pygame.mouse.set_visible (False)
        super().__init__(game, "res/bgm/bgm_gameplay.mp3")
        
        self.res = self.game.ResourceCache.Resources

        # set starting difficulty
        self.difficulty = 1

        # Game stats
        self.stats = GameStats ()

        # assign seeds (if available)
        if seeds is None:
            self.seeded = False
            logging.info ("this level is not seeded")
        else:
            if (len(seeds) > 0):
                self.seeds = seeds
                self.seeded = True
            
                logging.info ("this level is seeded, it's seeds consist of {0}".format(self.seeds))
            else:
                self.seeded = False
                logging.info ("this level is not seeded")

        # level
        self.level = Level (difficulty = self.difficulty, game = self.game, stats = self.stats)

        # generate level
        if self.seeded:
            self.level.generate (self.seeds[0])
        else:
            self.level.generate ()  

        # add level
        self.Add (self.level)

        # player
        self.player = Player(self.level, self.game)
        self.Add (self.player)

        # message text
        self.msgtext = SpriteText("", font = self.res["fnt_VanillaExtract_40"])
        self.msgtext.Background = [0,0,0]
        self.Add (self.msgtext)

        # lives display
        self.livesdisplay = LivesDisplay (self.player, self.game)
        self.Add (self.livesdisplay)

        # frogs display
        self.frogsdisplay = FrogDisplay (self.player, self.game)
        self.Add (self.frogsdisplay)

        # points counter
        self.pointscounter = SpriteText ("0", font = self.res["fnt_Berlin_48"])
        self.pointscounter.rect.centerx = pygame.display.get_surface().get_size()[0] // 2
        self.Add (self.pointscounter)

        # time display
        self.timeText = SpriteText ("0", font = self.res["fnt_Berlin_24"])
        self.timeText.rect.centerx = pygame.display.get_surface().get_size()[0] // 2
        self.timeText.rect.y = 40
        self.startTime = pygame.time.get_ticks()
        self.totalTime = 0
        self.Add (self.timeText)

        # level display
        self.levelText = SpriteText ("Level 1", font = self.res["fnt_Berlin_24"])
        self.levelText.Background = [0,0,0]
        self.levelText.rect.y = pygame.display.get_surface().get_size()[1] - self.levelText.image.get_size()[1]
        self.Add (self.levelText)

        # empty surface
        self.emptysurf = pygame.Surface ((1,1))
        
        # time taken to get one frog from start to finish
        self.runTime = 0
        self.runStart = self.startTime

        # time taken to clear the level
        self.levelTime = 0
        self.levelStart = self.startTime

        # pause menu
        self.Paused = False
        self.pauseMenu = PauseMenu (self.game, self, pygame.Rect (30,30,pygame.display.get_surface().get_size()[0] - 60,pygame.display.get_surface().get_size()[1] - 60))
        self.pauseMenu.Disable()
        self.foreground = pygame.sprite.Group()
        self.foreground.add (self.pauseMenu)
        self.Add (self.foreground)

        self.oldstate = pygame.key.get_pressed()
        self.newstate = pygame.key.get_pressed()

        self.pausetime = 0

    def Update (self):
        self.newstate = pygame.key.get_pressed()
        self.pauseMenu.Update()
        if not self.Paused:
            # UNPAUSED
            super().Update()
            if self.pauseMenu.Enabled:
                self.pauseMenu.Disable()

            pygame.mouse.set_visible (False)

            # update time
            self.runTime = pygame.time.get_ticks() - self.runStart
            self.levelTime = pygame.time.get_ticks() - self.levelStart

            # total time (displayed on the screen)
            self.totalTime = pygame.time.get_ticks() - self.startTime - self.pausetime
            self.timeText.SetText (str(round (self.totalTime / 1000)) + "/sec")
            self.timeText.rect.centerx = pygame.display.get_surface().get_size()[0] // 2
            self.stats.Time = self.totalTime
            
            # update level
            self.level.Update()

            # handle game events
            for event in pygame.event.get():
                if (event.type == RESTART):
                    # game over
                    if self.player.Lives == -1:
                        self.game.ChangeScreen (GameOverScreen (self.game, self.stats))

                    # next stage
                    if self.player.Frogs == 0:
                        
                        # increase difficulty
                        self.difficulty += 1

                        # update level text
                        self.levelText.SetText ("Level " + str(self.difficulty))

                        # reset frogs
                        self.player.Frogs = Player.frogs

                        # give points
                        self.stats.Points += round (1000000000 / self.levelTime + self.difficulty * 40000)
                        self.stats.leveltimes.append (self.levelTime)

                        # reset time
                        self.levelTime = 0
                        self.levelStart = pygame.time.get_ticks()

                        # award lives, max 7
                        if self.difficulty % 2 == 0 and self.player.Lives < 7 and self.difficulty > 2:
                            self.player.Lives += 1

                        # regenerate level
                        self.Remove (self.level)    # remove level from group temporarily

                        # generate new level
                        self.level = Level (difficulty = self.difficulty, game = self.game, stats = self.stats)
                        self.player.level = self.level
                        # use seeds
                        if self.seeded:
                            # check if there are still seeds
                            if self.difficulty <= (len (self.seeds)):
                                self.level.generate (self.seeds[self.difficulty - 1])
                                logging.info ("this level is still seeded")
                            else:   # otherwise, stop seeding the levels
                                self.seeded = False
                                self.level.generate ()
                                logging.info ("this level is no longer seeded")
                        else:
                            self.level.generate()

                        # re-add the level
                        self.Add (self.level)
                        
                        # move all UI to the front again
                        self.move_to_front  (self.player)
                        self.move_to_front (self.msgtext)
                        self.move_to_front (self.pointscounter)
                        self.move_to_front (self.levelText)
                        self.move_to_front (self.timeText)
                        self.Remove (self.foreground)
                        self.Add (self.foreground)

                    # clear msg text
                    self.msgtext.image = self.emptysurf

                    # update displays
                    self.Remove (self.livesdisplay)
                    self.Remove (self.frogsdisplay)
                    self.livesdisplay.UpdateLives()
                    self.frogsdisplay.UpdateFrogs()
                    self.Add (self.livesdisplay)
                    self.Add (self.frogsdisplay)

                if event.type == DEATH:
                    # show msg text
                    self.msgtext.SetText ("You died, press the space key to continue")
                    self.msgtext.rect.x = pygame.display.get_surface().get_size()[0] / 2 - self.msgtext.image.get_size()[0] / 2
                    self.msgtext.rect.y = pygame.display.get_surface().get_size()[1] / 2 - self.msgtext.image.get_size()[1] / 2

                if event.type == WIN:
                    # show msg text
                    self.msgtext.SetText ("Nice work! press the space key to continue")
                    self.msgtext.rect.x = pygame.display.get_surface().get_size()[0] / 2 - self.msgtext.image.get_size()[0] / 2
                    self.msgtext.rect.y = pygame.display.get_surface().get_size()[1] / 2 - self.msgtext.image.get_size()[1] / 2
                    
                    # award points
                    self.stats.Points += round (10000000 / self.runTime + self.difficulty * 100)
                    self.stats.runtimes.append (self.runTime)
            
                    # update points text
                    self.pointscounter.SetText (str(self.stats.Points))
                    self.pointscounter.rect.centerx = pygame.display.get_surface().get_size()[0] // 2

                    self.runTime = 0
                    self.runStart = pygame.time.get_ticks()
        else:
            # PAUSED
            if not self.pauseMenu.Enabled:
                self.pauseMenu.Enable()        
                pygame.mouse.set_visible (True)
                #TODO self.pausetime = pygame.time.get_ticks() - self.startTime

        if get_keydown (self.oldstate, self.newstate, [pygame.K_ESCAPE]):
            self.Paused = not self.Paused

        self.oldstate = self.newstate

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)