from pathlib import Path


def walk(path, callback=None):
    if not isinstance(path, Path):
        raise TypeError('path must be an instance of filepath.Path')
    if not callable(callback):
        raise TypeError('callback must be a function')

    callback(path)

    # We do not follow symlinks (meaning only that we don't recurse down links
    # to directories, since we've already called our callback on path)
    if path.is_symlink():
        return

    # is_dir must follow is_symlink, because is_dir *does* follow symlinks
    if path.is_dir():
        for subpath in path.iterdir():
            walk(subpath, callback)
