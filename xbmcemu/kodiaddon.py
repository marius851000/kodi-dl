from lxml import etree
from .emuvfs import File
from mock import patch
import copy
import os
import sys
from .kodihandle import KodiHandle
class KodiAddon:
    def __init__(self, instance, id):
        self.instance = instance
        self.addon_id = id
        self.name = None
        self.addon_folder = "special://home/addons/"+self.addon_id+"/"
        self.addon_metadata_xml_file = instance.join_path([self.addon_folder, "addon.xml"])
        self.to_imports = []

        self.reload_addon_xml()

    def reload_addon_xml(self):
        file = File(self.instance, self.addon_metadata_xml_file, "rb")
        root = etree.fromstring(file.read())
        file.close()
        
        self.name = root.get("name")

        for extension in root.findall("extension"):
            point = extension.get("point")
            if point == "xbmc.python.pluginsource":
                self.entry_file_name = extension.get("library")

        for requires in root.findall("requires"):
            for import_statement in requires.findall("import"):
                self.to_imports.append(import_statement.get("addon"))

    def execute(self, path):
        virtual_path = self.instance.join_path([self.addon_folder, self.entry_file_name])
        file = File(self.instance, self.instance.join_path([self.addon_folder, self.entry_file_name]), "rb")
        file_binary = file.read()
        file.close()

        #TODO: rewrite the full path based on declared dependancies
        new_path = copy.copy(sys.path)

        for explicit_dependancies in self.to_imports:
            if explicit_dependancies == "xbmc.python":
                continue
            path = self.instance.get_import_path_for_library(explicit_dependancies)
            new_path.append(path)

        new_path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "xbmcmodule")))
        new_path.append(os.path.dirname(self.instance.get_real_path(virtual_path)))

        addon_handle = self.instance.obtain_handle();

        self.instance.handles[addon_handle] = KodiHandle(self)

        global_var = {
            "__name__": "__main__"
        }
        with patch.object(sys, "path", new_path):
            with patch.object(sys, "argv", ["plugin://" + self.addon_id + "/", str(addon_handle), "?"+path]):
                import xbmcemull
                with patch.object(xbmcemull, "INSTANCE", self.instance):
                    with patch.object(xbmcemull, "ADDON", self):
                        exec(file_binary, global_var, global_var)

        return self.instance.free_handle(addon_handle)
