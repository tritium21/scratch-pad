def group(iterable, size):
    "Group items in iterable in sub-iterables of size"
    from itertools import zip_longest
    return (tuple(filter(None, x)) for x in zip_longest(*([iter(iterable)]*size)))
