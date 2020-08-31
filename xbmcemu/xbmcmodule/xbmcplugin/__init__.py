import xbmcemull

def addDirectoryItem(handle, url, listitem, isFolder = False, totalItems = 0):
    xbmcemull.INSTANCE.get_handle(handle).add_directory_item(url, listitem, isFolder, totalItems)
    return True

def addDirectoryItems(handle, items, totalItems = 0):
    for item in items:
        xbmcemull.INSTANCE.get_handle(handle).add_directory_item(item[0], item[1], item[2], totalItems)
    return True

def endOfDirectory(handle, succeeded = True, updateListing = False, cacheToDisc = True):
    xbmcemull.INSTANCE.get_handle(handle).end_of_directory(handle, succeeded, updateListing, cacheToDisc)

def setResolvedUrl(handle, succeeded, listitem):
    xbmcemull.INSTANCE.get_handle(handle).set_resolved_url(succeeded, listitem)

def addSortMethod(handle, sort_method, label2mask=0):
    if label2mask != 0:
        print("kodidl:todo: ignoring label2mask in addSortMethod")
    xbmcemull.INSTANCE.get_handle(handle).add_sort_method(sort_method)

def setContent(handle, content):
    xbmcemull.INSTANCE.get_handle(handle).set_content(content)

def x_getLanguageOrder():
    return xbmcemull.INSTANCE.additional_input["language_order"]

SORT_METHOD_TRACKNUM = 7
#TODO: find the true id
SORT_METHOD_ALBUM = -1
SORT_METHOD_ALBUM_IGNORE_THE = -1
SORT_METHOD_ARTIST = -1
SORT_METHOD_ARTIST_IGNORE_THE = -1
SORT_METHOD_BITRATE = -1
SORT_METHOD_DATE = -1
SORT_METHOD_DATEADDED = -1
SORT_METHOD_DRIVE_TYPE = -1
SORT_METHOD_DURATION = -1
SORT_METHOD_EPISODE = -1
SORT_METHOD_FILE = -1
SORT_METHOD_GENRE = -1
SORT_METHOD_LABEL = -1
SORT_METHOD_LABEL_IGNORE_THE = -1
SORT_METHOD_LISTENERS = -1
SORT_METHOD_MPAA_RATING = -1
SORT_METHOD_NONE = -1
SORT_METHOD_PLAYLIST_ORDER = -1
SORT_METHOD_PRODUCTIONCODE = -1
SORT_METHOD_PROGRAM_COUNT = -1
SORT_METHOD_SIZE = -1
SORT_METHOD_SONG_RATING = -1
SORT_METHOD_STUDIO = -1
SORT_METHOD_STUDIO_IGNORE_THE = -1
SORT_METHOD_TITLE = -1
SORT_METHOD_TITLE_IGNORE_THE = -1
SORT_METHOD_UNSORTED = -1
SORT_METHOD_VIDEO_RATING = -1
SORT_METHOD_VIDEO_RUNTIME = -1
SORT_METHOD_VIDEO_SORT_TITLE = -1
SORT_METHOD_VIDEO_SORT_TITLE_IGNORE_THE = -1
SORT_METHOD_VIDEO_TITLE = -1
SORT_METHOD_VIDEO_YEAR = -1
