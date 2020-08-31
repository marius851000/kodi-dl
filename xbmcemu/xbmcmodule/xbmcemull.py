INSTANCE = None
ADDON = None

import unicodedata

def to_str(thing):
    try:
        unicode
        have_unicode = True
    except:
        have_unicode = False

    if have_unicode:
        if type(thing) == unicode:
            return unicodedata.normalize("NFKD", thing).encode("ascii", "ignore")
        else:
            return str(thing)
    else:
        return thing
