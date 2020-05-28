from decorator import decorate

def _deprecated(func, *args, **kw):
    return func(*args, **kw)

def deprecated(func):
    return decorate(func, _deprecated)
