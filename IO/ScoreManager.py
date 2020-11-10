import pickle

class ScoreManager:
    def __init__(self) -> None:
        self.Scores = []

    def write (self):
        with open('scores.pickle', 'wb') as handle:
            pickle.dump(self.Scores, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def read (self):
        with open('scores.pickle', 'rb') as handle:
            self.Scores = pickle.load(handle)