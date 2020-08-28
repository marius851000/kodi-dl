import xbmcemull

def translatePath(path):
    return xbmcemull.INSTANCE.get_real_path(path)
