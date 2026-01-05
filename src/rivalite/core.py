"""
Core utilities for the library Rivalite

These core utilities support the rest of the library. The functions here are designed for quick and easy optimizations for your code.
"""

from pathlib import Path
import importlib
import pydoc

class PrivateFileError(Exception):
    """
    Occurs when trying to use about() on a private file
    """
    pass

def ensure_list(value):
    """
    Returns the value as a list even if it isn't iterable

    - If the value is None, it returns an empty list.
    - If the value is a list; tuple; or set, it returns the data as a list
    - Otherwise, it wraps the value in a list
    """

    if value is None:
        return []

    if isinstance(value, (list, tuple, set)):
        return list(value)

    else:
        return [value]

def about(module=None):
    """
    Returns a list of all available modules if module is left None. Otherwise, it will go into detail on a module.
    Use help(rivalite) for the package itself
    """

    if module is None:
        package_dir = Path(__file__).parent
        files = [p.name for p in package_dir.iterdir()]
        for f in files[:]:
            if f.startswith("_"):
                files.remove(f)
        for i, f in enumerate(files):
            files[i] = f[:-3]
        return files

    module = str(module).strip()

    if module.startswith("_"):
        raise PrivateFileError(f"can't access {module}.py due to the file being private.")

    pkg = importlib.import_module(f"rivalite.{module}")
    render = pydoc.render_doc(pkg)
    return render
