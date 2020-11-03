from Framework.UI.Button import Button, ButtonTheme
import pygame

class InvisibleButtonTheme (ButtonTheme):
    def __init__ (self):
        super().__init__ ()
        self.unclickedColour = [0,0,0]
        self.hoverColour = [0,0,0]
        self.clickColour = [0,0,0]
        self.disabledColour = [0,0,0]

class InvisibleButton (Button):
    def __init__(self, game, parent, w = 200, h=50, clickEventName = "OnClick"):
        # check if all relevant assets are loaded before proceeding
        if not "font" in game.ResourceCache.LoadedDirectories:
            game.ResourceCache.LoadDirectory ("font")
        if not "se" in game.ResourceCache.LoadedDirectories:
            game.ResourceCache.LoadDirectory ("se")

        resources = game.ResourceCache.Resources
        super().__init__(resources, parent, label = "", w = w, h=h, theme = InvisibleButtonTheme() , clickEventName = clickEventName)

        #  make the whole thing fully transparent
        pygame.Surface.set_colorkey (self._pane.image, [0,0,0]) 