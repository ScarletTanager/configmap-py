from walk import walk
from pathlib import Path

def load_configmap(pathstr):
    path = Path(pathstr)
    map_contents = {}

    def configmap_callback(path):
        nonlocal map_contents
        # Canonicalize the path
        if path.is_symlink():
            try:
                path = path.resolve(strict=True)
            except:
                # We silently skip unresolveable symlinks
                return

        # Skip directories
        if path.is_dir():
            return
        with path.open() as f:
            map_contents[path.name] = f.read()

    walk(path, callback=configmap_callback)
    return map_contents
