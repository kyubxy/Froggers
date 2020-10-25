from Framework.SpriteText import *

class FroggerText (SpriteText):
    def __init__(self, text, size = 48):
        super().__init__(text=text, size=size, font = "res/fnt_Berlin.ttf")

    def update (self):
        super().update()

    def SetText (self, text):
        super().SetText(text)

    def SetColour (self, col):
        super().SetColour (text)

    def UpdateText (self):
        super().UpdateText ()

    def kill (self):
        super().kill()