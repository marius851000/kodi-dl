import xbmcemull

class Addon:
    def __init__(self):
        self.addon_path = xbmcemull.ADDON.addon_id
        self.addon = xbmcemull.INSTANCE.get_addon(self.addon_path)

    def getAddonInfo(self, id):
        if id == "id":
            return self.addon.addon_id
        elif id == "name":
            return self.addon.name
        else:
            raise BaseException("kodidl: xbmcaddon.Addon.getAddonInfo: unknown id type : \"{}\"".format(id))
