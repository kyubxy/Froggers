from Framework.Sprite import *

# physical, drawable representation of a card
class Card ():
    def __init__(self, jacket, meta):
        # sprite 
        self.Jacket = jacket
        
        # contains card metadata (name, rarity etc)
        self.meta = meta
