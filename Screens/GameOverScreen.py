from Screen import *
from Screens.MainMenuScreen import *
import Screens.MainMenuScreen 
from Framework.KeyboardListener import *

class GameOverScreen (Screen, KeyboardListener):
    def __init__ (self, game):
        super().__init__(game)
        self.deathtext = SpriteText("GAME OVER, press space bar to continue")
        self.deathtext.SetColour ([255,0,0])
        self.Add (self.deathtext)

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