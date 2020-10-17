from Framework.Screen import *
from Framework.SpriteText import *
from Framework.UI.Button import Button
import Screens.GachaScreen 

class GachaplayScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)

        self.Add (SpriteText("gachaplay"))

        # roll button
        self.RollButton = Button (self, "roll", clickEventName="roll")
        self.RollButton.set_Rect (pygame.Rect (10, 200, 200, 50))
        self.Add (self.RollButton)

        # back button
        self.BackButton = Button (self, "back", clickEventName="back")
        self.BackButton.set_Rect (pygame.Rect (10, 300, 200, 50))
        self.Add (self.BackButton)

    def roll (self):
        print ("rolled 0 star")

    def back (self):
        self.game.ChangeScreen(Screens.GachaScreen.GachaScreen (self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)