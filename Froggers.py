import sys
import tkinter as tk
import os.path
import logging


# add framework to sys path 
# (dont want a repeat of *last time*)
sys.path.insert (0, "Framework")

from Framework.Game import *
from Framework.ResourceManagement.ResourceCache import *
from Screens.MainMenuScreen import *
from Screens.GameOverScreen import *
from IO.PreferenceManager import PreferenceManager
from IO.ScoreManager import ScoreManager
from gachaTools.CardCollection import *

# Froggers game instance
class FroggersGame (Game):
    def __init__(self, w=1366,h=768):
        # initialise tkinter
        self.root = tk.Tk()
        self.root.withdraw()
        self.root.attributes ("-topmost", True)     

        # initialise managers
        self.cardCollection = CardCollection (self) 
        self.preferenceManager = PreferenceManager ()
        self.scoreManager = ScoreManager ()

        # load save data
        if os.path.exists ("pref.pickle"):
            self.preferenceManager.read()
        else:
            self.preferenceManager.write()
            logging.debug (f"self.preferenceManager.Preferences")

        # load scores
        if os.path.exists ("scores.pickle"):
            self.scoreManager.read()
        else:
            self.scoreManager.write()

        super().__init__(title = "Froggers", width=w, height=h, fullscreen=self.preferenceManager.get ("fullscreen", False))

        # load main screen
        self.ChangeScreen (MainMenuScreen(self))

# entry point
if __name__ == "__main__":
    game = FroggersGame(1366, 768)
    game.Run()  