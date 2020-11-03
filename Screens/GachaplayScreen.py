from Framework.Screen import *
from Framework.Sprite import *
from Framework.SpriteText import *
from GameObjects.gacha.gachaAnimation import *
import Screens.MainMenuScreen

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

        self.endscreen = False

        self.instruction = SpriteText ("Click anywhere to continue", font = self.game.ResourceCache.Resources["fnt_Berlin_20"])
        self.instruction.rect.y = 80

        self.oldstate = pygame.mouse.get_pressed()[0]
        self.newstate = pygame.mouse.get_pressed()[0]

    def Update (self):
        super().Update()

        if (self.intro_playing):
            # play intro animation
            self.intro_playing = self.intro_animation.play (self)
        else:
            if self.endscreen:
                self.newstate = pygame.mouse.get_pressed()[0]

                if self.newstate and not self.oldstate:
                    self.game.ChangeScreen (Screens.MainMenuScreen.MainMenuScreen(self.game))

                self.oldstate = self.newstate
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
        else:
            self.endscreen = True
            self.remove (self.fish_animation)
            self.Add (SpriteText ("Results", font = self.game.ResourceCache.Resources["fnt_VanillaExtract_48"]))
            self.Add (self.instruction)
            self.game.cardCollection.write_frogs()

            for cardno in range (len(self.cards)):
                card = self.cards[cardno]
                card.Scale (64,64)
                card.rect.x += 64 * cardno
                card.rect.y = 128
                self.Add (card)

    def Add (self, sprite):
        super().Add(sprite)

    def Draw (self, win):
        super().Draw(win)
