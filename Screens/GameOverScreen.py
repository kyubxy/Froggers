from Screen import *
from Screens.MainMenuScreen import *
import Screens.MainMenuScreen 
from Framework.KeyboardListener import *
from Stats import GameStats

class GameOverScreen (Screen):
    def __init__ (self, game, stats):
        super().__init__(game)
        self.stats = stats
        self.deathtext = SpriteText("GAME OVER")
        self.deathtext.SetColour ([255,0,0])
        self.Add (self.deathtext)

        self.messages = [
            "RESULTS",
            "Points: " + str(stats.Points), 
            "Time: " + str (stats.Time/1000) + " seconds",
            "",
            "Press space to continue...",
            ]

        for msg in range(len(self.messages)):
            self.msgtxt = SpriteText (self.messages[msg], 30)
            self.msgtxt.rect.y = 100 + 30 * msg
            self.add (self.msgtxt)

        self.oldstate = pygame.key.get_pressed()
        self.newstate = pygame.key.get_pressed()

    def Update (self):
        super().Update()

        self.newstate = pygame.key.get_pressed()

        if self.newstate [pygame.K_SPACE] and not self.oldstate [pygame.K_SPACE]:
            self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))

        self.oldstate = self.newstate 

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)