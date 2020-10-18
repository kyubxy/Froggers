from GameObjects.turfs.Turf import Turf

class RailTurf (Turf):
    def __init__(self):
        Turf.__init__ (self, 2, "res/textures/img_railstrip.png")
    
    def Update(self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive(self)
