import pygame

# groups whereby the children inherit translations from their parents

class GeometricGroup (pygame.sprite.LayeredUpdates):
    def __init__(self):
        super().__init__()

        # group's position
        self._position = (0,0)

    def change_pos (self, pos):
        self._position = pos
        # update transforms with the new position
        self.UpdateTransforms()

    def change_pos_x(self, x):
        self._position = (x, self._position[1])
        # update transforms with the new position
        self.UpdateTransforms()

    def change_pos_y(self, y):
        self._position = (self._position[0], y)
        # update transforms with the new position
        self.UpdateTransforms()

    # updates a single child's position
    def UpdateSpriteTransform (self, sprite):
        if (hasattr (sprite, "change_pos")):
            self.changex = getattr (sprite, "change_pos_x")
            self.changey = getattr (sprite, "change_pos_y")
        else:
            sprite.rect.x += self._position[0] 
            sprite.rect.y += self._position[1]

    # call anytime transforms are updated, updates child positions so that they are relative
    def UpdateTransforms (self):
        for sprite in self.sprites():
            self.UpdateSpriteTransform (sprite)

    def Add (self, sprite):
        self.UpdateSpriteTransform (sprite) # update the sprite's position before adding
        self.add (sprite)

    def Remove (self, sprite):
        self.remove (sprite)

    def move_to_back (self, sprite):
        super().move_to_back (sprite)