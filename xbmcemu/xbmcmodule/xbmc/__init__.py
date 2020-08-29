import xbmcemull

from .keyboard import Keyboard

LOGDEBUG = 0
LOGINFO = 1
LOGWARNING = 2
LOGERROR = 3
LOGFATAL = 4

def translatePath(path):
    return xbmcemull.INSTANCE.get_real_path(path)

def log(msg, level=LOGDEBUG):
    print("kodidl: log (level {}): {}".format(level, msg))
