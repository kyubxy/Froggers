from Framework.Screen import *
from Framework.SpriteText import *
import Screens.GachaScreen 
from UI.FroggerButton import FroggerButton
import random

class GachaplayScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)

        self.Add (SpriteText("gachaplay"))

        # roll button
        self.RollButton = FroggerButton (self.game, self, "roll", clickEventName="roll")
        self.RollButton.set_Rect (pygame.Rect (10, 200, 200, 50))
        self.Add (self.RollButton)

        # back button
        self.BackButton = FroggerButton (self,game, self, "back", clickEventName="back")
        self.BackButton.set_Rect (pygame.Rect (10, 300, 200, 50))
        self.Add (self.BackButton)

        pygame.mixer.music.load ("res/bgm_gachaplay.mp3")
        pygame.mixer.music.play()

    def roll (self):
        e = random.randrange (0, 10)
        if (e == 1):
            print ("rolled a 5 star")
        elif (e == 2 or e == 3 or e == 4):
            print ("rolled a 4 star")
        else:
            print ("rolled 3 star")

    def back (self):
        self.game.ChangeScreen(Screens.GachaScreen.GachaScreen (self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)