import os
from .kodiaddon import KodiAddon
from .exception import KeyboardInputRequired

class KodiInstance:
    def __init__(self, kodi_path):
        self.kodi_path = os.path.abspath(kodi_path)
        self.handles = {}
        self.addons = {}
        self.planned_input = []
        self.real_path_map = {
            "userdata": os.path.join(self.kodi_path, "userdata"),
            "profile": os.path.join(self.kodi_path, "userdata"),
            "home": self.kodi_path,
        }
        
        self.additional_input =  {
            "language_order": ["en"]
        }

    def get_addon(self, addon_id):
        if addon_id in self.addons:
            return self.addons[addon_id]
        addon = KodiAddon(self, addon_id)
        self.addons[addon_id] = addon
        return addon

    def run_addon(self, addon_id, url):
        addon = self.get_addon(addon_id)
        return addon.execute(url)

    def run_url(self, url):
        if url[:9] != "plugin://":
            raise BaseException("can't run an url that doesn't start with plugin://")
        url = url[9:]
        addon_id = url.split("/")[0]
        rest_url = url[len(addon_id):]
        rest_url = rest_url[1:]
        return self.run_addon(addon_id, rest_url)

    def obtain_handle(self):
        id = 1
        while True:
            if id in self.handles:
                id += 1
            else:
                self.handles[id] = None
                return id

    def get_handle(self, id):
        return self.handles[int(id)]

    def free_handle(self, id):
        old_handle = self.handles[id]
        del self.handles[id]
        return old_handle

    def join_path(self, paths):
        result_path = ""
        first_loop = True
        for path in paths:
            if len(result_path) != 0:
                if result_path[-1] == "/":
                    result_path = result_path[0:-1]
            if first_loop:
                result_path = path
                first_loop = False
            else:
                result_path += "/"+path
        return result_path

    def is_real_path(self, path):
        if path.split("//")[0] == "special:":
            folder = path.split("//")[1].split("/")[0]
            return folder in self.real_path_map
        else:
            raise "Invalid path: {}".format(path)

    def get_real_path(self, path):
        folder = path.split("//")[1].split("/")[0]
        remaining = path.split("//")[1][len(folder)+1:]
        return os.path.join(self.real_path_map[folder], remaining)

    def file_exist(self, path):
        return os.path.isfile(self.get_real_path(path))

    def get_import_path_for_library(self, lib_name):
        return self.get_real_path("special://home/addons/{}/lib".format(lib_name))

    def get_user_keyboard_input(self, keyboard):
        if len(self.planned_input) > 0:
            return self.planned_input.pop(0)
        else:
            raise KeyboardInputRequired(keyboard)
