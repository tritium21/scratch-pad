import contextlib
import ctypes
import os
import pathlib
import shutil
import sys
import tempfile

win = sys.platform == 'win32'


def replace_file(old, new)
    if win:
        ctypes.windll.kernel32.ReplaceFileW(old, new, None, 0x2, None, None)
        return
    os.rename(new, old)


@contextlib.contextmanager
def atomic(path, mode='r', buffering=-1, encoding=None, errors=None, newline=None):
    name = path = pathlib.Path(path)
    exists = path.is_file()
    if exists:
        name = tempfile.mktemp(prefix=path.name(path), dir=path.parent)
        shutil.copy2(path, name)
    with open(name, mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline) as tf:
        yield tf
    if exists:
        replace_file(path, name)
