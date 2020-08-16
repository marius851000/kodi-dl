import copy

class ListItem:
    def __init__(self, label = None, path = None):
        self.label = label
        self.path = path
        self.arts = {}
        self.category = None
        self.info = {}
        self.properties = {}
        self.subtitles = []

    def setArt(self, values):
        self.arts = copy.copy(values)

    def setInfo(self, category, values):
        self.category = category
        self.info = copy.copy(values)

    def setProperty(self, key, value):
        self.properties[key] = value

    def setSubtitles(self, subtitles):
        self.subtitles = copy.copy(subtitles)

    def pretty_print(self, pre=""):
        print(pre+"label: {}".format(self.label))
        if self.arts != {}:
            print(pre+"art: {}".format(self.arts))
        if self.category != None:
            print(pre+"category: {}".format(self.category))
            print(pre+"info: {}".format(self.info))
        if self.properties != {}:
            print(pre+"property: {}".format(self.properties))
        if self.path != None:
            print(pre+"path: {}".format(self.path))
        if self.subtitles != []:
            print(pre+"subtitles: {}".format(self.subtitles))

    def to_dict(self):
        result = {
            "label": self.label,
            "path": self.path,
            "arts": self.arts,
            "category": self.category,
            "info": self.info,
            "properties": self.properties,
            "subtitles": self.subtitles,
        }
        return result
