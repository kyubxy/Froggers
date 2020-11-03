from Framework.Screen import *
from Framework.SpriteText import *
import Screens.MainMenuScreen
from Screens.GachaplayScreen import *
from UI.FroggerButton import FroggerButton

class CustomizeScreen (Screen):
    def __init__ (self, game):
        super().__init__(game, "res/bgm/bgm_menuloop.mp3")

        self.CARD_PADDING_X = 20
        self.CARD_PADDING_y = 80

        self.Add (SpriteText("customize"))

        self.w, self.h = pygame.display.get_surface().get_size()

        # back button
        self.BackButton = FroggerButton (self.game, self, "back", clickEventName="back")
        self.BackButton.set_Rect (pygame.Rect (10, self.h - 75, 200, 50))
        self.Add (self.BackButton)

        self.cards = []

        self.DisplayAllPlayers ()
        
    def DisplayAllPlayers (self):
        self.game.cardCollection.read_frogs()
        self.c = 0
        self.y = 0
        for card_id in self.game.cardCollection.FrogCollection:
            card_details =self.game.cardCollection.FrogCollection[card_id]
            card = self.game.cardCollection.get_card (card_details["rarity"], card_id)

            card.Scale (64,64)
            x = self.CARD_PADDING_X + self.c * 64
            if x > self.w:
                card.rect.x = 0
                self.c = 0
            else:
                card.rect.x = x
                self.c += 1
                
            card.rect.y = self.CARD_PADDING_y + self.y * 64
            self.Add (card)
            self.cards.append (card)
            

    def back (self):
        self.game.ChangeScreen(Screens.MainMenuScreen.MainMenuScreen(self.game))

    def Update (self):
        super().Update()

        for card in self.cards:
            if card.clicked:
                pass
            # TODO add player sprite changing code

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)