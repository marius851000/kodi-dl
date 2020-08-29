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

SORT_METHOD_TRACKNUM = 7
