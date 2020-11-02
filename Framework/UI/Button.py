from Sprite import *
from SpriteText import *
from MouseListener import *
import pygame
import math

# asthetic details about buttons
class ButtonTheme:
    def __init__(self):
        # default colour
        self.unclickedColour = [255,255,255]
        # colour when the button is touching mouse
        self.hoverColour = [163,163,163]
        # colour when the left click is being pressed
        self.clickColour = [79, 79, 79]
        # colour of label
        self.labelColour = [0,0,0]
        # colour of button when it is in the disabled state
        self.disabledColour = [54,54,54]
        # font of label. Leave as none for default font
        self.font = None    
        # sound made by the button when pressed. Leave as None for no sound
        self.pressedsound = None    # path to pressed sound

# contains the background and clickable logic 
class ClickablePane (Sprite, MouseListener):
    def __init__(self, w, h, observer, theme):
        # implementation of observer pattern for button
        # in this case, the observer is just the class instancing the pane
        self._obs = observer

        self.theme = theme

        # generate surface
        self._s = pygame.Surface ([w,h])
        self._s.fill(self.theme.unclickedColour)

        self.Enabled = True

        super().__init__ (img = self._s)

    def update (self):
        if self.Enabled:
            # handle colour logic
            if self.rect.collidepoint (pygame.mouse.get_pos()):
                self.image.fill(self.theme.hoverColour)
                if (pygame.mouse.get_pressed()[0]):
                    self.image.fill (self.theme.clickColour)
            else:
                self.image.fill(self.theme.unclickedColour)  
        else:
            self.image.fill (self.theme.disabledColour)

    def MouseDown (self, event):
        # handle clicking logic
        if (event.button == 1):     # check for left clicks
            if (self.rect.collidepoint (event.pos)):
                # safely call the observer's OnClick method
                if (hasattr (self._obs, "OnClick")):
                    self._click = getattr (self._obs, "OnClick")
                    self._click()

# 
class Button (pygame.sprite.OrderedUpdates):
    def __init__(self, resources, parent, label = "button", w = 200, h=50, theme = ButtonTheme(), labelsize = 32, clickEventName = "OnClick"):
        super().__init__()

        # safely access the parent's click method
        if (hasattr (parent, clickEventName)):
            self._click = getattr (parent, clickEventName)

        # get theme
        self.Theme = theme
        self.labelsize = labelsize
        
        # back pane
        self._pane = ClickablePane (w, h, self, theme)
        self.add (self._pane)

        # label
        font = pygame.font.SysFont (None, 28) if self.Theme.font is None else resources[self.Theme.font]
        self._label = SpriteText (label, self.labelsize, font = font)
        self._label.SetColour (self.Theme.labelColour)
        self.add (self._label)

        self._enabled = True

        # sound
        if theme.pressedsound != None:
            self.sound = resources[theme.pressedsound]
        else:
            self.sound = None

    # method for the pane observer
    def OnClick (self):
        if self.sound != None and self._enabled:
            self.sound.play()

        # call the parent's click method
        if self._enabled:
            self._click()

    # enable button operations
    def Enable (self):
        self._enabled = True
        self._pane.Enabled = True

    # disable button operations
    def Disable (self):
        self._enabled = False
        self._pane.Enabled = False

    # This button's rectangle is the pane's rectangle
    def get_Rect (self):
        return self._pane.rect

    def set_Rect (self, rect):
        # set pane position
        self._pane.rect.x = rect.x
        self._pane.rect.y = rect.y
        self._pane.Scale (rect.width, rect.height)

        # set label position
        self._label.rect.x = self._pane.rect.x + self._pane.rect.width / 2 - self._label.image.get_rect ().width / 2
        self._label.rect.y = self._pane.rect.y + self._pane.rect.height / 2 - self._label.image.get_rect ().height / 2

    def kill (self):
        super().kill()
        