from pygame.display import toggle_fullscreen
from UI.FroggerButton import FroggerButton
from Framework.SpriteText import SpriteText
from Framework.Sprite import Sprite
from Framework.Screen import *
import Screens.MainMenuScreen
from tkinter import messagebox

class OptionScreen (Screen):
    def __init__ (self, game):
        super().__init__(game, bgm = "res/bgm/bgm_menuloop.mp3")     

        self.bg = Sprite ("img_bg", resources=self.game.ResourceCache.Resources)
        self.bg.Scale (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1])
        self.add (self.bg)
        
        # title text
        self.titletext = SpriteText("Options", font = game.ResourceCache.Resources["fnt_VanillaExtract_48"])
        self.Add (self.titletext)

        # music
        self.musicButton = FroggerButton (self.game, self, "Toggle music", clickEventName="toggleMusic")
        self.musicButton.set_Rect (pygame.Rect (10, 100, 200,50))
        self.Add (self.musicButton)

        # fullscreen
        self.fullscreenButton = FroggerButton (self.game, self, "Toggle fullscreen", clickEventName="toggleFullscreen")
        self.fullscreenButton.set_Rect (pygame.Rect (10, 200, 200,50))
        self.Add (self.fullscreenButton)
        
        # back
        self.backButton = FroggerButton (self.game, self, "back", clickEventName="back")
        self.backButton.set_Rect (pygame.Rect (10, pygame.display.get_surface().get_size()[1] - 60, 200,50))
        self.Add (self.backButton)
        
    def toggleMusic (self):
        self._toggleField ("bgm")

        if self.game.preferenceManager.Preferences["bgm"]:
            self.Play()
        else:
            pygame.mixer.music.stop()                           

    def toggleFullscreen (self):
        self._toggleField ("fullscreen")
        
        res = self.game.preferenceManager.Preferences["fullscreen"]
        messagebox.showinfo (f"fullscreen {res}", "restart the game for changes to take effect")

    # safely toggles a field
    def _toggleField (self, field, default = False):
        self.game.preferenceManager.read()
        if self.game.preferenceManager.Preferences.get (field) is None:     # check if the field exists
            self.game.preferenceManager.Preferences[field] = default    # use default value
        else:            
            # if existing
            self.game.preferenceManager.Preferences[field] = not self.game.preferenceManager.Preferences[field]  
        self.game.preferenceManager.write()

    def back (self):
        self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))