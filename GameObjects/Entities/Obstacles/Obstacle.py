from Framework.Sprite import *

# anything that moves along a turf, not necessarily harmful
class Obstacle (Sprite):
    def __init__(self, path, direc, pos, speed, game, img = None):
        self.dir = direc        # direction of the obstacle {-1,1}
        if path is None:
            super().__init__ (img = img)
        else:
            super().__init__(img = game.ResourceCache.Resources[path])  # load the texture
        # set initial position

        # ensure the initial position is always on screen
        self.rect.x = pos[0] if direc == 1 else pygame.display.get_surface().get_size()[0] - pos[0] 
        self.rect.y = pos[1]

        self.speed = speed # speed of the obstacle

    def Scale (self, width, height):
        super().Scale(width, height)

    def update (self):
        super().update()
                
        # move the obstacle
        self.rect.x += self.dir * self.speed

        # wrap the obstacle around the screen
        if self.dir == 1:
            if (self.rect.left > pygame.display.get_surface().get_size()[0]):
                self.rect.x = -100 - self.rect.width
        else:
            if (self.rect.right < -0):
                self.rect.x = pygame.display.get_surface().get_size()[0]+400

    def kill(self):
        super().kill()

# anything that kills the player, very harmful
class Harmable ():
    def __init__(self):
        pass