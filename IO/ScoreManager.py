import pickle

# handles scores. less ambiguous name, binary serlization prevents tampering at the fundamental level
# but the user should still be able to clear the scores manually if need be.
class ScoreManager:
    def __init__(self) -> None:
        self.Scores = []

    # write the state
    def write (self):
        with open('scores.pickle', 'wb') as handle:
            pickle.dump(self.Scores, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # read the state
    def read (self):
        with open('scores.pickle', 'rb') as handle:
            self.Scores = pickle.load(handle)