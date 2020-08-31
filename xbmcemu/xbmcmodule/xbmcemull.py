INSTANCE = None
ADDON = None

def to_str(thing):
    try:
        unicode
        have_unicode = True
    except:
        have_unicode = False
    if have_unicode:
        if type(thing) == unicode:
            return thing.decode("utf8")
        else:
            return str(thing)
    else:
        return thing
