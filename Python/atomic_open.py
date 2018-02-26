import contextlib
import ctypes
import os
import os.path
import shutil
import sys
import tempfile


@contextlib.contextmanager
def atomic(path, mode='r', buffering=-1, encoding=None, errors=None, newline=None):
    name = tempfile.mktemp(prefix=os.path.basename(path), dir=os.path.dirname(path))
    shutil.copy2(path, name)
    with open(name, mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline) as tf:
        yield tf
    if sys.platform == 'win32':
        ctypes.windll.kernel32.ReplaceFileW(path, name, None, 0x2, None, None)
    else:
        os.rename(name, path)
