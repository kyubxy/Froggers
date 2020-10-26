import sys
import pygame
import tkinter as tk

# add framework to sys path 
# (dont want a repeat of *last time*)
sys.path.insert (0, "Framework")

from Game import *
from Screens.MainMenuScreen import *
from Screens.GameOverScreen import *
import constants

# Froggers game instance
class FroggersGame (Game):
    def __init__(self, w=1366,h=768):
        super().__init__(title = "Froggers", width=w, height=h)
        self.ChangeScreen (MainMenuScreen(self))

        # initialise tkinter
        root = tk.Tk()
        root.withdraw()

    def Update (self):
        super().Update()

    def Draw (self):
        super().Draw()

    def Run(self):
        super().Run()

# entry point
game = FroggersGame(1366, 768)
game.Run()  
