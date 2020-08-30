INSTANCE = None
ADDON = None

def to_str(thing):
    if type(thing) == unicode:
        return thing.decode("utf8")
    else:
        return str(thing)
