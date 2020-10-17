import unittest
import sys
sys.path.insert (0, "Framework")

from Game import *
from UI.Button import Button
from Screen import *


class ButtonTest (Game, unittest.TestCase):
	def __init__(self):
		super().__init__(title = "ButtonTest")

		self.button = Button()
		#self.button.rect_set (pygame.Rect(500,100,400,30))
		self.CurrentScreen.Add (self.button)

	def Update (self):
		super().Update()

	def Run(self):
		super().Run()

t = ButtonTest()
t.Run()