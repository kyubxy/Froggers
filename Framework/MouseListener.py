# gets mouse presses. Only helpful for key down strokes

class MouseListener:
    def MouseDown (self, event):
        pass

def get_mousedown (oldkeystate, newkeystate, keys):
    return any ([newkeystate[k] and not oldkeystate[k] for k in keys])