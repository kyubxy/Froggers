from Framework.Sprite import *

# box sprite
class Box (Sprite):
    def __init__(self, rect, stroke = 0, col = [255,255,255]):
        surf = pygame.Surface ((rect.width, rect.height))             # create an empty surface
        pygame.draw.rect (surf, col, pygame.Rect (0,0,rect.width,rect.height), stroke)    # draw the rectangle
        super ().__init__ (img = surf)  # initialise the rectangle
        self.rect.x = rect.x
        self.rect.y = rect.y

        # set the colour key to black to ensure transparency
        # *do not set the colour to black, the whole image will just be transparent
        pygame.Surface.set_colorkey (self.image, [0,0,0])   
