from GameObjects.turfs.Turf import Turf

class RailTurf (Turf):
    def __init__(self):
        Turf.__init__ (self, "res/textures/img_railstrip.png", 2)