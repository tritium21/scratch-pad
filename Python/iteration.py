def group(iterable, size):
    "Group items in iterable in sub-iterables of size"
    try:
        from itertools import zip_longest
    except ImportError:
        from itertools import izip_longest as zip_longest
    return (tuple(filter(None, x)) for x in zip_longest(*([iter(iterable)]*size)))
