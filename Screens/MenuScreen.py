from Framework.Screen import *
from Framework.SpriteText import *
from Framework.UI.Button import Button
from Screens.GameScreen import *
from Screens.GachaScreen import *

class MainMenuScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)

        self.Add (SpriteText("main menu"))

        # play button
        self.PlayButton = Button (self, "play", clickEventName="StartGame")
        self.PlayButton.set_Rect (pygame.Rect (10, 200, 200, 50))
        self.Add (self.PlayButton)

        # gacha button
        self.GachaButton = Button (self, "gacha", clickEventName="StartGacha")
        self.GachaButton.set_Rect (pygame.Rect (10, 300, 200, 50))
        self.Add (self.GachaButton)

        # exit button
        self.ExitButton = Button (self, "Exit", clickEventName="Exit")
        self.ExitButton.set_Rect (pygame.Rect (10, 400, 200, 50))
        self.Add (self.ExitButton)

    def StartGame (self):
        self.game.ChangeScreen (GameScreen (self.game))

    def StartGacha (self):
        self.game.ChangeScreen (GachaScreen (self.game))

    def Exit(self):
        self.game.Exit()

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)