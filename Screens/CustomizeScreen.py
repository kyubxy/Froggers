from Framework.Screen import *
from Framework.SpriteText import *
from Framework.UI.Button import Button
import Screens.MainMenuScreen
from Screens.GachaplayScreen import *

class CustomizeScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)

        self.Add (SpriteText("customize"))

        # back button
        self.BackButton = Button (self, "back", clickEventName="back")
        self.BackButton.set_Rect (pygame.Rect (10, 300, 200, 50))
        self.Add (self.BackButton)
    def back (self):
        self.game.ChangeScreen(Screens.MainMenuScreen.MainMenuScreen(self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)