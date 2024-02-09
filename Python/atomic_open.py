import contextlib
import os
import pathlib
import shutil
import sys
import tempfile


@contextlib.contextmanager
def atomic(path, mode='r', buffering=-1, encoding=None, errors=None, newline=None):
    name = path = pathlib.Path(path)
    exists = path.is_file()
    if exists:
        name = pathlib.Path(tempfile.mktemp(prefix=path.name(path), dir=path.parent))
        shutil.copy2(path, name)
    with open(name, mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline) as tf:
        try:
            yield tf
        except Cancel:
            if not exists:
                pathlib.Path(name).unlink()
            return
    if exists:
        name.replace(path)
