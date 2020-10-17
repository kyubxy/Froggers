from Framework.Screen import *
from Framework.SpriteText import *
from Framework.UI.Button import Button
import Screens.MainMenuScreen
from GameObjects.Level import *

class GameScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)
        
        self.level = Level (30)
        self.Add (self.level)

    # leave to main menu
    def Leave (self):
        self.game.ChangeScreen(Screens.MainMenuScreen.MainMenuScreen(self.game))

    def Update (self):
        super().Update()

        keys = pygame.key.get_pressed ()
        if keys[pygame.K_UP]:
            self.level.Position = -10 
        elif keys[pygame.K_DOWN]:
            self.level.Position = 10 
        else:
            self.level.Position = 0

        self.level.Update()
        

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)