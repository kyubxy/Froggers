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
    def __init__ (self, game):
        super().__init__(game)

        # check if the textures have been loaded
        if not "textures" in self.game.ResourceCache.LoadedDirectories:
            self.game.ResourceCache.LoadDirectory ("textures") 
        
        self.res = self.game.ResourceCache.Resources

        self.difficulty = 1

        # level
        self.level = Level (self.difficulty, self.game)
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

        # Game stats
        self.stats = GameStats ()

        # points counter
        self.pointscounter = SpriteText ("0", font = self.res["fnt_Berlin_24"])
        self.Add (self.pointscounter)

        # time display
        self.timeText = SpriteText ("0", font = self.res["fnt_Berlin_24"])
        self.timeText.rect.y = 40
        self.startTime = pygame.time.get_ticks()
        self.totalTime = 0
        self.Add (self.timeText)

        # level display
        self.levelText = SpriteText ("Level 1", font = self.res["fnt_Berlin_24"])
        self.Add (self.levelText)
        
    def Update (self):
        super().Update()

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
                    self.player.Frogs = 5

                    self.Remove (self.level)

                    self.level = Level (self.difficulty, self.game)
                    self.player.level = self.level

                    self.Add (self.level)
                    
                    self.move_to_front  (self.player)
                    self.move_to_front (self.msgtext)
                    self.move_to_front (self.pointscounter)
                    self.move_to_front (self.levelText)
                    self.move_to_front (self.timeText)

                    self.stats.Points += self.difficulty * 100

                self.msgtext.SetText ("")

                # account for the updated draw stack
                self.Remove (self.livesdisplay)
                self.Remove (self.frogsdisplay)
                self.livesdisplay.UpdateLives()
                self.frogsdisplay.UpdateFrogs()
                self.Add (self.livesdisplay)
                self.Add (self.frogsdisplay)

            if event.type == DEATH:
                self.msgtext.SetText ("You died, press the space key to continue")
                self.msgtext.rect.y = pygame.display.get_surface().get_size()[1] / 2 - self.msgtext.rect.height / 2

            if event.type == WIN:
                self.msgtext.SetText ("Nice work! press the space key to continue")
                self.msgtext.rect.y = pygame.display.get_surface().get_size()[1] / 2 - self.msgtext.rect.height / 2
                self.stats.Points += 100

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)