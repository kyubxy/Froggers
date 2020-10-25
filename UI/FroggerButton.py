from Framework.UI.Button import Button, ButtonTheme

class FroggerButtonTheme (ButtonTheme):
    def __init__(self):
        super().__init__()
        
        self.font = "res/fnt_Berlin.ttf"
        self.pressedsound = "res/se/se_button.wav"

class FroggerButton (Button):
    def __init__(self, parent, label = "button", w = 200, h=50, labelsize = 20, clickEventName = "OnClick"):
        super().__init__(parent, label = label, w = w, h=h, theme = FroggerButtonTheme(), labelsize = labelsize , clickEventName = clickEventName)

