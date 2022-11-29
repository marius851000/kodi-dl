import xbmcemull

def exists(path):
    return xbmcemull.INSTANCE.file_exist(path)

def mkdir(path):
    return xbmcemull.INSTANCE.mkdir(path)

def translatePath(path):
    return xbmcemull.INSTANCE.get_real_path(path)