from GameObjects.turfs.Turf import Turf
from Framework.Sprite import *

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

        # place 5 caves
        for i in range (5):
            self.c = Cave (game)
            self.c.rect.x = 80 + i * pygame.display.get_surface().get_size()[0] / 5 
            self.c.rect.y = 64
            self.Add (self.c)
    
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
        self.image = self.game.ResourceCache.Resources["img_caveoccupied"]
        self.Scale (64,64)
        self.Occupied = True