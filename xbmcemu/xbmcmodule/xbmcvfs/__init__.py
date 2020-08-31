import xbmcemull

def exists(path):
    return xbmcemull.INSTANCE.file_exist(path)

def mkdir(path):
    return xbmcemull.INSTANCE.mkdir(path)
