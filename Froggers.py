import sys
import tkinter as tk
import os.path
import logging

# add framework to sys path 
# (dont want a repeat of *last time*)
sys.path.insert (0, "Framework")

from Framework.Game import *
from Screens.MainMenuScreen import *
from Screens.GameOverScreen import *
from Framework.ResourceManagement.ResourceCache import *
from gachaTools.CardCollection import *
from IO.PreferenceManager import PreferenceManager

# Froggers game instance
class FroggersGame (Game):
    def __init__(self, w=1366,h=768):
        # initialise tkinter
        root = tk.Tk()
        root.withdraw()       

        # initialise managers
        self.cardCollection = CardCollection (self) 
        self.preferenceManager = PreferenceManager ()

        # load save data
        if os.path.exists ("pref.pickle"):
            self.preferenceManager.read()
        else:
            self.preferenceManager.write()
        logging.debug (self.preferenceManager.Preferences)

        super().__init__(title = "Froggers", width=w, height=h)

        # load main screen
        self.ChangeScreen (MainMenuScreen(self))

# entry point
game = FroggersGame(1366, 768)
game.Run()  