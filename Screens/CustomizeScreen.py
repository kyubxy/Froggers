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
		self.CARD_SPACING = 70 

		self.bg = Sprite ("img_bg", resources=self.game.ResourceCache.Resources)
		self.bg.Scale (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1])
		self.add (self.bg)

		self.Add (SpriteText("customize", font=game.ResourceCache.Resources["fnt_VanillaExtract_48"]))

		self.w, self.h = pygame.display.get_surface().get_size()

		# back button
		self.BackButton = FroggerButton (self.game, self, "back", clickEventName="back")
		self.BackButton.set_Rect (pygame.Rect (10, self.h - 75, 200, 50))
		self.Add (self.BackButton)

		# selected sprite
		self.selectedBoxTex = pygame.Surface ((self.CARD_SPACING,self.CARD_SPACING))
		self.selectedBoxTex.fill ([199, 255, 0])
		self.selectedBox = Sprite (img =self.selectedBoxTex)
		self.Add (self.selectedBox)

		self.game.cardCollection.add_frog (0, "default")
		self.game.cardCollection.write_frogs ()

		self.cards = []

		self.DisplayAllPlayers ()
		
	def DisplayAllPlayers (self):
		self.game.cardCollection.read_frogs()
		self.c = 0
		self.y = 0
		for card_id in self.game.cardCollection.FrogCollection:
			card = self.game.cardCollection.get_card (card_id)

			card.Scale (64,64)
			x = self.CARD_PADDING_X + self.c * self.CARD_SPACING 
			if x > self.w:
				card.rect.x = 0
				self.c = 0
			else:
				card.rect.x = x
				self.c += 1
				
			card.rect.y = self.CARD_PADDING_y + self.y * self.CARD_SPACING
			self.Add (card)
			self.cards.append (card)
			
		self.game.preferenceManager.read()

	def back (self):
		self.game.ChangeScreen(Screens.MainMenuScreen.MainMenuScreen(self.game))

	def Update (self):
		super().Update()

		for card in self.cards:
			if card.ID == self.game.preferenceManager.get("player_sprite", "default"):
				self.selectedBox.rect.x = card.rect.x
				self.selectedBox.rect.y = card.rect.y

			if card.clicked:
				self.game.preferenceManager.Preferences["player_sprite"] = card.ID
				self.playercard = self.game.cardCollection.get_card(self.game.preferenceManager.Preferences["player_sprite"])
				self.game.ResourceCache.Resources["img_player"] = self.playercard.Jacket 
				self.game.preferenceManager.write()

	def Add (self, sprite):
		super().Add(sprite)

	def Draw (self, win):
		super().Draw(win)