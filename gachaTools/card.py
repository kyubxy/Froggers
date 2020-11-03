from Framework.Sprite import *

# physical, drawable representation of a card
class Card (Sprite):
    def __init__(self, jacket, meta):
        # sprite 
        self.Jacket = jacket
        
        # contains card metadata (name, rarity etc)
        self.meta = meta

        super().__init__(img=jacket)

        self.oldstate = pygame.mouse.get_pressed()[0]
        self.newstate = pygame.mouse.get_pressed()[0]

        self.clicked = False

    def update (self):
        super().update ()

        self.newstate = pygame.mouse.get_pressed()[0]
        self.clicked = self.rect.collidepoint(pygame.mouse.get_pos()) and self.newstate and not self.oldstate
        self.oldstate = self.newstate