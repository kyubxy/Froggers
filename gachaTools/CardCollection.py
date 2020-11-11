import random
from gachaTools.card import *
from Framework.ResourceManagement.ResourceCache import *
import os
import os.path
import configparser
import pickle
import datetime
import logging
from Framework.Game import *

# in regards to gacha frogs, only two operations can take place on them
# 1, gaining new frogs through gacha (summoning). 2, viewing existing frog data (getting).
# This class handles both operations
class CardCollection: 
	def __init__(self, game):
		 
		self.game = game

		# all playable characters earned by the player
		self.CharaCache = ResourceCache ("res/gacha")
		#self.CharaCache.Resources["img_original"] = game.ResourceCache.Resources["img_player"]	# add the original player

		# earned frogs and their data
		# key: frog id - value: frog meta 
		self.FrogCollection = dict()
		self.read_frogs()
		logging.debug (f"{self.FrogCollection}")

	# update frog list, add the METADATA
	def read_frogs (self) -> list():
		if (not os.path.exists ("data.pickle")):
			logging.warning ("no gacha file was found")
			return
		
		with open ("data.pickle", "rb") as handle:
			# deserialize (unpickle) the data 
			self.FrogCollection = pickle.load (handle)

	# writes the list to file
	def write_frogs (self):
		# write in binary and give the file a really vague name to deter tampering
		with open ("data.pickle", "wb") as handle:
			# serialize (pickle) the data and write to file
			pickle.dump (self.FrogCollection, handle, pickle.HIGHEST_PROTOCOL)

	# add a NEW frog's metadata to the list 
	def add_frog (self, rarity, id = None):
		if id is None:	# random card of rarity
			cardDirs = [x for x in os.listdir ("res/gacha") if x[0] == str(rarity)]
			CardID = cardDirs[random.randint (0, len(cardDirs) - 1)]
			id = CardID[2:]

		else:			# specific card
			CardID = "{0}_{1}".format (rarity, id)	# directory path of card

		# load the ini
		self.config = configparser.ConfigParser ()
		self.config.read (os.path.join (os.path.join ("res", "gacha", CardID), "info.ini"))
		meta = dict (self.config.items ("meta"))

		# add to the dictionary
		self.FrogCollection[CardID] = meta

		return CardID

	def get_card (self, CardID):
		#CardID = "{0}_{1}".format (rarity, id)	# directory path of card
			
		# load the image. This step also doubles up as means of checking the card's existence
		self.CharaCache.LoadAsset (os.path.join (CardID, "img_player.png"), resname=CardID)

		# get metadata
		meta = self.FrogCollection[CardID]
		
		# create a card from the file
		card = Card (self.CharaCache.Resources[CardID], meta, CardID)

		return card

	# highcardMin = generate at least 1 card above 3 star. Make true for larger number of rolls
	def roll_gacha (self, rolls, highcardMin = False):
		# generate a new seed independent from previous seeds entered through level generation
		random.seed (datetime.datetime.now())

		cards = [] # return value

		# number of cards whose rarity is greater than 4
		# attained through the highcardMin system
		goodcards = 0	

		# give the player some proportion of good cards for larger rolls
		if highcardMin:
			goodcards = random.randint (1, rolls // 2)
			# add exclusively good cards
			for _ in range (goodcards):
				frog = self.add_frog (random.randint (4, 5))
				cards.append (self.get_card (frog))

		# add the reset of the cards
		for _ in range (rolls - goodcards):
			frog = self.add_frog (3)
			cards.append (self.get_card (frog))		

		# shuffle cards
		random.shuffle (cards)

		return cards
