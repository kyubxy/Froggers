import sys
import pygame

# add framework to sys path 
# (dont want a repeat of *last time*)
sys.path.insert (0, "Framework")

from Game import *
from Screens.MainMenuScreen import *

# Froggers game instance
class FroggersGame (Game):
    def __init__(self, w=1366,h=768):
        super().__init__(title = "Froggers", width=w, height=h)
        self.ChangeScreen (MainMenuScreen(self))

    def Update (self):
        super().Update()

    def Draw (self):
        super().Draw()

    def OnEvent (self, event):
        super().OnEvent(event)

    def Run(self):
        super().Run()

# entry point
game = FroggersGame()
game.Run()  
