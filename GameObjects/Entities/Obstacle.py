from Framework.Sprite import *

class Obstacle (Sprite):
    def __init__(self, path, direc, pos, speed, frequency_offset):
        self.frequency_offset = frequency_offset
        self.dir = direc
        super().__init__(path)
        self.rect.x = 0 if direc == 1 else pygame.display.get_surface().get_size()[0] + self.frequency_offset
        self.rect.y = pos[1]
        self.speed = speed

    def Scale (self, width, height):
        super().Scale(width, height)

    def update (self):
        super().update()
        self.rect.x += self.dir * self.speed
        if self.dir == 1:
            if (self.rect.left > pygame.display.get_surface().get_size()[0] + self.frequency_offset):
                self.rect.x = -self.rect.width
        else:
            if (self.rect.right < -self.frequency_offset):
                self.rect.x = pygame.display.get_surface().get_size()[0]+self.rect.width

    def kill(self):
        super().kill()