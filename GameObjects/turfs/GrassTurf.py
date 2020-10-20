from GameObjects.turfs.Turf import Turf
from Framework.Sprite import *

class GrassTurf (Turf):
    def __init__(self):
        Turf.__init__ (self, 1, "res/textures/img_grass.png")
    
    def Update(self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive(self)

# same as grass turf but with caves to signify the end of the level
class GrassEndTurf (Turf):
    def __init__(self):
        Turf.__init__ (self, 5, "res/textures/img_grass.png")

        # place 5 caves
        for i in range (5):
            self.c = Cave ()
            self.c.rect.x = 80 + i * pygame.display.get_surface().get_size()[0] / 5 # TODO: come up with a better way to place the caves along the x axis
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
    def __init__(self):
        self.occupiedtex = pygame.image.load("res/textures/img_caveoccupied.png")       
        super().__init__("res/textures/img_cave.png")
        self.Scale (64,64)
        self.Occupied = False   # whether the player can enter

    def Occupy (self):
        self.image = self.occupiedtex
        self.Scale (64,64)
        self.Occupied = True