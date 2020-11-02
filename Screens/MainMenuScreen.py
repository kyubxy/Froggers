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
        super().__init__(game, "res/bgm/bgm_menuloop.mp3")

        self.TOOLBAR_BOTTOM = 60
        self.BGLEVEL_PROPERTIES = {"difficulty": 10, "length": 10}

        game.ResourceCache.LoadDirectory ("font")
        game.ResourceCache.LoadDirectory ("se")
        game.ResourceCache.LoadDirectory ("textures")

        self.toolbar = list()

        # background
        self.level = Level (game=self.game, properties=self.BGLEVEL_PROPERTIES)
        self.level.generate()
        self.Add (self.level)
        self.moved = 0
        
        # foreground 
        # pygame doesn't support moving entire groups to the front layer directly
        # so an alternative is to add the foreground groups into a single group and then remove and add the group to move it to the front
        self.foreground = pygame.sprite.Group ()

        # fader
        self.fader = Sprite (img = pygame.Surface (pygame.display.get_surface().get_size()))
        self.Add (self.fader)
        self.fader.image.set_alpha (255)
        self.fade_amount = 255

        # title
        self.title = SpriteText("Froggers", font = game.ResourceCache.Resources["fnt_VanillaExtract_48"])
        self.title.rect.y = 20
        self.title.rect.centerx = pygame.display.get_surface().get_size()[0] // 2
        self.foreground.add (self.title)
        
        # author
        self.author = SpriteText ("Justin Tieu yr12, 2020", font = game.ResourceCache.Resources["fnt_Berlin_20"])
        self.author.rect.x = pygame.display.get_surface().get_size()[0] - self.author.rect.width
        self.foreground.add (self.author)

        # disclaimer
        self.disclaimer = SpriteText ("not for public redistribution", font = game.ResourceCache.Resources["fnt_Berlin_20"])
        self.disclaimer.rect.x = pygame.display.get_surface().get_size()[0] - self.disclaimer.rect.width
        self.disclaimer.rect.y = 18
        self.foreground.add (self.disclaimer)

        # press anywhere text
        self.pressanywhere_text = SpriteText ("Press anywhere to start...", font = game.ResourceCache.Resources["fnt_Berlin_20"])
        self.pressanywhere_text.rect.centerx = pygame.display.get_surface().get_size()[0] // 2
        self.pressanywhere_text.rect.centery = pygame.display.get_surface().get_size()[1] // 2
        self.foreground.add (self.pressanywhere_text)
        
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

        # seedpack button
        self.SeedpackButton = FroggerButton (game, self, "<No seedpack selected>", clickEventName="LoadGame")
        self.toolbar.append (self.SeedpackButton)        

        # exit button
        self.ExitButton = FroggerButton (game, self, "X", clickEventName="Exit")
        self.ExitButton.set_Rect (pygame.Rect (10, 10, 50, 50))
        self.foreground.add (self.ExitButton)

        # option button
        self.OptionButton = FroggerButton (game, self, "O", clickEventName="StartOption")
        self.OptionButton.set_Rect (pygame.Rect (70, 10, 50, 50))
        self.foreground.add (self.OptionButton)

        # add buttons to toolbar
        for button_no in range (len(self.toolbar)):
            button = self.toolbar[button_no]
            width = pygame.display.get_surface().get_size()[0] / len (self.toolbar)
            button.set_Rect (pygame.Rect(width * button_no,  pygame.display.get_surface().get_size()[1] - self.TOOLBAR_BOTTOM, width, 60))
            self.foreground.add (button) 
        self.Add (self.foreground)

        self.seeds = []

    def StartGame (self):
        self.game.ResourceCache.LoadDirectory ("textures") 
        self.game.ChangeScreen (GameScreen (self.game))

    def LoadGame (self):
        seedpack = filedialog.askopenfilename(initialdir = os.path.join (os.getcwd(), "SEEDPACKS"), title = "Select seedpack",filetypes = (("text files","*.txt"),("all files","*.*")))
        
        self.seeds = []

        if not seedpack:
            return

        sp = open(seedpack, "r")
        for seed in sp:
            self.seeds.append (int(seed))

        # generate new level with seeds
        self.Remove (self.level)
        self.level = Level (game=self.game, properties=self.BGLEVEL_PROPERTIES)
        self.level.generate (seed=self.seeds[0])
        self.moved = 0
        
        # set button name
        self.SeedpackButton._label.SetText (os.path.basename (seedpack))

        self.Refresh()

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
        self.moved += 1
        
        # fade in
        if self.moved < 200:
            self.fader.image.set_alpha (self.fade_amount)
            self.fade_amount -= 5          

        # fade out
        if self.moved + 350 > self.level.length:
            self.fader.image.set_alpha (self.fade_amount)
            self.fade_amount += 5

        if (self.moved + 100 > self.level.length):
            # generate new level when moved down entire level
            self.Remove (self.level)
            if len (self.seeds) > 0:
                self.level = Level (game=self.game)
                self.level.generate (self.seeds[0])
                self.seeds.pop(0)
            else:
                self.level = Level (game=self.game, properties=self.BGLEVEL_PROPERTIES)
                self.level.generate()
            self.moved = 0

            self.Refresh()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)

    def Refresh (self):        
        self.Add (self.level)

        # fader
        self.Remove (self.fader)
        self.fade_amount = 255
        self.Add (self.fader)
        
        # move all foreground elements to the front
        self.Remove (self.foreground)
        self.Add (self.foreground)