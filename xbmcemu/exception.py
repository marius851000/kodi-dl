class KeyboardInputRequired(Exception):
    def __init__(self, keyboard):
        self.keyboard = keyboard
