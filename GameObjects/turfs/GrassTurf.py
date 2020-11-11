from GameObjects.turfs.Turf import Turf
from Framework.Sprite import *
import GameObjects.Entities.Player 

# initial grass turf
class GrassTurf (Turf):
    def __init__(self, game):
        Turf.__init__ (self, 3, "img_grass", game)
    
    def Update(self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive(self)

# same as grass turf but with caves to signify the end of the level
class GrassEndTurf (Turf):
    def __init__(self, game):
        Turf.__init__ (self, 9, "img_grass", game)

        # place n caves
        x = 80
        y = 0
        for _ in range (GameObjects.Entities.Player.Player.frogs):
            self.c = Cave (game)

            # make sure the caves don't spawn off screen
            if x > pygame.display.get_surface().get_size()[0]:
                x = 80
                y += 1

            self.c.rect.x = x
            self.c.rect.y = 64 + 128 * y

            self.Add (self.c)

            x += pygame.display.get_surface().get_size()[0] / 5 
    
    def Update(self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive(self)

# used to signify end of level
class Cave (Sprite):
    def __init__(self, game):
        super().__init__(img = game.ResourceCache.Resources["img_cave"])
        self.Scale (64,64)
        self.Occupied = False   # whether the player can enter
        self.game = game

    # change cave state to occupied
    def Occupy (self):
        self.ChangeImage(self.game.ResourceCache.Resources["img_caveoccupied"])
        self.Scale (64,64)
        self.Occupied = True