from UI.FroggerButton import FroggerButton
from Framework.SpriteText import SpriteText
from Framework.Sprite import Sprite
from Framework.Screen import *
import Screens.MainMenuScreen
from GameObjects.Entities.Obstacles.Train import *

class test (Screen):
    def __init__ (self, game):
        super().__init__(game, bgm = "res/bgm/bgm_menuloop.mp3")     

        game.ResourceCache.LoadDirectory ("textures")
        game.ResourceCache.LoadDirectory ("font")
        game.ResourceCache.LoadDirectory ("se")

        self.bg = Sprite ("img_bg", resources=self.game.ResourceCache.Resources)
        self.bg.Scale (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1])
        self.add (self.bg)
        
        # title text
        self.titletext = SpriteText("test", font = game.ResourceCache.Resources["fnt_VanillaExtract_48"])
        self.Add (self.titletext)

        # back
        self.backButton = FroggerButton (self.game, self, "back", clickEventName="back")
        self.backButton.set_Rect (pygame.Rect (10, pygame.display.get_surface().get_size()[1] - 60, 200,50))
        self.Add (self.backButton)

        game.scoreManager.Scores.sort (key=lambda x: x.Points, reverse=True)

        self.directions = [-1,1]
        self.Add (Train(game, 1, (0,0), 2, random.randint (3, 6), random.randint (0, 2)))


    def back (self):
        self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))

    def Update (self):
        super().Update()