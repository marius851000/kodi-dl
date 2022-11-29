import copy
import xbmcemull

from .dialog import Dialog
from .window import Window

class ListItem:
    def __init__(self, label = None, path = None, label2 = None, offscreen = True):
        self._is_instancied = True # not sure to remember why this is needed
        self.label = label
        self.label2 = label2
        self.path = path
        self.arts = {}
        self.category = None
        self.info = {}
        self.properties = {}
        self.subtitles = []
        self.context_menu_item = []
        self.x_avalaible_languages = [] #under the ietf code
        self.stream_info = {}
        self.offscreen = offscreen # is likely to got unused
    
    def check_instancied(self):
        if not hasattr(self, "_is_instancied"):
            ListItem.__init__(self)


    def setArt(self, values):
        self.check_instancied()
        for key in values:
            self.arts[key] = values[key]

    def setIconImage(self, path):
        self.check_instancied()
        self.arts["icon"] = path

    def setInfo(self, type, infoLabels):
        self.check_instancied()
        self.category = type
        for key in infoLabels:
            self.info[key] = infoLabels[key]

    def setProperty(self, key, value):
        self.check_instancied()
        self.properties[key] = value

    def setProperties(self, dictionary):
        self.check_instancied()
        for key in dictionary:
            self.setProperty(key, dictionary[key])

    def setPath(self, path):
        self.check_instancied()
        splited_cookie = path.split("|Cookie=")
        if len(splited_cookie) > 1:
            path = splited_cookie[0]
            print("kodidl: unused cookie for media: {}".format(splited_cookie[1]))
        self.path = path

    def getLabel(self):
        self.check_instancied()
        return self.label

    def setSubtitles(self, subtitles):
        self.check_instancied()
        self.subtitles = copy.copy(subtitles)

    def addContextMenuItems(self, items):
        self.check_instancied()
        for item in items:
            self.context_menu_item.append(item)

    def x_addAvalaibleLanguages(self, languages):
        self.check_instancied()
        self.x_avalaible_languages.extend(languages)

    def x_addAvalaibleLangueg(self, language):
        self.check_instancied()
        self.x_avalaible_languages.extend(language)

    def addStreamInfo(self, category, info):
        self.check_instancied()
        if category not in self.stream_info:
            self.stream_info[category] = {}
        for key in info:
            self.stream_info[category][key] = info[key]

    def pretty_print(self, pre=""):
        self.check_instancied()
        if self.label != None:
            print(pre+"label: {}".format(xbmcemull.to_str(self.label)))
        if self.label2 != None:
            print(pre+"label2: {}".format(xbmcemull.to_str(self.label2)))
        if self.arts != {}:
            print(pre+"art: {}".format(self.arts))
        if self.category != None:
            print(pre+"category: {}".format(xbmcemull.to_str(self.category)))
            print(pre+"info: {}".format(self.info))
        if self.properties != {}:
            print(pre+"property: {}".format(self.properties))
        if self.path != None:
            print(pre+"path: {}".format(xbmcemull.to_str(self.path)))
        if self.subtitles != []:
            print(pre+"subtitles: {}".format(self.subtitles))
        if self.context_menu_item != []:
            print(pre+"context menu items: {}".format(self.context_menu_item))
        if self.x_avalaible_languages != []:
            print(pre+"avalaible languages: {}".format(self.x_avalaible_languages))
        if self.stream_info != {}:
            print(pre+"stream info: {}".format(self.stream_info))

    def to_dict(self):
        self.check_instancied()
        result = {
            "label": self.label,
            "label2": self.label2,
            "path": self.path,
            "arts": self.arts,
            "category": self.category,
            "info": self.info,
            "properties": self.properties,
            "subtitles": self.subtitles,
            "context_menu_item": self.context_menu_item,
            "x_avalaible_languages": self.x_avalaible_languages,
            "stream_info": self.stream_info
        }
        return result

def getCurrentWindowId():
    print("kodidl: placeholder: xbmcgui.getCurrentWindowId")
    return 0
