from Framework.UI.Button import *
from UI.FroggerButton import  FroggerButtonTheme
from Framework.SpriteText import SpriteText
import pygame
from Framework.Sprite import *
from GameObjects.Entities.Player import Player
from constants import *
from UI.HideableButton import HideableButton
import Screens.MainMenuScreen

class PauseMenu  (pygame.sprite.Group):
    def __init__(self, game, parent, rect):
        super ().__init__ ()

        self.game = game
        self.parent = parent
        self.rect = rect

        self.BUTTON_Y = 200
        self.PADDING = 20

        self.Enabled = False

        # back pane
        self._bgpane_surf = pygame.Surface ((rect.w,rect.h))
        self._bgpane_surf.fill ([0,0,0])
        self._bgpane = Sprite (img = self._bgpane_surf)
        self._bgpane.rect = rect
        self._bgpane.image.set_alpha (180)
        self.add (self._bgpane)
        self._bgpane.Hide()

        # pause title
        self.title = SpriteText ("Paused", font = game.ResourceCache.Resources["fnt_Berlin_48"])
        self.title.rect.x = rect.x + self.PADDING
        self.title.rect.y = rect.y + self.PADDING
        self.add (self.title)

        # Resume
        self.ResumeButton = HideableButton (self.game, self, "Resume", 40,40,24, "Resume")
        self.ResumeButton.set_Rect (pygame.Rect (self.rect.x + self.PADDING, self.PADDING + self.BUTTON_Y, 200,50))
        self.add (self.ResumeButton)

        # Exit
        self.ExitButton = HideableButton (self.game, self, "Exit", 40,40,24, "back")
        self.ExitButton.set_Rect (pygame.Rect (self.rect.x + self.PADDING, self.PADDING + self.BUTTON_Y + 80, 200,50))
        self.add (self.ExitButton)

        # score text
        self.ScoreText = SpriteText ("", font = self.game.ResourceCache.Resources["fnt_Berlin_48"])
        self.ScoreText.rect.x = 400
        self.ScoreText.rect.y = 250
        self.add (self.ScoreText)

        # time text
        self.TimeText = SpriteText ("", font = self.game.ResourceCache.Resources["fnt_Berlin_48"])
        self.TimeText.rect.x = 400
        self.TimeText.rect.y = 300
        self.add (self.TimeText)

    def Resume (self):
        self.parent.Paused = False
        
    def back (self):
        self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))

    def Enable (self):
        # show and enable everything

        self._bgpane.Show()
        self.title.SetText ("Paused")

        self.ResumeButton.Enable()
        self.ExitButton.Enable()

        self.ScoreText.SetText ("Score: {0}".format(self.parent.stats.Points))
        self.TimeText.SetText ("Time: {0}".format (self.parent.runTime))

        self.Enabled = True

    def Disable (self):
        # disable and hide everything

        self._bgpane.Hide()
        self.title.SetText ("")

        self.ExitButton.Disable()
        self.ResumeButton.Disable()

        self.ScoreText.SetText ("")
        self.TimeText.SetText ("")

        self.Enabled = False

    def Update (self):
        # these items are not included in the update stack
        self.ResumeButton.update()
        self.ExitButton.update()