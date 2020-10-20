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
        
        self.difficulty = 1

        # level
        self.level = Level (self.difficulty)
        self.Add (self.level)

        # player
        self.player = Player(self.level)
        self.Add (self.player)

        # message text
        self.msgtext = SpriteText("", 40)
        self.msgtext.Background = [0,0,0]
        self.Add (self.msgtext)

        # lives display
        self.livesdisplay = LivesDisplay (self.player)
        self.Add (self.livesdisplay)

        # frogs display
        self.frogsdisplay = FrogDisplay (self.player)
        self.Add (self.frogsdisplay)

        # Game stats
        self.stats = GameStats ()

        # points counter
        self.pointscounter = SpriteText ("0")
        self.Add (self.pointscounter)

    def Update (self):
        super().Update()

        self.pointscounter.SetText (str(self.stats.Points))

        self.level.Update()

        for event in pygame.event.get():
            if (event.type == RESTART):
                # game over
                if self.player.Lives == -1:
                    self.game.ChangeScreen (GameOverScreen (self.game))

                # next stage
                if self.player.Frogs == 0:
                    self.difficulty += 1
                    self.player.Frogs = 5

                    self.Remove (self.level)

                    self.level = Level (self.difficulty)
                    self.player.level = self.level

                    self.Add (self.level)
                    
                    self.move_to_front  (self.player)
                    self.move_to_front (self.msgtext)
                    self.move_to_front (self.pointscounter)

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