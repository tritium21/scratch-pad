import contextlib
import io

@contextlib.contextmanager
def open_helper(obj, *args, **kwargs):
    """
    Yields obj if it is file-like already, otherwise open and yields object.
    """
    if isinstance(obj, io.IOBase):
        yield obj
    else:
        with open(obj, *args, **kwargs) as f:
            yield f
