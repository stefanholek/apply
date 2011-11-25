"""An apply function for Python 2 and 3."""

def apply(object, args=None, kwargs=None):
    """Call a callable object with positional arguments taken from the
    tuple args, and keyword arguments taken from the optional dictionary
    kwargs; return its results.
    """
    if args is None:
        args = ()
    if kwargs is None:
        kwargs = {}
    return object(*args, **kwargs)
