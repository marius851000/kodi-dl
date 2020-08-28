import xbmcemull

def addDirectoryItem(handle, url, listitem, isFolder = False, totalItems = 0):
    xbmcemull.INSTANCE.get_handle(handle).add_directory_item(url, listitem, isFolder, totalItems)
    return True


def endOfDirectory(handle, succeeded = True, updateListing = False, cacheToDisc = True):
    xbmcemull.INSTANCE.get_handle(handle).end_of_directory(handle, succeeded, updateListing, cacheToDisc)

def setResolvedUrl(handle, succeeded, listitem):
    xbmcemull.INSTANCE.get_handle(handle).set_resolved_url(succeeded, listitem)

def addSortMethod(handle, sort_method):
    xbmcemull.INSTANCE.get_handle(handle).add_sort_method(sort_method)

SORT_METHOD_TRACKNUM = 7