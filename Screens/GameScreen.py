from Framework.Screen import *
from Framework.SpriteText import *
from GameObjects.Level import *
from GameObjects.Entities.Player import *
from UI.LivesDisplay import *
from Screens.GameOverScreen import *

class GameScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)
        
        # level
        self.level = Level (5)
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

        if (not self.player.Alive):
            self.deathtext.SetText ("You died, press any key to continue")
            self.deathtext.rect.x = pygame.display.get_surface().get_size()[0] / 2 - self.deathtext.rect.width / 2
            self.deathtext.rect.y = pygame.display.get_surface().get_size()[1] / 2 - self.deathtext.rect.height / 2
        else:
            self.deathtext.SetText ("")

        for event in pygame.event.get():
            if (event.type == pygame.USEREVENT + 2):
                # account for the updated draw stack
                self.Remove (self.livesdisplay)
                self.livesdisplay.UpdateLives()
                self.Add (self.livesdisplay)

                if self.player.Lives == -1:
                    self.game.ChangeScreen (GameOverScreen (self.game))

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)