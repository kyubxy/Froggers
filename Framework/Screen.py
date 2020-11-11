import pygame
from SpriteText import *

# Drawables are sorted into screens that can be drawn at different times
class Screen (pygame.sprite.LayeredUpdates):
    nowplaying = ""
    playMusic = True

    def __init__(self, game, bgm = None):
        super(Screen, self).__init__(self)
        self.game = game

        # fps counter
        self.frameratecounter = SpriteText ("fps", 24)
        self.frameratecounter.Background = [0,0,0]

        # remove if unnecessary
        self.Add (self.frameratecounter)

        self.game.preferenceManager.read()
        Screen.playMusic = self.game.preferenceManager.Preferences.get ("bgm", True)

        self.bgm = bgm
        if not bgm is None:
            if Screen.nowplaying != bgm and Screen.playMusic:
                self.Play ()

    def Play (self):
        Screen.nowplaying = self.bgm    
        pygame.mixer.music.load (self.bgm)
        pygame.mixer.music.play (-1)

    def Update (self):
        super().update()

        # update fps counter
        fpstext = "fps: {0}".format (round(self.game.Clock.get_fps(), 2))
        self.frameratecounter.SetText (fpstext)
        # position fps counter to the bottom right corner
        self.frameratecounter.rect.x = pygame.display.get_surface().get_size()[0] - self.frameratecounter.image.get_size()[0]
        self.frameratecounter.rect.y = pygame.display.get_surface().get_size()[1] - self.frameratecounter.image.get_size()[1]

    # turn fps counter on
    def EnableFPS (self):   
        self.Add (self.frameratecounter)

    # turn fps counter off
    def DisableFPS (self):  
        self.frameratecounter.kill()

    # override parent methods

    def Add (self, sprite):
        super(Screen, self).add (sprite)
        self.move_to_front (self.frameratecounter)

    def Remove (self, sprite):
        super().remove (sprite)

    def Draw (self, win):
        super (Screen, self).draw (win)