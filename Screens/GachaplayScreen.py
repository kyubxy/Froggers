from Framework.Screen import *
from Framework.SpriteText import *
from Framework.Sprite import *
from UI.FroggerButton import FroggerButton
import Screens.GachaScreen 

class GachaplayScreen (Screen):
    def __init__ (self, game, rolls):
        super().__init__(game)

        game.ResourceCache.LoadDirectory ("textures")

        self.rolls = rolls
        self.Add (SpriteText("gachaplay"))

        # roll button
        self.RollButton = FroggerButton (game, self, "roll", clickEventName="roll")
        self.RollButton.set_Rect (pygame.Rect (10, 200, 200, 50))
        self.Add (self.RollButton)

        # back button
        self.BackButton = FroggerButton (game, self, "back", clickEventName="back")
        self.BackButton.set_Rect (pygame.Rect (10, 300, 200, 50))
        self.Add (self.BackButton)

        # play bgm
        pygame.mixer.music.load ("res/bgm/bgm_gachaplay.mp3")
        pygame.mixer.music.play()

    def generate_frogs(self, no):
        frogs = []
        for i in range (no):
            frogs.append ()

        return frogs

    def roll (self):
        pass

    def back (self):
        self.game.ChangeScreen(Screens.GachaScreen.GachaScreen (self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)