import functools
import pprint

def decorator(function=None, /, *, pretty=False):
    if function is None:
        return functools.partial(decorator, pretty=pretty)
    printer = print
    if pretty:
        printer = pprint.pprint
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(function.__name__)
        printer(args)
        printer(kwargs)
        return function(*args, **kwargs)
    return wrapper

@decorator
def foo(x, y):
    return x + y

@decorator(pretty=True)
def bar(x, y):
    return x + y

def baz(x, y):
    return x + y

if __name__ == "__main__":
    foo("a really long list of strings that should split".split(), "this needs to be added".split())
    bar("a really long list of strings that should split".split(), "this needs to be added".split())
    baz = decorator(baz, pretty=True)
    baz("a really long list of strings that should split".split(), "this needs to be added".split())
    # outputs:
    # foo
    # (['a', 'really', 'long', 'list', 'of', 'strings', 'that', 'should', 'split'], ['this', 'needs', 'to', 'be', 'added'])
    # {}
    # bar
    # (['a', 'really', 'long', 'list', 'of', 'strings', 'that', 'should', 'split'],
    #  ['this', 'needs', 'to', 'be', 'added'])
    # {}
    # baz
    # (['a', 'really', 'long', 'list', 'of', 'strings', 'that', 'should', 'split'],
    #  ['this', 'needs', 'to', 'be', 'added'])
    # {}
