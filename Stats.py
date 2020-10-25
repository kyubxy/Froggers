class PlayerStats ():
    def __init__(self):
        self.Coins = 0          # coins earned by the player
        self.Frogs = []         # Frog types attained through gacha
        self.HighestLevel = 0   # highest level reached by the player
        self.Rank = 1           # level gained through experience points
        self.Experience = 0

class GameStats ():
    def __init__(self):
        self.Points = 0
        self.Time = 0
        self.Seeds = []