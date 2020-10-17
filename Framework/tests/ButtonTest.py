import sys
sys.path.insert (0, "Framework")

from Game import *
from UI.Button import Button, ButtonTheme
from Screen import *


class ButtonTest (Game):
	def __init__(self):
		Game.__init__(self)

		self.theme = ButtonTheme ()
		self.theme.Rounded = True

		self.button = Button(self, "button", theme = self.theme, labelsize=48, clickEventName="click")
		self.button.set_Rect (pygame.Rect(600,100,300,100))
		self.CurrentScreen.Add (self.button)

		self.movingButton = Button(self, "moving button", theme = self.theme, clickEventName="moveClick")
		self.movingButton.set_Rect (pygame.Rect(0,0,300,100))
		self.CurrentScreen.Add (self.movingButton)
		self.x = 0
		self.dir = 1

	def click (self):
		print ("clicked button")

	def moveClick (self):
		print ("clicked moving button")

	def Update (self):
		super().Update()
		if (self.x > 1166):
			self.dir = -1
		elif (self.x < 0):
			self.dir = 1

		self.x += 5 * self.dir
		self.movingButton.set_Rect (pygame.Rect(self.x,0,200,50))

	def Run(self):
		super().Run()

t = ButtonTest()
t.Run()