from Framework.Sprite import *

# anything that moves along a turf, not necessarily harmful
class Obstacle (Sprite):
    def __init__(self, path, direc, pos, speed, game):
        self.dir = direc
        super().__init__(img = game.ResourceCache.Resources[path])
        self.rect.x = pos[0] if direc == 1 else pygame.display.get_surface().get_size()[0] - pos[0]
        self.rect.y = pos[1]
        self.speed = speed

    def Scale (self, width, height):
        super().Scale(width, height)

    def update (self):
        super().update()
                
        self.rect.x += self.dir * self.speed
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