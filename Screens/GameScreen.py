from Framework.Screen import *
from GameObjects.Level import *
from GameObjects.Entities.Player import *

class GameScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)
        
        # level
        self.level = Level (30)
        self.Add (self.level)

        # player
        self.player = Player(self.level)
        self.Add (self.player)

    def Update (self):
        super().Update()

        self.level.Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)