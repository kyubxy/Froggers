from Framework.Screen import *
from Framework.SpriteText import *
from Screens.GameScreen import *
from Screens.GachaScreen import *
from Screens.CustomizeScreen import *
from UI.FroggerButton import FroggerButton

class MainMenuScreen (Screen):
    def __init__ (self, game):
        super().__init__(game)

        game.ResourceCache.LoadDirectory ("font")
        game.ResourceCache.LoadDirectory ("se")

        # title
        self.title = SpriteText("Froggers", font = game.ResourceCache.Resources["fnt_VanillaExtract_48"])
        self.Add (self.title)
        
        # author
        self.author = SpriteText ("Justin Tieu", 24, font = game.ResourceCache.Resources["fnt_VanillaExtract_24"])
        self.author.rect.y = pygame.display.get_surface().get_size()[1] - self.author.rect.height
        self.Add (self.author)

        # play button
        self.PlayButton = FroggerButton (game, self, "play", clickEventName="StartGame")
        self.PlayButton.set_Rect (pygame.Rect (10, 200, 200, 50))
        self.Add (self.PlayButton)

        # gacha button
        self.GachaButton = FroggerButton (game, self, "gacha", clickEventName="StartGacha")
        self.GachaButton.set_Rect (pygame.Rect (10, 300, 200, 50))
        self.Add (self.GachaButton)

        # customize button
        self.CustomizeButton = FroggerButton (game, self, "customize", clickEventName="customize")
        self.CustomizeButton.set_Rect (pygame.Rect (10, 400, 200, 50))
        self.Add (self.CustomizeButton)

        # exit button
        self.ExitButton = FroggerButton (game, self, "Exit", clickEventName="Exit")
        self.ExitButton.set_Rect (pygame.Rect (10, 500, 200, 50))
        self.Add (self.ExitButton)

    def StartGame (self):
        self.game.ResourceCache.LoadDirectory ("textures") 
        self.game.ChangeScreen (GameScreen (self.game))

    def StartGacha (self):
        self.game.ChangeScreen (GachaScreen (self.game))

    def customize (self):
        self.game.ChangeScreen (CustomizeScreen (self.game))

    def Exit(self):
        self.game.Exit()

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)