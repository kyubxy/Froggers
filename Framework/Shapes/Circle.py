from Framework.Sprite import *

# circle sprite
# FIXME currently a stationary object
class Circle (Sprite):
    def __init__(self, x, y, r, width, col = [255,255,255]):
        surf = pygame.Surface ((2*r,2*r))             # create an empty surface
        pygame.draw.circle (surf, col, (x,y), r, width)    # draw the circle
        super ().__init__ (img = surf)  # initialise the circle