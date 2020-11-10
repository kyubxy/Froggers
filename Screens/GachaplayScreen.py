from Framework.Screen import *
from Framework.Sprite import *
from Framework.SpriteText import *
from GameObjects.gacha.gachaAnimation import *
from Screens.GachaResultsScreen import *

class GachaplayScreen (Screen, MouseListener):
    def __init__ (self, game, rolls, guarantee4):
        super().__init__(game, "res/bgm/bgm_gachaplay.mp3")

        game.ResourceCache.LoadDirectory ("textures")

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

    def Update (self):
        super().Update()

        if (self.intro_playing):
            # play intro animation
            self.intro_playing = self.intro_animation.play (self)
        else:
            self.fish_animation.play()   

    def Roll (self):
        if self.rolls > 0:
            self.rolls -= 1
            # get random card
            self.remove (self.intro_animation)
            self.remove (self.fish_animation)
            self.fish_animation.Start(self.cards[self.rolls - 1])
            self.add (self.fish_animation)
            self.move_to_front(self.frameratecounter)
        else:
            self.game.ChangeScreen (GachaResultsScreen(self.game, self.cards))

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)
