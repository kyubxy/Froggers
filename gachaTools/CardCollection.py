from gachaTools.card import *
from Framework.ResourceManagement.ResourceCache import *
import os
import os.path
import configparser
import pickle

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
		self.get_frogs()

		self.summon ("tippy1", 5)
		self.write_frogs()

		self.read_frogs()
		print ()

	# update frog list, add the METADATA
	def read_frogs (self) -> list():
		if (not os.path.exists ("data.pickle")):
			print ("no gacha file was found")
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
	def add_frog (self, id, rarity):
		RelativeDirectory = "{0}_{1}".format (rarity, id)	# directory path of card

		# load the ini
		self.config = configparser.ConfigParser ()
		self.config.read (os.path.join (os.path.join ("res", "gacha", RelativeDirectory), "info.ini"))
		meta = dict (self.config.items ("meta"))

		# add to the dictionary
		self.FrogCollection[id] = meta

	def get_jacket (self, id):
		# load the image. This step also doubles up as means of checking the card's existence
		RelativeDirectory = "{0}_{1}".format (rarity, id)	# directory path of card
		self.CharaCache.LoadAsset (os.path.join (RelativeDirectory, "img_player.png"), resname=id)
		
		# create a card from the file
		card = Card (self.CharaCache.Resources[id], meta)

		# add name to list
		self.FrogCollection.append (meta["name"])
		self.write_frogs()

		return card
'''
	# summon a specic card given its ID
	def summon (self, id, rarity) -> Card:
		# load the image. This step also doubles up as means of checking the card's existence
		RelativeDirectory = "{0}_{1}".format (rarity, id)	# directory path of card
		self.CharaCache.LoadAsset (os.path.join (RelativeDirectory, "img_player.png"), resname=id)

		# load the metadata
		# intialise ini reading
		self.config = configparser.ConfigParser ()

		# load the ini
		self.config.read (os.path.join (os.path.join ("res", "gacha", RelativeDirectory), "info.ini"))
		meta = dict (self.config.items ("meta"))
		
		# create a card from the file
		card = Card (self.CharaCache.Resources[id], meta)

		# add name to list
		self.FrogCollection.append (meta["name"])
		self.write_frogs()

		return card

	
	'''