from UI.FroggerButton import *
from Framework.UI.Button import *

class HideableButtonTheme (FroggerButtonTheme):
    def __init__(self) -> None:         
        super().__init__()
        
        self.disabledColour = [0,0,0]

# a button that hides when disabled
class HideableButton (Button):
    def __init__(self, game, parent, label = "button", w = 200, h=50, labelsize = 20, clickEventName = "OnClick"):
        # check if all relevant assets are loaded before proceeding
        if not "font" in game.ResourceCache.LoadedDirectories:
            game.ResourceCache.LoadDirectory ("font")
        if not "se" in game.ResourceCache.LoadedDirectories:
            game.ResourceCache.LoadDirectory ("se")

        resources = game.ResourceCache.Resources
        super().__init__(resources, parent, label = label, w = w, h=h, theme = HideableButtonTheme(), labelsize = labelsize , clickEventName = clickEventName)

        self._originalLabel = label

        #  make the whole thing fully transparent
        pygame.Surface.set_colorkey (self._pane.image, [0,0,0]) 

    def Disable(self): 
        super().Disable ()
        self._label.SetText ("")

    def Enable (self):
        super().Enable()
        self._label.SetText (self._originalLabel)