# gets key presses. Only helpful for key down strokes

class KeyboardListener:
    def KeyDown (self, event):
        pass


def get_keydown (oldkeystate, newkeystate, keys):
    return any ([newkeystate[k] and not oldkeystate[k] for k in keys])