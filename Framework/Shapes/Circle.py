from Framework.Sprite import *

# circle sprite
class Circle (Sprite):
    def __init__(self, x, y, r, width = 0, col = [255,255,255]):
        surf = pygame.Surface ((2*r,2*r))             # create an empty surface
        pygame.draw.circle (surf, col, (r,r), r, width)    # draw the circle
        super ().__init__ (img = surf)  # initialise the circle
        self.rect.x = x
        self.rect.y = y

        # set the colour key to black to ensure transparency
        # *do not set the colour to black, the whole image will just be transparent
        pygame.Surface.set_colorkey (self.image, [0,0,0])   

    # PARENT METHODS

    # rotate about the vertical axis
    def Rotate(self, angle):
        super().Rotate(angle)
    # you can also modify self.image directly however problems arise when the sprite is rotated and is generally not recommended
    def ChangeImage (self, surface):
        super().ChangeImage(surface)
    # changes width and height
    def Scale (self, width, height):
        super().Scale(width, height)
    # used by pygame group, called once per frame
    def update (self):
        pass
    # removes all instances of this object from all pygame groups
    def kill (self):
        super().kill()
