from UI.FroggerButton import FroggerButton
from Framework.SpriteText import SpriteText
from Framework.Sprite import Sprite
from Framework.Screen import *
import Screens.MainMenuScreen

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

        self.backButton = FroggerButton (self.game, self, "back", clickEventName="back")
        self.backButton.set_Rect (pygame.Rect (10, pygame.display.get_surface().get_size()[1] - 60, 200,50))
        self.Add (self.backButton)
        
    def toggleMusic (self):
        self.game.preferenceManager.read()
        if self.game.preferenceManager.Preferences.get ("bgm") is None:
            self.game.preferenceManager.Preferences["bgm"] = False
            pygame.mixer.music.stop()
        else:            
            if self.game.preferenceManager.Preferences["bgm"]:
                self.game.preferenceManager.Preferences["bgm"] = False
                pygame.mixer.music.stop()                
            else:
                self.game.preferenceManager.Preferences["bgm"] = True
                self.Play()             

        self.game.preferenceManager.write()

    def back (self):
        self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)