import xbmcemull

class Keyboard:
    def __init__(self, text=None, heading=None, hidden=False):
        self.text = text
        self.heading = heading
        self.hidden = hidden

    def doModal(self, autoclose=0):
        xbmcemull.INSTANCE.get_user_keyboard_input(self)
