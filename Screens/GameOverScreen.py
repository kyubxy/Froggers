from Screen import *
from Screens.MainMenuScreen import *
import Screens.MainMenuScreen 
from Stats import GameStats
from UI.FroggerButton import *
import pygame
import datetime
import os
from tkinter import messagebox, simpledialog
from GameObjects.Entities.Player import *
import logging

class GameOverScreen (Screen):
    def __init__ (self, game, stats):
        super().__init__(game)
        pygame.mouse.set_visible (True)
        
        self.stats = stats 

        self.stats.Name = simpledialog.askstring ("Name", "what is your name?")

        # game over text
        self.deathtext = SpriteText("GAME OVER", font = game.ResourceCache.Resources["fnt_VanillaExtract_48"])
        self.deathtext.SetColour ([255,0,0])
        self.Add (self.deathtext)

        # give coins
        self.coinamount = round ((stats.Points * Player.frogs) / (10000 * (Player.lives+1)))
        self.game.preferenceManager.Preferences["coins"] += self.coinamount
        self.game.preferenceManager.write()

        # display game statistics
        self.results = [
            "RESULTS",
            "",
            f"Points:  {stats.Points}", 
            f"Time: {datetime.timedelta (seconds = round (stats.Time/1000))}",
            f"Coins: +{self.coinamount}",
            "",
            f"Played as {self.stats.Name}"
            ]

        self.DisplayMessages (self.results, (30, 100))

        # display seeds
        self.seeds = ["Your seeds for this round were:"]
        self.seeds.extend (self.stats.Seeds)
        self.DisplayMessages (self.seeds, (500, 100))
        
        # home button
        self.HomeButton = FroggerButton (self.game, self, "Back", clickEventName= "Home")
        self.HomeButton.set_Rect (pygame.Rect (30, 500, 200, 50))
        self.Add (self.HomeButton)

        # export button
        self.ExportButton = FroggerButton (self.game, self, "Export seeds", clickEventName= "Export")
        self.ExportButton.set_Rect (pygame.Rect (30, 580, 200, 50))
        self.Add (self.ExportButton)

        self.game.scoreManager.Scores.append (self.stats)
        self.game.scoreManager.write()
        
    # export the seed list to a file
    def Export (self):
        # check if the folder exists, create one if it doesn't
        if not os.path.isdir ("SEEDPACKS"):
            os.mkdir ("SEEDPACKS")

        # write the file
        #filename = "{0}.txt".format(datetime.datetime.now())
        filename = simpledialog.askstring("filename", "Name the seedpack file")
        if not filename:
            return
             
        f = open(os.path.join ("SEEDPACKS", filename + ".txt"), "w")

        if f == "":
            return

        for seed in range (len(self.stats.Seeds)):
            f.write ("{0}\n".format (self.stats.Seeds[seed]))
        f.close()
        logging.info ("wrote file {0}".format (filename))

        # create a tkinter popup to notify the user
        messagebox.showinfo ("Successfully wrote the seedpacks", "Go to the SEEDPACKS folder in the game's folder")
        
        # disable the button so the same seedpack can't be exported twice
        self.ExportButton.Disable()

    # exit to
    def Home (self):
        self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)

    def DisplayMessages (self, messages, pos, spacing = 30):
        for msg in range(len(messages)):
            self.msgtxt = SpriteText (messages[msg], font = self.game.ResourceCache.Resources["fnt_Berlin_30"])
            self.msgtxt.rect.x = pos[0]
            self.msgtxt.rect.y = pos[1] + spacing * msg
            self.add (self.msgtxt)