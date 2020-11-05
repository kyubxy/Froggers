import sys
import tkinter as tk
import os.path

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
        self.cardCollection = CardCollection (self) 
        self.preferenceManager = PreferenceManager ()

        if os.path.exists ("pref.pickle"):
            self.preferenceManager.read()
        else:
            self.preferenceManager.write()

        super().__init__(title = "Froggers", width=w, height=h)

        print (self.preferenceManager.Preferences)

        #self.ChangeScreen (GachaplayScreen(self, 8, True))  
        self.ChangeScreen (MainMenuScreen(self))    

    def Update (self):
        super().Update()

    def Draw (self):
        super().Draw()

    def Run(self):
        super().Run()

# entry point
game = FroggersGame(1366, 768)
game.Run()  