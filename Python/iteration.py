import itertools

def group_longest(iterable, size):
    "Group items in iterable in sub-iterables of size"
    return (tuple(filter(None, x)) for x in itertools.zip_longest(*([iter(iterable)]*size)))

def group(iterable, size):
    "Group items in iterable in sub-iterables of size"
    return zip(*([iter(iterable)]*size))
