from UI.FroggerButton import FroggerButton
from Framework.SpriteText import SpriteText
from Framework.Sprite import Sprite
from Framework.Screen import *
import Screens.MainMenuScreen

class GachaResultsScreen (Screen):
    def __init__ (self, game, cards):
        super().__init__(game, bgm = "res/bgm/bgm_menuloop.mp3")     

        self.cards = cards

        # background
        self.bg = Sprite ("img_bg", resources=self.game.ResourceCache.Resources)
        self.bg.Scale (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1])
        self.add (self.bg)
        
        # title text
        self.titletext = SpriteText("Results", font = game.ResourceCache.Resources["fnt_VanillaExtract_48"])
        self.Add (self.titletext)
        
        # back
        self.backButton = FroggerButton (self.game, self, "back", clickEventName="back")
        self.backButton.set_Rect (pygame.Rect (10, pygame.display.get_surface().get_size()[1] - 60, 200,50))
        self.Add (self.backButton)
        
        self.game.cardCollection.write_frogs()

        # display each of the cards
        for cardno in range (len(self.cards)):
            card = self.cards[cardno]
            card.Scale (64,64)
            card.rect.x = 64 * cardno
            card.rect.y = 128
            self.Add (card)

    def back (self):
        self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))
