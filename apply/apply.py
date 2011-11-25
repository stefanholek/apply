"""An apply function for Python 2 and 3."""

def  apply(func, *args, **kw):
    """Call a callable object with positional arguments taken from the
    tuple args, and keyword arguments taken from the optional dictionary kw.
    Return its results.
    """
    return func(*args, **kw)
