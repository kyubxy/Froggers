from GameObjects.Entities.Obstacles.Obstacle import *
import random

# train obstacle
class Train (Obstacle, Harmable):
    def __init__(self, game, dir, pos, speed, length, colour):
        self.KEYCOLOUR = [13,37,69]
        self.length = length

        # load appropriate texture
        directions = {1 : "right", -1 : "left"}
        colours = ["blueline", "greenline", "orangeline"]

        # load textures
        self.body = game.ResourceCache.Resources[f"img_train_{colours[colour]}_body_{directions[dir]}"]
        self.front = game.ResourceCache.Resources[f"img_train_{colours[colour]}_front_{directions[dir]}"]

        # construct the train
        bodylen = (self.length - 1) if dir == -1 else self.length
        tex = pygame.Surface ((self.front.get_rect().w + self.body.get_rect().w * bodylen,self.body.get_rect().h))
        tex.fill (self.KEYCOLOUR)

        
        tex.blit (self.front, (0 if dir == -1 else length * self.body.get_rect().w,0))

        for x in range (1 if dir == -1 else 0,length):
            offset =  self.front.get_rect().w - self.body.get_rect().w if dir == -1 else 0
            tex.blit (self.body, (x * self.body.get_rect().w + offset,0))

        tex.set_colorkey (self.KEYCOLOUR)
        
        super().__init__(None, dir, pos, speed, game, img = tex)

        scaling_factor = 128 / self.rect.h
        self.Scale (self.rect.w * scaling_factor ,self.rect.h * scaling_factor)

    def update (self):
        super().update()