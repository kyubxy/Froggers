from Framework.Screen import *
from Framework.SpriteText import *
from Framework.Sprite import *
from UI.FroggerButton import FroggerButton
from GameObjects.gacha.gachaAnimation import *
import Screens.GachaScreen 

class GachaplayScreen (Screen):
    def __init__ (self, game, rolls):
        super().__init__(game)

        game.ResourceCache.LoadDirectory ("textures")

        self.rolls = rolls
        #self.Add (SpriteText("gachaplay"))

        # roll button
        self.RollButton = FroggerButton (game, self, "roll", clickEventName="roll")
        self.RollButton.set_Rect (pygame.Rect (10, 200, 200, 50))
        #self.Add (self.RollButton)

        # back button
        self.BackButton = FroggerButton (game, self, "back", clickEventName="back")
        self.BackButton.set_Rect (pygame.Rect (10, 300, 200, 50))
        #self.Add (self.BackButton)

        # play bgm
        pygame.mixer.music.load ("res/bgm/bgm_gachaplay.mp3")
        #pygame.mixer.music.play()

        # gacha animations
        # introduction
        self.intro_animation = IntroductionAnimation (self.game)
        self.Add (self.intro_animation)

        # fishing
        self.fish_animation = FishingAnimation (self.game)
        self.fish_animation.reset()

    def roll (self):
        pass

    def back (self):
        self.game.ChangeScreen(Screens.GachaScreen.GachaScreen (self.game))

    def Update (self):
        super().Update()

        # play intro animation
        intro_finished = self.intro_animation.play ()

        if (intro_finished):
            self.Add (self.fish_animation)
            self.fish_animation.play()      

            

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)