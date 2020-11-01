from Framework.Sprite import *

# physical, drawable representation of a card
class Card (Sprite):
    def __init__(self, jacket, meta):
        # sprite 
        self.Jacket = jacket
        
        # contains card metadata (name, rarity etc)
        self.meta = meta

        super().__init__(img=jacket)