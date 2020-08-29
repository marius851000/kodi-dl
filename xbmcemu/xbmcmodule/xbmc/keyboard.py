import xbmcemull

class Keyboard:
    def __init__(self, text=None, heading=None, hidden=False):
        self.text = text
        self.heading = heading
        self.hidden = hidden

    def doModal(self, autoclose=0):
        self.text = xbmcemull.INSTANCE.get_user_keyboard_input(self)

    def isConfirmed(self):
        print("kodidl:todo: isConfirmed always return true")
        return True

    def getText(self):
        return self.text
