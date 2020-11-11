import pickle

# handles ALL save data
# despite the file being called pref, the file contains main game data
# that needs to persist during runs. The naming is used to deter tampering.
class PreferenceManager:
    def __init__(self) -> None:
        self.Preferences = dict()

    # write the state to a file
    def write (self):
        with open('pref.pickle', 'wb') as handle:
            pickle.dump(self.Preferences, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # set the state to a file
    def read (self):
        with open('pref.pickle', 'rb') as handle:
            self.Preferences = pickle.load(handle)

    # safely retrieve a value. Use a default value if the value hasn't been written already
    def get (self, key, defaultValue, setDefault = True):        
        if self.Preferences.get (key) is not None:
            return self.Preferences[key]
        else:
            # write the value when requested
            if setDefault:
                self.Preferences[key] = defaultValue
                self.write()
            return defaultValue
            