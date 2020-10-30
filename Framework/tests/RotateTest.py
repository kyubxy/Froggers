import sys
sys.path.insert (0, "Framework")

from Game import *
from GeometricGroup import *
from Sprite import *

class RotateTest (Game):
    def __init__(self):
        super().__init__(title = "RotateTest")

        self.box = Sprite ("res/textures/img_cave.png")
        self.box.Rotate (45)
        self.CurrentScreen.Add (self.box)

    def Update(self):
        super().Update()

    def Run(self):
        super().Run()

t = RotateTest()
t.Run()