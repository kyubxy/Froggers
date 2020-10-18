import sys
sys.path.insert (0, "Framework")

from Game import *
from TileSurface import *
from Sprite import *
import random

class TileTest (Game):
	def __init__(self):
		super().__init__()
		self.t = TileSurface (coverarea = (500,500), path = "res/textures/img_grass.png", tilesize=(100,100))
		self.s = Sprite (img = self.t)
		self.CurrentScreen.Add (self.s)
		
	def Update (self):
		super().Update()
		
	def Run(self):
		super().Run()

t = TileTest()
t.Run()