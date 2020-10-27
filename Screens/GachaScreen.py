from Framework.Screen import *
from Framework.SpriteText import *
from UI.FroggerButton import FroggerButton
import Screens.MainMenuScreen
from Screens.GachaplayScreen import *

class GachaScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)

        self.Add (SpriteText("gacha"))

        # 1 pull
        self.pull1 = FroggerButton (self.game, self, "Roll, 60 coins", clickEventName="Gacha1")
        self.pull1.set_Rect (pygame.Rect (10, 200, 200, 50))
        self.Add (self.pull1)

        # 10 pull
        self.pull10 = FroggerButton (self.game, self, "Roll 10, 400 coins", clickEventName="Gacha10")
        self.pull10.set_Rect (pygame.Rect (10, 300, 200, 50))
        self.Add (self.pull10)

        # back button
        self.BackButton = FroggerButton (self.game, self, "back", clickEventName="back")
        self.BackButton.set_Rect (pygame.Rect (10, 400, 200, 50))
        self.Add (self.BackButton)

    def Gacha1 (self):
        self.game.ChangeScreen(GachaplayScreen (self.game, 1))

    def Gacha10 (self):
        self.game.ChangeScreen(GachaplayScreen (self.game, 10))

    def back (self):
        self.game.ChangeScreen(Screens.MainMenuScreen.MainMenuScreen(self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)