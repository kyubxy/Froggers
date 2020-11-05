import pickle

class PreferenceManager:
    def __init__(self) -> None:
        self.Preferences = dict()

    def write (self):
        with open('pref.pickle', 'wb') as handle:
            pickle.dump(self.Preferences, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def read (self):
        with open('pref.pickle', 'rb') as handle:
            self.Preferences = pickle.load(handle)

    def get (self, key, defaultValue, setDefault = True):        
        if self.Preferences.get (key) is not None:
            return self.Preferences[key]
        else:
            # write the value when requested
            if setDefault:
                self.Preferences[key] = defaultValue
                self.write()
            return defaultValue