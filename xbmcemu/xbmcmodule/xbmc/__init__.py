import xbmcemull

from .keyboard import Keyboard
from .monitor import Monitor
from .player import Player

LOGDEBUG = 0
LOGINFO = 1
LOGWARNING = 2
LOGERROR = 3
LOGFATAL = 4
LOGNONE = 5

def translatePath(path):
    return xbmcemull.INSTANCE.get_real_path(path)

def log(msg, level=LOGDEBUG):
    print("kodidl: log (level {}): {}".format(level, msg))

def getLanguage(format=2): #TODO: region
    if format == 2:
        print("kodidl:todo: plugin ask for language. returning english")
        return "English"
    else:
        raise BaseException

def executebuiltin(command):
    print("kodidl:todo: ignoring executeBuiltin {}".format(command))

def getInfoLabel(infotag):
    infotag_l = infotag.lower()
    if infotag_l == "system.buildversion":
        return "19.0"
    else:
        print("kodidl: unknown infotag for getInfoLabel: {}, retuning None instad".format(infotag))
        return None
