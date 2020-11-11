from UI.FroggerButton import FroggerButton
from Framework.SpriteText import SpriteText
from Framework.Sprite import Sprite
from Framework.Screen import *
import Screens.MainMenuScreen
import datetime

class ScoresScreen (Screen):
    def __init__ (self, game):
        super().__init__(game, bgm = "res/bgm/bgm_menuloop.mp3")     

        self.bg = Sprite ("img_bg", resources=self.game.ResourceCache.Resources)
        self.bg.Scale (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1])
        self.add (self.bg)
        
        # title text
        self.titletext = SpriteText("Scores", font = game.ResourceCache.Resources["fnt_VanillaExtract_48"])
        self.Add (self.titletext)

        # back
        self.backButton = FroggerButton (self.game, self, "back", clickEventName="back")
        self.backButton.set_Rect (pygame.Rect (10, pygame.display.get_surface().get_size()[1] - 60, 200,50))
        self.Add (self.backButton)

        game.scoreManager.read()
        #game.scoreManager.Scores = sorted (game.scoreManager.Scores)
        game.scoreManager.Scores.sort (key=lambda x: int(x.Points), reverse=True)

        message_format = lambda score: f"{score.Name} : {score.Points}pts - {datetime.timedelta(seconds= round(score.Time / 1000))}"
        messages = [message_format (score) for score in game.scoreManager.Scores]
       
        self.DisplayMessages (messages, (80,80))

    def back (self):
        self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen (self.game))

    def Update (self):
        super().Update()

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)
    
    def DisplayMessages (self, messages, pos, spacing = 30):
        for msg in range(len(messages)):
            self.msgtxt = SpriteText (messages[msg], font = self.game.ResourceCache.Resources["fnt_Berlin_30"], colour=[0,0,0])
            self.msgtxt.rect.x = pos[0]
            self.msgtxt.rect.y = pos[1] + spacing * msg
            self.add (self.msgtxt)