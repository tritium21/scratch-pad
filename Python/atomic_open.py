import contextlib
import pathlib
import shutil
import tempfile


@contextlib.contextmanager
def atomic(path, mode='r', buffering=-1, encoding=None, errors=None, newline=None):
    old_path = pathlib.Path(path)
    new_path = pathlib.Path(tempfile.mktemp(prefix=path.name(path), dir=path.parent))
    exists = old_path.is_file()
    if exists:
        shutil.copy2(old_path, new_path)
    with open(new_path, mode=mode, buffering=buffering, encoding=encoding, errors=errors, newline=newline) as tf:
        yield tf
        tf.flush()
    new_path.replace(old_path)
