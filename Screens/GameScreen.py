from Framework.Screen import *
from Framework.SpriteText import *
from GameObjects.Level import *
from GameObjects.Entities.Player import *
from UI.LivesDisplay import *
from UI.FrogDisplay import *
from Screens.GameOverScreen import *
from constants import *
from Stats import GameStats

class GameScreen (Screen):
    def __init__ (self, game, seeds = None):
        super().__init__(game)

        # check if the textures have been loaded
        if not "textures" in self.game.ResourceCache.LoadedDirectories:
            self.game.ResourceCache.LoadDirectory ("textures") 
        
        self.res = self.game.ResourceCache.Resources

        pygame.mixer.music.load ("res/bgm/bgm_gameplay.mp3")
        pygame.mixer.music.play()

        self.difficulty = 1

        # Game stats
        self.stats = GameStats ()

        # seeds (if available)
        if seeds is None:
            self.seeded = False
            print ("this level is not seeded")
        else:
            if (len(seeds) > 0):
                self.seeds = seeds
                self.seeded = True
            
                print ("this level is seeded, it's seeds consist of", self.seeds)
            else:
                self.seeded = False
                print ("this level is not seeded")

        # level
        self.level = Level (self.difficulty, self.game, self.stats)

        if self.seeded:
            self.level.generate (self.seeds[0])
        else:
            self.level.generate ()

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
        self.Add (self.pointscounter)

        # time display
        self.timeText = SpriteText ("0", font = self.res["fnt_Berlin_24"])
        self.timeText.rect.y = 40
        self.startTime = pygame.time.get_ticks()
        self.totalTime = 0
        self.Add (self.timeText)

        # level display
        self.levelText = SpriteText ("Level 1", font = self.res["fnt_Berlin_24"])
        self.levelText.Background = [0,0,0]
        self.Add (self.levelText)

        # empty surface
        self.emptysurf = pygame.Surface ((1,1))
        
        # time taken to get one frog from start to finish
        self.runTime = 0
        self.runStart = self.startTime

        # time taken to clear the level
        self.levelTime = 0
        self.levelStart = self.startTime

    def Update (self):
        super().Update()

        self.runTime = pygame.time.get_ticks() - self.runStart
        self.levelTime = pygame.time.get_ticks() - self.levelStart

        self.totalTime = pygame.time.get_ticks() - self.startTime
        self.timeText.SetText (str(round (self.totalTime / 1000)) + "/sec")
        self.timeText.rect.x = pygame.display.get_surface().get_size()[0] - self.timeText.image.get_size()[0]
        self.stats.Time = self.totalTime

        self.levelText.SetText ("Level " + str(self.difficulty))
        self.levelText.rect.y = pygame.display.get_surface().get_size()[1] - self.levelText.image.get_size()[1]
        
        self.pointscounter.SetText (str(self.stats.Points))
        self.pointscounter.rect.x = pygame.display.get_surface().get_size()[0] - self.pointscounter.image.get_size()[0]
        
        self.level.Update()

        for event in pygame.event.get():
            if (event.type == RESTART):
                # game over
                if self.player.Lives == -1:
                    self.game.ChangeScreen (GameOverScreen (self.game, self.stats))

                # next stage
                if self.player.Frogs == 0:
                    self.difficulty += 1
                    self.player.Frogs = FROGS

                    self.stats.Points += round (1000000000 / self.levelTime + self.difficulty * 40000)
                    self.stats.leveltimes.append (self.levelTime)

                    self.levelTime = 0
                    self.levelStart = pygame.time.get_ticks()

                    if self.difficulty % 2 == 0 and self.player.Lives < 7:
                        self.player.Lives += 1

                    self.Remove (self.level)

                    self.level = Level (self.difficulty, self.game, self.stats)
                    self.player.level = self.level
                    if self.seeded:
                        if self.difficulty <= (len (self.seeds)):
                            self.level.generate (self.seeds[self.difficulty - 1])
                            print ("this level is still seeded")
                        else:
                            self.seeded = False
                            self.level.generate ()
                            print ("this level is no longer seeded")
                    else:
                        self.level.generate()

                    self.Add (self.level)
                    
                    self.move_to_front  (self.player)
                    self.move_to_front (self.msgtext)
                    self.move_to_front (self.pointscounter)
                    self.move_to_front (self.levelText)
                    self.move_to_front (self.timeText)

                self.msgtext.image = self.emptysurf

                # account for the updated draw stack
                self.Remove (self.livesdisplay)
                self.Remove (self.frogsdisplay)
                self.livesdisplay.UpdateLives()
                self.frogsdisplay.UpdateFrogs()
                self.Add (self.livesdisplay)
                self.Add (self.frogsdisplay)


            if event.type == DEATH:
                self.msgtext.SetText ("You died, press the space key to continue")
                self.msgtext.rect.x = pygame.display.get_surface().get_size()[0] / 2 - self.msgtext.image.get_size()[0] / 2
                self.msgtext.rect.y = pygame.display.get_surface().get_size()[1] / 2 - self.msgtext.image.get_size()[1] / 2

            if event.type == WIN:
                self.msgtext.SetText ("Nice work! press the space key to continue")
                self.msgtext.rect.x = pygame.display.get_surface().get_size()[0] / 2 - self.msgtext.image.get_size()[0] / 2
                self.msgtext.rect.y = pygame.display.get_surface().get_size()[1] / 2 - self.msgtext.image.get_size()[1] / 2
                self.stats.Points += round (10000000 / self.runTime + self.difficulty * 100)
                self.stats.runtimes.append (self.runTime)

                self.runTime = 0
                self.runStart = pygame.time.get_ticks()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)