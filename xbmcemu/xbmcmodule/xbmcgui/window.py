#TODO: get rid of hack (and understand what this does exactly)

class Window:
    def __init__(self, existing_window_id = None):
        self.window_id = existing_window_id

    def getProperty(self, property):
        print("kodidl:todo: unknown property in getProperty: {}, returning None".format(property))
        return None

    def clearProperty(self, property):
        print("kodidl:todo: unknown property in clearProperty: {}, skipping".format(property))
        pass

    def setProperty(self, property, value):
        print("kodidl:todo: setting {} to {}, doing nothing".format(property, value))
        pass
