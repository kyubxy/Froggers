import sys
sys.path.insert (0, "Framework")

from Game import *
from GeometricGroup import *
from Sprite import *

class GeometricGroupTest (Game):
	def __init__(self):
		Game.__init__(self)
		self.gc = GeometricGroup ()
		self.img = pygame.Surface ((30, 30))
		self.img.fill ([255,255,255])
		self.img2 = pygame.Surface ((30, 30))
		self.img2.fill ([23,23,23])
		self.s = Sprite (img = self.img)
		self.a = Sprite (img = self.img2)
		self.a.Scale(1366, 100) 
		self.gc.Add (self.a)
		self.s.rect.x = 0
		self.s.rect.y = 0
		self.gc.Add (self.s)

		self.gc.change_pos_y(768)
		
	def Update (self):
		super().Update()
		self.gc.Add (self.s)
		self.CurrentScreen.Add (self.gc)
		self.gc.change_pos_y (-5)
		self.s.rect.x += 10

	def Run(self):
		super().Run()

t = GeometricGroupTest()
t.Run()