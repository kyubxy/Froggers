from pickle import FALSE
from Framework.Screen import *
from Framework.SpriteText import *
from UI.FroggerButton import FroggerButton
import Screens.MainMenuScreen
from Screens.GachaplayScreen import *
from Screens.BuyCoinScreen import *

class GachaScreen (Screen):
    def __init__ (self, game):
        super().__init__(game) 

        self.bg = Sprite ("img_bg", resources=self.game.ResourceCache.Resources)
        self.bg.Scale (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1])
        self.add (self.bg)

        self.Add (SpriteText("fishing", font=game.ResourceCache.Resources["fnt_VanillaExtract_48"]))

        # 1 pull
        self.pull1 = FroggerButton (self.game, self, "Fish, 250 coins", clickEventName="Gacha1")
        self.pull1.set_Rect (pygame.Rect (10, 200, 200, 50))
        self.Add (self.pull1)

        # 10 pull
        self.pull10 = FroggerButton (self.game, self, "Fish 10, 2000 coins", clickEventName="Gacha10")
        self.pull10.set_Rect (pygame.Rect (10, 300, 200, 50))
        self.Add (self.pull10)

        if self.game.preferenceManager.Preferences["coins"] >= 250:
            self.pull1.Enable()
        else:
            self.pull1.Disable()

        if self.game.preferenceManager.Preferences["coins"] >= 2000:
            self.pull10.Enable()
        else:
            self.pull10.Disable()

        # coin button
        self.CoinButton = FroggerButton (game, self, "Coins: {0}".format (self.game.preferenceManager.Preferences["coins"]), clickEventName="CoinButton")
        self.CoinButton.set_Rect (pygame.Rect (pygame.display.get_surface().get_size()[0] - 400, 10, 300, 50))
        self.add (self.CoinButton)
        self.coin = Sprite ("img_coin", resources = self.game.ResourceCache.Resources)
        self.coin.rect = pygame.Rect (pygame.display.get_surface().get_size()[0] - 150, 15, 30, 30)
        self.add (self.coin)

        # back button
        self.BackButton = FroggerButton (self.game, self, "back", clickEventName="back")
        self.BackButton.set_Rect (pygame.Rect (10, 400, 200, 50))
        self.Add (self.BackButton)

        # instructions
        self.instructions = Sprite ("img_gachainstructions", resources=game.ResourceCache.Resources)
        self.instructions.rect.x = 270
        self.instructions.rect.y = 100
        self.add (self.instructions)


    def CoinButton (self):
        self.game.ChangeScreen (BuyCoinScreen (self.game))

    def Gacha1 (self):
        self.game.ChangeScreen(GachaplayScreen (self.game, 1, False))
        self.game.preferenceManager.Preferences["coins"] -= 250
        self.game.preferenceManager.write()

    def Gacha10 (self):
        self.game.ChangeScreen(GachaplayScreen (self.game, 10, True))
        self.game.preferenceManager.Preferences["coins"] -= 2000
        self.game.preferenceManager.write()

    def back (self):
        self.game.ChangeScreen(Screens.MainMenuScreen.MainMenuScreen(self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)

    def ei (self):
        pass