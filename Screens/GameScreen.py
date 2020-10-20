from Framework.Screen import *
from Framework.SpriteText import *
from GameObjects.Level import *
from GameObjects.Entities.Player import *
from UI.LivesDisplay import *
from Screens.GameOverScreen import *
from constants import *

class GameScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)
        
        # level
        self.level = Level (10)
        self.Add (self.level)

        # player
        self.player = Player(self.level)
        self.Add (self.player)

        # death text
        self.deathtext = SpriteText("")
        self.deathtext.Background = [0,0,0]
        self.Add (self.deathtext)

        # lives display
        self.livesdisplay = LivesDisplay (self.player)
        self.Add (self.livesdisplay)

    def Update (self):
        super().Update()

        self.level.Update()

        for event in pygame.event.get():
            if (event.type == RESTART):
                self.deathtext.SetText ("")
                # account for the updated draw stack
                self.Remove (self.livesdisplay)
                self.livesdisplay.UpdateLives()
                self.Add (self.livesdisplay)

                # game over
                if self.player.Lives == -1:
                    self.game.ChangeScreen (GameOverScreen (self.game))

            if event.type == DEATH:
                self.deathtext.SetText ("You died, press the space key to continue")
                self.deathtext.rect.x = pygame.display.get_surface().get_size()[0] / 2 - self.deathtext.rect.width / 2
                self.deathtext.rect.y = pygame.display.get_surface().get_size()[1] / 2 - self.deathtext.rect.height / 2

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)