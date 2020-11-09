from Framework.Sprite import Sprite
from UI.FroggerButton import FroggerButton
from Framework.Screen import *
import Screens.MainMenuScreen
import logging

class BuyCoinScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)     

        self.bg = Sprite ("img_bg", resources=self.game.ResourceCache.Resources)
        self.bg.Scale (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1])
        self.add (self.bg)

        self.coins4000Button = FroggerButton (game, self, "4000 coins => $4000 AUD", clickEventName="coins4000")
        self.coins4000Button.set_Rect (pygame.Rect (10, 10, 300, 50))
        self.add (self.coins4000Button)

        self.coins10000Button = FroggerButton (game, self, "10000 coins => $1 AUD (+$99999AUD and your first born child) WHAT A BARGAIN!", clickEventName="coins10000")
        self.coins10000Button.set_Rect (pygame.Rect (10, 70, 800, 50))
        self.add (self.coins10000Button)

        self.backButton = FroggerButton (game, self, "back", clickEventName="back")
        self.backButton.set_Rect (pygame.Rect (10, 150, 300, 50))
        self.add (self.backButton)

         

    def coins4000 (self):
        self.game.preferenceManager.Preferences ["coins"] += 4000
        self.game.preferenceManager.write()
        logging.info ("bought 4000 coins")

    def coins10000 (self):
        self.game.preferenceManager.Preferences ["coins"] += 10000
        self.game.preferenceManager.write()
        logging.info ("bought 10000 coins")

    def back (self):
        self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)