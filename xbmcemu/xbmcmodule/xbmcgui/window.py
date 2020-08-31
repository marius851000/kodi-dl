#TODO: get rid of hack (and understand what this does exactly)

class Window:
    def __init__(self, existing_window_id = None):
        self.window_id = existing_window_id

    def getProperty(self, property):
        if property == "plugin.video.youtube-configs":
            return None
        else:
            raise BaseException

    def clearProperty(self, property):
        if property == "plugin.video.youtube-configs":
            pass
        else:
            raise BaseException
