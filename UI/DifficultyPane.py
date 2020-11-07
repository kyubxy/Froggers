from Framework.UI.Button import *
from UI.FroggerButton import  FroggerButtonTheme
from Framework.SpriteText import SpriteText
import pygame
from Framework.Sprite import *
from GameObjects.Entities.Player import Player
from constants import *
from UI.HideableButton import *

class DifficultyPane  (pygame.sprite.OrderedUpdates):
    def __init__(self, game, parent, rect):
        super ().__init__ ()

        self.PADDING = 5
        self.LIVES_LINE = 50
        self.FROGS_LINE = 150

        self.rect = rect
        self.game = game
        self.Enabled = False
        self.parent = parent

        # back pane
        self._bgpane_surf = pygame.Surface ((rect.w,rect.h))
        self._bgpane_surf.fill ([100,100,100])
        self._bgpane = Sprite (img = self._bgpane_surf)
        self._bgpane.rect = rect
        self.add (self._bgpane)
        self._bgpane.Hide()

        # title
        self._text = SpriteText ("", font = game.ResourceCache.Resources["fnt_Berlin_20"], colour=[255,255,255])
        self._text.rect.x = self.rect.x
        self._text.rect.y = self.rect.y
        self.add (self._text)

        # lives
        self.lifeIcon = Sprite ("img_lives", resources=game.ResourceCache.Resources)
        self.lifeIcon.rect.x = self.rect.x + self.PADDING
        self.lifeIcon.rect.y = self.rect.y + self.LIVES_LINE
        self.add (self.lifeIcon)
        self.lifeIcon.Hide()

        # lives text
        self.livesText = SpriteText ("", font = game.ResourceCache.Resources["fnt_Berlin_20"], colour=[255,255,255])
        self.livesText.rect.x = self.rect.x + self.PADDING + 50
        self.livesText.rect.y = self.rect.y + self.LIVES_LINE + 10
        self.add (self.livesText)

        # lives down
        self.lifeDown = HideableButton (self.game, self, "-", 40,40,24, "LivesDown")
        self.lifeDown.set_Rect (pygame.Rect (self.rect.x + self.PADDING + 100, self.rect.y + self.LIVES_LINE, 40,40))
        self.add (self.lifeDown)
        self.lifeDown.Disable()

        # lives up
        self.lifeUp = HideableButton (self.game, self, "+", 40,40,24, "LivesUp")
        self.lifeUp.set_Rect (pygame.Rect (self.rect.x + self.PADDING + 180, self.rect.y + self.LIVES_LINE, 40,40))
        self.add (self.lifeUp)
        self.lifeUp.Disable()

        # frogs
        self.frogIcon = Sprite ("img_player", resources=game.ResourceCache.Resources)
        self.frogIcon.rect.x = self.rect.x + self.PADDING
        self.frogIcon.rect.y = self.rect.y + self.FROGS_LINE
        self.add (self.frogIcon)
        self.frogIcon.Hide()

        # frog down
        self.frogDown = HideableButton (self.game, self, "-", 40,40,24, "FrogDown")
        self.frogDown.set_Rect (pygame.Rect (self.rect.x + self.PADDING + 100, self.rect.y + self.FROGS_LINE, 40,40))
        self.add (self.frogDown)
        self.frogDown.Disable()

        # frog up
        self.frogUp = HideableButton (self.game, self, "+", 40,40,24, "FrogUp")
        self.frogUp.set_Rect (pygame.Rect (self.rect.x + self.PADDING + 180, self.rect.y + self.FROGS_LINE, 40,40))
        self.add (self.frogUp)
        self.frogUp.Disable()

        # frog text
        self.frogText = SpriteText ("", font = game.ResourceCache.Resources["fnt_Berlin_20"], colour=[255,255,255])
        self.frogText.rect.x = self.rect.x + self.PADDING + 50
        self.frogText.rect.y = self.rect.y + self.FROGS_LINE + 10
        self.add (self.frogText)

        # done button
        self.doneButton = HideableButton (self.game, self, "Done", 40,40,24, "Done")
        self.doneButton.set_Rect (pygame.Rect (self.rect.x + self.PADDING , self.rect.y + 250, self.rect.width /2,40))
        self.add (self.doneButton)
        self.doneButton.Disable()

    def Enable (self):
        self.Enabled = True
        self._bgpane.Show()

        self._text.SetText ("Difficulty")

        self.lifeIcon.Show()
        self.lifeUp.Enable()
        self.lifeDown.Enable()

        self.frogIcon.Show()
        self.frogIcon.Scale (32,32)
        self.frogUp.Enable()
        self.frogDown.Enable()

        self.doneButton.Enable()

        self.UpdateLabels()

    def Disable (self):
        self.Enabled = False
        self._bgpane.Hide()

        self._text.SetText ("")

        self.lifeIcon.Hide()
        self.lifeUp.Disable()
        self.lifeDown.Disable()

        self.frogIcon.Hide()
        self.frogUp.Disable()
        self.frogDown.Disable()

        self.doneButton.Disable()

        self.livesText.SetText ("")
        self.frogText.SetText ("")

    def Done (self):
        self.parent.difficulty()

    def UpdateLabels (self):
        self.livesText.SetText ("{0}".format (Player.lives))
        self.frogText.SetText ("{0}".format (Player.frogs))

    def LivesUp (self):
        Player.lives += 1
        self.UpdateLabels()

    def LivesDown (self):
        if Player.lives > 0:
            Player.lives -= 1
            self.UpdateLabels()

    def FrogUp (self):
        Player.frogs += 1
        self.UpdateLabels()

    def FrogDown (self):
        if Player.frogs > 1:
            Player.frogs -= 1
            self.UpdateLabels()

    def Update (self):
        pass