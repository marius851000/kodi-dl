import copy

import xbmcemull

class ListItem:
    def __init__(self, label = None, path = None, label2 = None):
        self.label = label
        self.label2 = label2
        self.path = path
        self.arts = {}
        self.category = None
        self.info = {}
        self.properties = {}
        self.subtitles = []
        self.context_menu_item = []

    def setArt(self, values):
        self.arts = copy.copy(values)

    def setInfo(self, category, values):
        self.category = category
        self.info = copy.copy(values)

    def setProperty(self, key, value):
        self.properties[key] = value

    def setProperties(self, dictionary):
        for key in dictionary:
            self.setProperty(key, dictionary[key])

    def setPath(self, path):
        self.path = path

    def getLabel(self):
        return self.label

    def setSubtitles(self, subtitles):
        self.subtitles = copy.copy(subtitles)

    def addContextMenuItems(self, items):
        for item in items:
            self.context_menu_item.append(item)

    def pretty_print(self, pre=""):
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

    def to_dict(self):
        result = {
            "label": self.label,
            "label2": self.label2,
            "path": self.path,
            "arts": self.arts,
            "category": self.category,
            "info": self.info,
            "properties": self.properties,
            "subtitles": self.subtitles,
            "context_menu_item": self.context_menu_item
        }
        return result

def getCurrentWindowId():
    print("kodidl: placeholder: xbmcgui.getCurrentWindowId")
    return 0
