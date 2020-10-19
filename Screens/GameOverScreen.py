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

    def Update (self):
        super().Update()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)