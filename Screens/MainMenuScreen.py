from Framework.Screen import *
from Framework.SpriteText import *
from Screens.GameScreen import *
from Screens.GachaScreen import *
from Screens.CustomizeScreen import *
from UI.FroggerButton import FroggerButton
from tkinter import filedialog
from tkinter import *
import os

class MainMenuScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)

        game.ResourceCache.LoadDirectory ("font")
        game.ResourceCache.LoadDirectory ("se")

        # title
        self.title = SpriteText("Froggers", font = game.ResourceCache.Resources["fnt_VanillaExtract_48"])
        self.Add (self.title)
        
        # author
        self.author = SpriteText ("Justin Tieu", 24, font = game.ResourceCache.Resources["fnt_VanillaExtract_24"])
        self.author.rect.y = pygame.display.get_surface().get_size()[1] - self.author.rect.height
        self.Add (self.author)

        # play button
        self.PlayButton = FroggerButton (game, self, "play", clickEventName="StartGame")
        self.PlayButton.set_Rect (pygame.Rect (10, 200, 200, 50))
        self.Add (self.PlayButton)

        # load button
        self.PlayButton = FroggerButton (game, self, "load", clickEventName="LoadGame")
        self.PlayButton.set_Rect (pygame.Rect (10, 300, 200, 50))
        self.Add (self.PlayButton)

        # gacha button
        self.GachaButton = FroggerButton (game, self, "gacha", clickEventName="StartGacha")
        self.GachaButton.set_Rect (pygame.Rect (10, 400, 200, 50))
        self.Add (self.GachaButton)

        # customize button
        self.CustomizeButton = FroggerButton (game, self, "customize", clickEventName="customize")
        self.CustomizeButton.set_Rect (pygame.Rect (10, 500, 200, 50))
        self.Add (self.CustomizeButton)

        # exit button
        self.ExitButton = FroggerButton (game, self, "Exit", clickEventName="Exit")
        self.ExitButton.set_Rect (pygame.Rect (10, 600, 200, 50))
        self.Add (self.ExitButton)

    def StartGame (self):
        self.game.ResourceCache.LoadDirectory ("textures") 
        self.game.ChangeScreen (GameScreen (self.game))

    def LoadGame (self):
        seedpack = filedialog.askopenfilename(initialdir = os.path.join (os.getcwd(), "SEEDPACKS"), title = "Select seedpack",filetypes = (("text files","*.txt"),("all files","*.*")))
        
        seeds = []

        if not seedpack:
            return

        sp = open(seedpack, "r")
        for seed in sp:
            seeds.append (int(seed))

        self.game.ResourceCache.LoadDirectory ("textures") 
        self.game.ChangeScreen (GameScreen (self.game, seeds))

    def StartGacha (self):
        self.game.ChangeScreen (GachaScreen (self.game))

    def customize (self):
        self.game.ChangeScreen (CustomizeScreen (self.game))

    def Exit(self):
        self.game.Exit()

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)