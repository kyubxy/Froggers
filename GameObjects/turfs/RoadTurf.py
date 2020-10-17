from GameObjects.turfs.Turf import Turf

class RoadTurf (Turf):
    def __init__(self):
        Turf.__init__ (self, "res/textures/img_roadstrip.png", 6)