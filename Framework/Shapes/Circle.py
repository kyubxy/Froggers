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