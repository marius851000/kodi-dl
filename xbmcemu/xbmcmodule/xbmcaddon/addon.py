import xbmcemull

class Addon:
    def __init__(self):
        self.addon_path = xbmcemull.ADDON.addon_id
        self.addon = xbmcemull.INSTANCE.get_addon(self.addon_path)

    def getAddonInfo(self, id):
        file_extensions = [".png", ".jpg", ".jpeg", ".gif"]

        if id == "id":
            return self.addon.addon_id
        elif id == "name":
            return self.addon.name
        elif id == "icon":
            for extension in file_extensions:
                icon_path = self.addon.instance.join_path([self.addon.addon_folder, "icon."+extension])
                if self.addon.instance.file_exist(icon_path):
                    return icon_path
            return None
        elif id == "fanart":
            for extension in file_extensions:
                icon_path = self.addon.instance.join_path([self.addon.addon_folder, "fanart."+extension])
                if self.addon.instance.file_exist(icon_path):
                    return icon_path
            return None
        elif id == "profile":
            return self.addon.instance.join_path(["special://profile/addon_data/", self.addon.addon_id])
        else:
            raise BaseException("kodidl: xbmcaddon.Addon.getAddonInfo: unknown id type : \"{}\"".format(id))
