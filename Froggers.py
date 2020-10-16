from Game import *
import pygame

# Froggers game instance
class FroggersGame (Game):
    def __init__(self):
        super().__init__(title = "Froggers")
        self.CurrentScreen = main(self)

    def Update (self):
        super().Update()

    def Draw (self):
        super().Draw()

    def OnEvent (self, event):
        super().OnEvent(event)

    def Run(self):
        super().Run()

# entry point
game = FroggersGame()
game.Run()  