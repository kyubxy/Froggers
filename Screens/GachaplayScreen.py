from Framework.Screen import *
from Framework.Sprite import *
from Framework.SpriteText import *
from GameObjects.gacha.gachaAnimation import *
from UI.FroggerButton import FroggerButton
import Screens.GachaScreen

class GachaplayScreen (Screen, MouseListener):
    def __init__ (self, game, rolls, guarantee4):
        super().__init__(game)

        game.ResourceCache.LoadDirectory ("textures")

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
        pygame.mixer.music.play()

        # gacha animations
        # introduction
        self.intro_animation = IntroductionAnimation (self.game)
        self.Add (self.intro_animation)
        self.intro_playing = True

        # fishing
        self.fish_animation = FishingAnimation (self.game, self)
        self.Add (self.fish_animation)

        # generate the cards
        self.cards = self.game.cardCollection.roll_gacha(rolls, guarantee4)
        self.rolls = rolls

    def back (self):
        self.game.ChangeScreen(Screens.GachaScreen.GachaScreen (self.game))

    def Update (self):
        super().Update()

        if (self.intro_playing):
            # play intro animation
            self.intro_playing = self.intro_animation.play (self)
        else:
            self.fish_animation.play()   

    def Roll (self):
        if self.rolls > 0:
            # get random card
            self.remove (self.intro_animation)
            self.remove (self.fish_animation)
            self.fish_animation.Start(self.cards[self.rolls - 1])
            self.add (self.fish_animation)
            self.move_to_front(self.frameratecounter)
            self.rolls -= 1

        # TODO results

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)
