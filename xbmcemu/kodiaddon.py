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
        self.version = None
        self.addon_folder = "special://home/addons/"+self.addon_id+"/"
        self.addon_metadata_xml_file = instance.join_path([self.addon_folder, "addon.xml"])
        self.to_imports = []
        self.default_setings = {}
        self.translations = {}

        self.reload_addon_xml()

    def reload_addon_xml(self):
        def open_xml(path):
            file = File(self.instance, path, "rb")
            root = etree.fromstring(file.read())
            file.close()
            return root
        root = open_xml(self.addon_metadata_xml_file)

        self.name = root.get("name")
        self.version = root.get("version")

        for extension in root.findall("extension"):
            point = extension.get("point")
            if point == "xbmc.python.pluginsource":
                self.entry_file_name = extension.get("library")

        for requires in root.findall("requires"):
            for import_statement in requires.findall("import"):
                self.to_imports.append(import_statement.get("addon"))

        setting_path = self.instance.join_path([self.addon_folder, "resources/settings.xml"])
        if self.instance.file_exist(setting_path):
            setting_root = open_xml(setting_path)
            for setting in setting_root.iter("setting"):
                id = setting.get("id")
                self.default_setings[id] = dict(setting.items())
                if self.default_setings[id].get("default") == None:
                    self.default_setings[id]["default"] = ""

        #HACK: how does kodi find this folder name

        possible_language_folder = ["English", "resource.language.en_us"]
        lang_folder = "none"

        for lang_folder in possible_language_folder:
            if self.instance.file_exist(self.instance.join_path([self.addon_folder, "resources/language/{}".format(lang_folder)])):
                break

        #TODO: allow to select the language
        translation_path_xml = self.instance.join_path([self.addon_folder, "resources/language/{}/strings.xml".format(lang_folder)])
        if self.instance.file_exist(translation_path_xml):
            translation_root = open_xml(translation_path_xml)
            for string in translation_root.iter("string"):
                self.translations[int(string.get("id"))] = string.text

        translation_path_po = self.instance.join_path([self.addon_folder, "resources/language/{}/strings.po".format(lang_folder)])
        if self.instance.file_exist(translation_path_po):
            trans_po = File(self.instance, translation_path_po, "r")
            msgctxt = None
            msgid = None
            msgstr = None
            for line in trans_po.read().split("\n"):
                first = line.split(" ")[0]
                rest = line[len(first):]
                if len(rest) >= 1:
                    rest = rest[1:]
                if first == "msgctxt":
                    if msgctxt != None:
                        self.translations[int(msgctxt)] = msgid
                        msgctxt = None
                    msgctxt = rest[2:-1]
                elif first == "msgid":
                    msgid = rest[1:-1]
                elif first == "msgstr":
                    msgstr = rest[1:-1]
            if msgctxt != None:
                self.translations[int(msgctxt)] = msgid


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
            addon_path = self.instance.get_import_path_for_library(explicit_dependancies)
            new_path.append(addon_path)

        new_path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "xbmcmodule")))
        new_path.append(os.path.dirname(self.instance.get_real_path(virtual_path)))

        addon_handle = self.instance.obtain_handle();

        self.instance.handles[addon_handle] = KodiHandle(self)

        global_var = {
            "__name__": "__main__"
        }
        with patch.object(sys, "path", new_path):
            with patch.object(sys, "argv", ["plugin://" + self.addon_id + "/", str(addon_handle), path]):
                import xbmcemull
                with patch.object(xbmcemull, "INSTANCE", self.instance):
                    with patch.object(xbmcemull, "ADDON", self):
                        exec(file_binary, global_var, global_var)

        return self.instance.free_handle(addon_handle)

    def get_setting(self, key):
        print("kodidl: getting the setting {} without checking custom value".format(key))
        if key in self.default_setings:
            return str(self.default_setings[key]["default"])
        else:
            return None

    def set_setting(self, key, value):
        print("kodidl:warning: setting value without writing it to disk: {}".format(key))
        if key in self.default_setings:
            self.default_setings[key]["default"] = value
        else:
            self.default_setings[key] = {"default": value}

    def get_translation(self, key):
        return self.translations[int(key)]
