from GameObjects.turfs.Turf import Turf

class RoadTurf (Turf):
    def __init__(self):
        Turf.__init__ (self, 6, "res/textures/img_roadstrip.png")

    def Update (self):
        pass

    def Active (self):
        Turf.Active(self)

    def NonActive (self):
        Turf.NonActive (self)