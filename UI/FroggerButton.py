from Framework.UI.Button import Button, ButtonTheme

class FroggerButtonTheme (ButtonTheme):
    def __init__(self):
        super().__init__()
        
        self.font = "fnt_Berlin_24"
        self.pressedsound = "se_button"

# frogger implementation of the framework button
class FroggerButton (Button):
    def __init__(self, game, parent, label = "button", w = 200, h=50, labelsize = 20, clickEventName = "OnClick"):
        # check if all relevant assets are loaded before proceeding
        if not "font" in game.ResourceCache.LoadedDirectories:
            game.ResourceCache.LoadDirectory ("font")
        if not "se" in game.ResourceCache.LoadedDirectories:
            game.ResourceCache.LoadDirectory ("se")

        resources = game.ResourceCache.Resources
        super().__init__(resources, parent, label = label, w = w, h=h, theme = FroggerButtonTheme(), labelsize = labelsize , clickEventName = clickEventName)

