import sys
sys.path.insert (0, "Framework")

from Game import *
from Screen import *
from SpriteText import *
import random

class SpriteTextTest (Game):
	def __init__(self):
		Game.__init__(self)
		self.text = SpriteText ("text")
		self.CurrentScreen.Add (self.text)
		self.text1 = SpriteText ("text")
		self.CurrentScreen.Add (self.text1)
		
	def Update (self):
		super().Update()
		self.text.SetText (str(random.randrange (0,9)) + str(random.randrange (0,9)) +str(random.randrange (0,9)) + str(random.randrange (0,9)) +str(random.randrange (0,9)) + str(random.randrange (0,9)) +str(random.randrange (0,9)) + str(random.randrange (0,9)) +str(random.randrange (0,9)) + str(random.randrange (0,9)) + str(random.randrange (0,9)))
		self.text1.SetText (str(random.randrange (0,9)) + str(random.randrange (0,9)) +str(random.randrange (0,9)) + str(random.randrange (0,9)) +str(random.randrange (0,9)) + str(random.randrange (0,9)) +str(random.randrange (0,9)) + str(random.randrange (0,9)) +str(random.randrange (0,9)) + str(random.randrange (0,9)) + str(random.randrange (0,9)))

	def Run(self):
		super().Run()

t = SpriteTextTest()
t.Run()