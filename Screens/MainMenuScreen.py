from Framework.Screen import *
from Framework.SpriteText import *
from Screens.GameScreen import *
from Screens.GachaScreen import *
from Screens.CustomizeScreen import *
from UI.InvisibleButton import InvisibleButton
from UI.FroggerButton import FroggerButton
from tkinter import filedialog
from tkinter import *
from Stats import *
import os

class MainMenuScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)

        self.TOOLBAR_BOTTOM = 60

        pygame.mixer.music.load ("res/bgm/bgm_menuloop.mp3")
        pygame.mixer.music.play()

        game.ResourceCache.LoadDirectory ("font")
        game.ResourceCache.LoadDirectory ("se")
        game.ResourceCache.LoadDirectory ("textures")

        self.toolbar = list()

        # background
        self.level = Level (game=self.game, properties={"difficulty": 10, "length": 10})
        self.level.generate()
        self.Add (self.level)

        # title
        self.title = SpriteText("Froggers", font = game.ResourceCache.Resources["fnt_VanillaExtract_48"])
        self.title.rect.y = 20
        self.title.rect.centerx = pygame.display.get_surface().get_size()[0] // 2
        self.Add (self.title)
        
        # author
        self.author = SpriteText ("Justin Tieu 2020, not for public redistribution", font = game.ResourceCache.Resources["fnt_Berlin_20"])
        self.author.rect.x = pygame.display.get_surface().get_size()[0] - self.author.rect.width
        self.Add (self.author)

        # press anywhere text
        self.pressanywhere_text = SpriteText ("Press anywhere to start...", font = game.ResourceCache.Resources["fnt_Berlin_20"])
        self.pressanywhere_text.rect.centerx = pygame.display.get_surface().get_size()[0] // 2
        self.pressanywhere_text.rect.centery = pygame.display.get_surface().get_size()[1] // 2
        self.Add (self.pressanywhere_text)
        
        # play button
        self.PlayButton = InvisibleButton (game, self, clickEventName="StartGame")
        self.PlayButton.set_Rect (pygame.Rect (0, 60, pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1] - 170))
        self.Add (self.PlayButton)

        # difficulty button
        self.CustomizeButton = FroggerButton (game, self, "difficulty", clickEventName="customize")
        self.toolbar.append (self.CustomizeButton)

        # scores button
        self.ScoresButton = FroggerButton (game, self, "scores", clickEventName="StartGacha")
        self.toolbar.append (self.ScoresButton)

        # customize button
        self.CustomizeButton = FroggerButton (game, self, "customize", clickEventName="customize")
        self.toolbar.append (self.CustomizeButton)

        # gacha button
        self.GachaButton = FroggerButton (game, self, "gacha", clickEventName="StartGacha")
        self.toolbar.append (self.GachaButton)

        # exit button
        self.ExitButton = FroggerButton (game, self, "X", clickEventName="Exit")
        self.ExitButton.set_Rect (pygame.Rect (10, 10, 50, 50))
        self.Add (self.ExitButton)

        # option button
        self.OptionButton = FroggerButton (game, self, "O", clickEventName="StartOption")
        self.OptionButton.set_Rect (pygame.Rect (70, 10, 50, 50))
        self.Add (self.OptionButton)

        # add buttons to toolbar
        for button_no in range (len(self.toolbar)):
            button = self.toolbar[button_no]
            width = pygame.display.get_surface().get_size()[0] / len (self.toolbar)
            button.set_Rect (pygame.Rect(width * button_no,  pygame.display.get_surface().get_size()[1] - self.TOOLBAR_BOTTOM, width, 60))
            self.Add (button) 

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

    def StartOption (self):
        pass

    def StartGacha (self):
        self.game.ChangeScreen (GachaScreen (self.game))

    def customize (self):
        self.game.ChangeScreen (CustomizeScreen (self.game))

    def Exit(self):
        self.game.Exit()

    def Update (self):
        super().Update()

        self.level.change_pos_y (-1)

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)